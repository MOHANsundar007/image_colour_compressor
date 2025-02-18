import os
import numpy as np
import cv2
import time
from flask import Flask, render_template, request, send_file

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
OUTPUT_FOLDER = "static"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def load_image(image_path):
    """Load and convert image to RGB format."""
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def initialize_centroids(X, K):
    """Initialize centroids using KMeans++ approach."""
    centroids = [X[np.random.randint(0, X.shape[0])]]
    for _ in range(1, K):
        distances = np.array([min([np.linalg.norm(x - c) for c in centroids]) for x in X])
        probabilities = distances / distances.sum()
        centroids.append(X[np.random.choice(X.shape[0], p=probabilities)])
    return np.array(centroids)

def assign_clusters(X, centroids):
    """Assign each pixel to the closest centroid."""
    distances = np.array([[np.linalg.norm(x - c) for c in centroids] for x in X])
    return np.argmin(distances, axis=1)

def update_centroids(X, labels, K):
    """Update centroids by calculating the mean of assigned pixels."""
    return np.array([X[labels == k].mean(axis=0) if np.any(labels == k) else X[np.random.randint(0, X.shape[0])] for k in range(K)])

def kmeans(X, K, max_iters=10):
    """Perform K-Means clustering."""
    centroids = initialize_centroids(X, K)
    for _ in range(max_iters):
        labels = assign_clusters(X, centroids)
        new_centroids = update_centroids(X, labels, K)
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    return centroids, labels

def compress_image(image_path, K=8):
    """Compress image using K-Means and return compressed image path and processing time."""
    start_time = time.time()

    image = load_image(image_path)
    original_shape = image.shape
    X = image.reshape(-1, 3)

    centroids, labels = kmeans(X, K)
    compressed_image = np.array([centroids[label] for label in labels], dtype=np.uint8).reshape(original_shape)

    compressed_path = os.path.join(OUTPUT_FOLDER, "compressed.png")
    cv2.imwrite(compressed_path, cv2.cvtColor(compressed_image, cv2.COLOR_RGB2BGR))

    compression_time = round(time.time() - start_time, 3)
    return compressed_path, compression_time

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        K = int(request.form["clusters"])

        filename = file.filename
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        compressed_path, time_taken = compress_image(file_path, K)

        return render_template("index.html", 
                       original=f"static/uploads/{filename}", 
                       compressed="static/compressed.png", 
                       time_taken=time_taken)


    return render_template("index.html", original=None, compressed=None, time_taken=None)

@app.route("/download")
def download():
    return send_file(os.path.join(OUTPUT_FOLDER, "compressed.png"), as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
