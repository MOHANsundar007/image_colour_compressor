# image_colour_compressor
Image Colour Compression Using K-Means Clustering
This project implements image compression using the K-Means clustering algorithm. The Flask-based web application allows users to upload an image, apply K-Means clustering to compress the image, and download the compressed version.

Features:
Upload an image and choose the number of clusters (K).
The image is compressed using the K-Means clustering algorithm.
Displays both the original and compressed images.
Provides a download link for the compressed image.
Tech Stack:
Flask: A lightweight web framework used to create the web application.
OpenCV: A computer vision library for image processing.
NumPy: Used for numerical operations and handling arrays in the K-Means algorithm.
HTML, CSS, and Bootstrap: For the user interface.
Project Overview:
The project uses the K-Means clustering algorithm to compress the colors in an image. It works by reducing the number of unique colors used in the image, making it smaller while trying to preserve the overall visual appearance. The number of clusters (K) can be customized by the user to control the compression level.

How It Works:
Image Upload: The user uploads an image through the web interface.
K-Means Clustering: The image is processed using the K-Means algorithm to compress the image by reducing the number of colors.
Display Results: Both the original and the compressed images are displayed on the web page.
Download: A download link is provided for the compressed image.
Prerequisites:
Before running the project, make sure you have the following installed:

Python 3.x
pip (Python package manager)
Required Libraries:
Flask
OpenCV
NumPy

