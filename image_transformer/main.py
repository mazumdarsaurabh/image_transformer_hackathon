# main.py

import tkinter as tk
from logic import ImageProcessor
from gui import ImageTransformerGUI

def main():
    root = tk.Tk()
    root.title("Image Transformer Tool")
    app = ImageTransformerGUI(root, ImageProcessor())
    root.mainloop()

if __name__ == "__main__":
    main()
