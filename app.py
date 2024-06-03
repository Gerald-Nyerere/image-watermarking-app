import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont
 
class ImageWatermarkApp:
    def __init__(self, master):
        self.master = master
        master.title("Image Watermarking App")
 
        self.label = tk.Label(master, text="Select Image:",  fg="green")
        self.label.pack()
 
        self.select_button = tk.Button(master, text="Browse", command=self.select_image, bg="blue")
        self.select_button.pack()
 
        self.watermark_label = tk.Label(master, text="Watermark Text:", fg="green")
        self.watermark_label.pack()
 
        self.watermark_entry = tk.Entry(master)
        self.watermark_entry.pack()
 
        self.watermark_button = tk.Button(master, text="Apply Watermark", command=self.apply_watermark, bg="red")
        self.watermark_button.pack()
 
    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg; *.jpeg; *.png; *.bmp")])
        self.image = Image.open(file_path)
        self.image.show()
       
 
    def apply_watermark(self):
        if hasattr(self, 'image'):
            watermark_text = self.watermark_entry.get()
            if watermark_text:
                # Add watermark
                width, height = self.image.size
                draw = ImageDraw.Draw(self.image)
                font = ImageFont.load_default()
                text_width, text_height = draw.textsize(watermark_text, font=font)
                margin = 10
                x = width - text_width - margin
                y = height - text_height - margin
                draw.text((x, y), watermark_text, fill=(255, 255, 255, 128), font=font)
                self.image.show()
            else:
                tk.messagebox.showwarning("Warning", "Please enter watermark text.")
        else:
            tk.messagebox.showwarning("Warning", "Please select an image.")
 
def main():
    root = tk.Tk()
    app = ImageWatermarkApp(root)
    root.mainloop()
 
if __name__ == "__main__":
    main()