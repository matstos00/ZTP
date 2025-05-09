from PIL import Image
from tkinter import filedialog
import numpy as np


class Presenter:
    """Klasa Prezenter łącząca model i widok."""

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.image_matrix = None
        self.mode = None

        self.view.set_load_button_command(self.load_image)
        self.view.set_compress_button_command(self.compress_image)

    def load_image(self):
        """Obsługa ładowania obrazu."""
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.bmp")])
        if file_path:
            try:
                image_matrix, mode = self.model.load_image(file_path)
                self.image_matrix = image_matrix
                self.mode = mode
                image = Image.open(file_path)
                self.view.display_image(image)
            except ValueError as e:
                print(e)

    def compress_image(self):
        """Obsługa kompresji obrazu."""
        if self.image_matrix is None:
            print("Najpierw wczytaj obraz.")
            return
        r = self.view.get_slider_value()
        try:
            compressed_matrix = self.model.svd_compression(self.image_matrix, self.mode, r)
            compressed_image = Image.fromarray(np.uint8(np.clip(compressed_matrix, 0, 255)))
            self.view.display_image(compressed_image)
        except ValueError as e:
            print(e)
