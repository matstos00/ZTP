import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

class View:
    """Klasa Widok obsługująca graficzny interfejs użytkownika."""

    def __init__(self, root):
        self.root = root
        self.root.title("Aplikacja do kompresji obrazów")

        self.label = tk.Label(root, text="Wybierz obraz do kompresji")
        self.label.pack()

        self.load_button = tk.Button(root, text="Wczytaj obraz", command=None)
        self.load_button.pack()

        self.slider = tk.Scale(root, from_=1, to=200, orient="horizontal", label="Liczba wartości osobliwych (r)")
        self.slider.pack()

        self.compress_button = tk.Button(root, text="Kompresuj obraz", command=None)
        self.compress_button.pack()

        self.image_label = tk.Label(root)
        self.image_label.pack()

    def display_image(self, image):
        """Wyświetlanie obrazu na GUI."""
        self.image = ImageTk.PhotoImage(image)
        self.image_label.config(image=self.image)

    def get_slider_value(self):
        """Zwraca wartość z suwaka."""
        return self.slider.get()

    def set_load_button_command(self, command):
        """Ustawia funkcję dla przycisku ładowania obrazu."""
        self.load_button.config(command=command)

    def set_compress_button_command(self, command):
        """Ustawia funkcję dla przycisku kompresji."""
        self.compress_button.config(command=command)
