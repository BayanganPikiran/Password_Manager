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

        self.fields_frame = self.create_fields_frame()

        self.website_entry_var = tk.StringVar()
        self.website_entry = self.create_website_entry()

        self.username_var = tk.StringVar()
        self.username_entry = self.create_username_entry()
        self.password_entry = None
        self.generate_password_btn = None
        self.retrieve_password_btn = None
        self.add_password_btn = None

    def create_logo_frame(self):
        logo_frame = tk.Frame(self.root)
        logo_frame.pack(expand=True, fill=tk.BOTH)
        return logo_frame

    def create_logo_canvas(self):
        canvas = tk.Canvas(self.logo_frame, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        logo = tk.PhotoImage(file="logo_resized.png")
        self.root.logo = logo  # keeps the logo from being garbage collected
        canvas.create_image((CANVAS_WIDTH / 2), (CANVAS_HEIGHT / 2), image=logo)
        canvas.pack()
        return canvas

    def create_fields_frame(self):
        fields_frame = tk.Frame(self.root)
        fields_frame.pack(expand=True, fill=tk.BOTH)
        return fields_frame

    def create_website_entry(self):
        web_entry = tk.Entry(self.fields_frame, bg='white', width=200, borderwidth=2,
                             textvariable=self.website_entry_var, justify=tk.LEFT)
        web_entry.insert(0, "Enter website url")
        web_entry.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW, padx=2, pady=2)
        return web_entry

    def create_username_entry(self):
        user_entry = tk.Entry(self.fields_frame, bg='white', width=200, borderwidth=2,
                              textvariable=self.username_var, justify=tk.LEFT)
        user_entry.insert(0, "Enter email or username")
        user_entry.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW, padx=2, pady=2)
        return user_entry





    def run_app(self):
        self.print_web_entry()
        self.root.mainloop()


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

if __name__ == '__main__':
    ui = UI()
    ui.run_app()
