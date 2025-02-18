# Image Colour Compressor

Image Colour Compression Using K-Means Clustering

This project implements image compression using the K-Means clustering algorithm. The Flask-based web application allows users to upload an image, apply K-Means clustering to compress the image, and download the compressed version.

## Features:
- Upload an image and choose the number of clusters (K).
- The image is compressed using the K-Means clustering algorithm.
- Displays both the original and compressed images.
- Provides a download link for the compressed image.

## Tech Stack:
- **Flask**: A lightweight web framework used to create the web application.
- **OpenCV**: A computer vision library for image processing.
- **NumPy**: Used for numerical operations and handling arrays in the K-Means algorithm.
- **HTML, CSS, Bootstrap**: For building the user interface.

## Project Overview:
This project uses the K-Means clustering algorithm to compress the colors in an image. By reducing the number of unique colors, the image size is reduced while attempting to maintain its visual appearance. Users can customize the number of clusters (K) to control the compression level, allowing for both higher compression and higher image quality.

## How It Works:
1. **Image Upload**: The user uploads an image through the web interface.
2. **K-Means Clustering**: The image is processed using the K-Means algorithm to compress the image by reducing the number of colors.
3. **Display Results**: Both the original and compressed images are displayed on the web page.
4. **Download**: A download link is provided for the compressed image.

## Prerequisites:
Before running the project, ensure that you have the following installed:
- Python 3.x
- pip (Python package manager)

## Installation:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/MOHANsundar007/image_colour_compressor.git
    cd image_colour_compressor
    ```

2. **Install the Required Libraries**:
    ```bash
    pip install -r requirements.txt
    ```
    Alternatively, you can install the libraries individually:
    ```bash
    pip install flask opencv-python numpy
    ```

## Running the Application:

1. **Start the Flask Application**:
    ```bash
    python app.py
    ```

2. **Access the Web Interface**:
    Open a web browser and go to:
    ```
    http://127.0.0.1:5000
    ```

3. **Upload an Image and Compress**:
    - Upload an image file.
    - Choose the number of clusters (K).
    - View the original and compressed images on the web page.
    - Download the compressed image.
