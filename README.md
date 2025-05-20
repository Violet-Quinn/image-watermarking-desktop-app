# Watermark App in Python

This project is a desktop application built with Python's Tkinter and Pillow libraries that allows users to add a watermark text to their images. The watermark is semi-transparent, rotated at 45 degrees, and centered over the image for a professional look.

---

## 🎨 Features

- **User-Friendly GUI**: Simple interface to input watermark text, select an image, and save the watermarked output.
- **Diagonal Watermark**: The watermark text is rotated 45 degrees and placed diagonally across the image.
- **Dynamic Font Size**: The watermark scales based on the size of the image to ensure visibility without overpowering the photo.
- **Semi-Transparent Text**: The watermark text is black with 50% opacity, allowing the image to show through.
- **Supports Common Image Formats**: Load PNG, JPG, JPEG, BMP images and save output as PNG or JPG.
- **Save-As Dialog**: Allows saving the edited image to a custom location and filename.

---

## ⚙️ Requirements

- Python 3.x
- Tkinter (usually included with Python)
- Pillow (`pip install Pillow`)

---

## 📂 Important Note

Make sure the font file **`LiberationSans-Regular.ttf`** is placed in the same folder as the Python script before running the application. This font file is required for rendering the watermark text.

---

## ▶️ How to Run

1. Ensure you have the required dependencies installed.
2. Place `LiberationSans-Regular.ttf` in the script folder.
3. Run the Python script:

```bash
python watermark_app.py
```

4. Enter the desired watermark text in the input box.
5. Click "Select Image" to choose your image file.
6. Click "Add Watermark and Save" to apply the watermark and save the new image.
