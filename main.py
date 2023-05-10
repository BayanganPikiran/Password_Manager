import tkinter as tk
from constants import *

class UI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(("{}x{}".format(ROOT_WIDTH, ROOT_HEIGHT)))
        self.root.resizable(None, None)
        self.image_frame = None
        self_fields_frame = None

    def run_app(self):
        self.root.mainloop()

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

if __name__ == '__main__':
    ui = UI()
    ui.run_app()
