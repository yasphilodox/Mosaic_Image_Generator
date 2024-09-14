import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageOps
import os

class MosaicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mosaic Image Generator")
        
        self.upload_btn = tk.Button(root, text="Upload Images", command=self.upload_images)
        self.upload_btn.pack()
        
        self.select_btn = tk.Button(root, text="Select Base Image", command=self.select_base_image)
        self.select_btn.pack()
        
        self.generate_btn = tk.Button(root, text="Generate Mosaic", command=self.generate_mosaic)
        self.generate_btn.pack()
        
        self.image_folder = None
        self.base_image_path = None

    def upload_images(self):
        # Allow user to select multiple images
        filetypes = [("Image files", "*.jpg *.jpeg *.png")]
        image_files = filedialog.askopenfilenames(filetypes=filetypes)
        
        # Check if images are selected
        if not image_files:
            messagebox.showerror("No images selected", "Please select at least 30 images.")
            return

        # Store the selected images
        self.image_folder = image_files
        print(f"Images uploaded: {len(self.image_folder)} images")

    def select_base_image(self):
        # Allow user to select a base image (jpg/png)
        filetypes = [("Image files", "*.jpg *.jpeg *.png")]
        self.base_image_path = filedialog.askopenfilename(filetypes=filetypes)
        
        if not self.base_image_path:
            messagebox.showerror("No image selected", "Please select a base image.")
        else:
            print(f"Base image selected: {self.base_image_path}")

    def generate_mosaic(self):
        if not self.image_folder or not self.base_image_path:
            messagebox.showerror("Missing images", "Please upload images and select a base image.")
            return
        
        # Load the base image and convert it to grayscale
        base_image = Image.open(self.base_image_path).convert("L")
        base_image = ImageOps.grayscale(base_image)

        # Define the size of mosaic tiles
        tile_size = 50  # Adjust this value as needed
        mosaic_image = self.create_mosaic(base_image, tile_size)
        
        # Save the result as mosaic_output.jpg
        output_path = "mosaic_output.jpg"
        mosaic_image.save(output_path)
        messagebox.showinfo("Mosaic Generated", f"Mosaic saved as {output_path}")
    
    def create_mosaic(self, base_image, tile_size):
        # Load each image and convert to grayscale
        resized_images = []
        for img_path in self.image_folder:
            img = Image.open(img_path).convert("L")
            resized_images.append(img.resize((tile_size, tile_size)))

        # Create a blank canvas for the mosaic
        mosaic = Image.new("L", base_image.size)
        base_width, base_height = base_image.size
        
        for y in range(0, base_height, tile_size):
            for x in range(0, base_width, tile_size):
                # Crop a section from the base image
                region = base_image.crop((x, y, x + tile_size, y + tile_size))
                avg_brightness = self.calculate_average_brightness(region)
                
                # Find the image with the closest brightness
                best_match = min(resized_images, key=lambda img: abs(self.calculate_average_brightness(img) - avg_brightness))
                mosaic.paste(best_match, (x, y))

        return mosaic

    def calculate_average_brightness(self, img):
        # Calculate the average brightness of the image
        pixels = list(img.getdata())
        return sum(pixels) / len(pixels)


if __name__ == "__main__":
    root = tk.Tk()
    app = MosaicApp(root)
    root.mainloop()
