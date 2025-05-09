import tkinter as tk
from model import Model
from view import View
from presenter import Presenter

if __name__ == "__main__":
    root = tk.Tk()
    model = Model()
    view = View(root)
    presenter = Presenter(model, view)
    root.mainloop()
