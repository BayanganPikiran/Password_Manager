import tkinter as tk
from constants import *


class UI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(("{}x{}".format(ROOT_WIDTH, ROOT_HEIGHT)))
        self.root.resizable(None, None)
        self.root.title("Password Manager")
        self.logo_frame = self.create_logo_frame()
        self.logo_canvas = self.create_logo_canvas()
        self_fields_frame = None

    def create_logo_frame(self):
        logo_frame = tk.Frame(self.root)
        logo_frame.pack(expand=True, fill=tk.BOTH)
        return logo_frame

    def create_logo_canvas(self):
        canvas = tk.Canvas(self.logo_frame, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        logo = tk.PhotoImage(file="logo_resized.png")
        self.root.logo = logo
        canvas.create_image((CANVAS_WIDTH / 2), (CANVAS_HEIGHT / 2), image=logo)
        canvas.pack()
        return canvas

    def run_app(self):
        self.root.mainloop()


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

if __name__ == '__main__':
    ui = UI()
    ui.run_app()
