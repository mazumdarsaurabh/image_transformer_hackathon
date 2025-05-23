# logic.py

import cv2
import numpy as np

class ImageProcessor:
    def __init__(self):
        self.original = None
        self.processed = None

    def load_image(self, path):
        self.original = cv2.imread(path)
        self.processed = self.original.copy()
        return self.processed

    def reset_image(self):
        if self.original is not None:
            self.processed = self.original.copy()
        return self.processed

    def get_image(self):
        return self.processed

    def convert_to_grayscale(self):
        self.processed = cv2.cvtColor(self.processed, cv2.COLOR_BGR2GRAY)

    def apply_gaussian_blur(self, ksize=5):
        self.processed = cv2.GaussianBlur(self.processed, (ksize, ksize), 0)

    def apply_median_blur(self, ksize=5):
        self.processed = cv2.medianBlur(self.processed, ksize)

    def sobel_edge_detection(self):
        gray = cv2.cvtColor(self.processed, cv2.COLOR_BGR2GRAY)
        self.processed = cv2.Sobel(gray, cv2.CV_64F, 1, 1, ksize=5)

    def canny_edge_detection(self):
        self.processed = cv2.Canny(self.processed, 100, 200)

    def threshold(self):
        gray = cv2.cvtColor(self.processed, cv2.COLOR_BGR2GRAY)
        _, self.processed = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    def rotate(self, angle):
        (h, w) = self.processed.shape[:2]
        M = cv2.getRotationMatrix2D((w // 2, h // 2), angle, 1)
        self.processed = cv2.warpAffine(self.processed, M, (w, h))

    def resize(self, fx=0.5, fy=0.5):
        self.processed = cv2.resize(self.processed, (0, 0), fx=fx, fy=fy)

    def erode(self, ksize=3):
        kernel = np.ones((ksize, ksize), np.uint8)
        self.processed = cv2.erode(self.processed, kernel, iterations=1)

    def dilate(self, ksize=3):
        kernel = np.ones((ksize, ksize), np.uint8)
        self.processed = cv2.dilate(self.processed, kernel, iterations=1)

    def adjust_brightness(self, value=30):
        hsv = cv2.cvtColor(self.processed, cv2.COLOR_BGR2HSV)
        hsv[:, :, 2] = np.clip(hsv[:, :, 2] + value, 0, 255)
        self.processed = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    def flip(self, mode=1):
        self.processed = cv2.flip(self.processed, mode)
