import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont
import os

def add_text_watermark(input_image_path, output_image_path, watermark_text):
    # Open image and convert to RGBA
    image = Image.open(input_image_path).convert("RGBA")

    # Create transparent watermark layer
    watermark_layer = Image.new("RGBA", image.size, (255, 255, 255, 0))

    # Load TTF font - make sure LiberationSans-Regular.ttf is in your script folder
    font_path = "LiberationSans-Regular.ttf"
    font_size = max(int(min(image.size) * 0.35), 30)  # ~35% of smaller dimension, min 30
    font = ImageFont.truetype(font_path, font_size)

    # Create text image (transparent) for watermark
    text_bbox = font.getbbox(watermark_text)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_image = Image.new("RGBA", (text_width, text_height), (255, 255, 255, 0))
    text_draw = ImageDraw.Draw(text_image)
    # Black text, 50% opacity (alpha=128)
    text_draw.text((0, 0), watermark_text, font=font, fill=(0, 0, 0, 128))

    # Scale text image larger for a bigger watermark
    scale_factor = 1.5  # Adjust this for bigger/smaller watermark
    scaled_width = int(text_image.width * scale_factor)
    scaled_height = int(text_image.height * scale_factor)
    text_image = text_image.resize((scaled_width, scaled_height), resample=Image.BICUBIC)

    # Rotate the text image diagonally (45 degrees)
    rotated_text = text_image.rotate(45, expand=1)

    # Calculate position to center the rotated watermark
    pos_x = (image.width - rotated_text.width) // 2
    pos_y = (image.height - rotated_text.height) // 2

    # Paste rotated watermark onto transparent layer using alpha mask
    watermark_layer.paste(rotated_text, (pos_x, pos_y), rotated_text)

    # Composite watermark layer over original image
    watermarked = Image.alpha_composite(image, watermark_layer)

    # Convert back to RGB and save
    watermarked.convert("RGB").save(output_image_path)


class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Diagonal Black Watermark App")
        self.root.geometry("400x250")
        self.image_path = None

        tk.Label(root, text="Enter Watermark Text:").pack(pady=5)
        self.watermark_entry = tk.Entry(root, width=40)
        self.watermark_entry.pack()

        tk.Button(root, text="Select Image", command=self.load_image).pack(pady=10)
        self.selected_image_label = tk.Label(root, text="No image selected")
        self.selected_image_label.pack()

        tk.Button(root, text="Add Watermark and Save", command=self.apply_watermark).pack(pady=10)
        self.status_label = tk.Label(root, text="", fg="green")
        self.status_label.pack()

    def load_image(self):
        filetypes = [("Image files", "*.png *.jpg *.jpeg *.bmp")]
        filepath = filedialog.askopenfilename(title="Select an Image", filetypes=filetypes)
        if filepath:
            self.image_path = filepath
            self.selected_image_label.config(text=os.path.basename(filepath))

    def apply_watermark(self):
        if not self.image_path:
            messagebox.showwarning("No Image", "Please select an image first.")
            return

        watermark_text = self.watermark_entry.get().strip()
        if not watermark_text:
            messagebox.showwarning("No Watermark", "Please enter watermark text.")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                                 filetypes=[("JPEG Image", "*.jpg"), ("PNG Image", "*.png")],
                                                 title="Save Watermarked Image As")
        if save_path:
            add_text_watermark(self.image_path, save_path, watermark_text)
            self.status_label.config(text="Watermark added successfully!", fg="green")


if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
