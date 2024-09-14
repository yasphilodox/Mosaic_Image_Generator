
# Mosaic Image Generator
(need a lot more work it was just for testing the library) 
This is a simple Python-based application that generates a mosaic image from a base image using a collection of uploaded images. The mosaic is composed of small grayscale images arranged in such a way that they represent the base image when viewed from a distance.




## Features
- **Upload Images**: Select multiple images (JPEG, JPG, PNG) to use as tiles for the mosaic.
- **Select Base Image**: Choose an image that will be transformed into a mosaic.
- **Generate Mosaic**: The app generates a mosaic based on the brightness values of the images provided.

## Requirements
- Python 3.x
- Pillow (Python Imaging Library)

## Installation

1. Clone or download the project.
2. Install the required dependencies using `pip`:

    ```bash
    pip install pillow
    ```

3. Run the `mosaic_app.py` script:

    ```bash
    python mosaic_app.py
    ```

## Usage

1. **Upload Images**: Click on the "Upload Images" button and select at least 30 images from your system.
2. **Select Base Image**: Click on the "Select Base Image" button and choose the image you want to turn into a mosaic.
3. **Generate Mosaic**: Click on the "Generate Mosaic" button to render and save the mosaic as `mosaic_output.jpg`.

## File Structure

```
mosaic_app/
│
├── mosaic_app.py        # Main application script
└── README.md            # Project readme file
```



 
