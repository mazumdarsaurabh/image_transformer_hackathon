# gui.py

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2

class ImageTransformerGUI:
    def __init__(self, root, processor):
        self.root = root
        self.processor = processor
        self.panel = tk.Label(root)
        self.panel.pack()

        button_frame = tk.Frame(root)
        button_frame.pack()

        self.add_button(button_frame, "Upload", self.upload_image)
        self.add_button(button_frame, "Grayscale", processor.convert_to_grayscale)
        self.add_button(button_frame, "Gaussian Blur", lambda: processor.apply_gaussian_blur(5))
        self.add_button(button_frame, "Median Blur", lambda: processor.apply_median_blur(5))
        self.add_button(button_frame, "Sobel Edge", processor.sobel_edge_detection)
        self.add_button(button_frame, "Canny Edge", processor.canny_edge_detection)
        self.add_button(button_frame, "Threshold", processor.threshold)
        self.add_button(button_frame, "Rotate", lambda: processor.rotate(45))
        self.add_button(button_frame, "Resize", processor.resize)
        self.add_button(button_frame, "Erode", processor.erode)
        self.add_button(button_frame, "Dilate", processor.dilate)
        self.add_button(button_frame, "Brighten", processor.adjust_brightness)
        self.add_button(button_frame, "Flip", processor.flip)
        self.add_button(button_frame, "Reset", processor.reset_image)
        self.add_button(button_frame, "Save", self.save_image)

    def add_button(self, parent, text, command):
        tk.Button(parent, text=text, command=lambda: [command(), self.show_image()]).pack(side=tk.LEFT, padx=2)

    def upload_image(self):
        path = filedialog.askopenfilename()
        if path:
            try:
                self.processor.load_image(path)
                self.show_image()
            except:
                messagebox.showerror("Error", "Invalid image file.")

    def save_image(self):
        file = filedialog.asksaveasfilename(defaultextension=".jpg")
        if file:
            cv2.imwrite(file, self.processor.get_image())

    def show_image(self):
        image = self.processor.get_image()
        if len(image.shape) == 2:  # grayscale
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
        else:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(image)
        imgtk = ImageTk.PhotoImage(image=im)
        self.panel.configure(image=imgtk)
        self.panel.image = imgtk
