import tkinter as tk
from constants import *
import random


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

        self.password_var = tk.StringVar()
        self.password_entry = self.create_password_entry()

        self.generate_password_btn = self.create_gen_pass_btn()
        self.get_password_btn = self.create_get_pass_btn()
        self.save_password_btn = self.create_save_pass_btn()
        self.delete_password_btn = self.create_del_pass_btn()

    def create_logo_frame(self):
        logo_frame = tk.Frame(self.root, bg=BACKGROUND_WHITE)
        logo_frame.pack(expand=True, fill=tk.BOTH)
        return logo_frame

    def create_logo_canvas(self):
        canvas = tk.Canvas(self.logo_frame, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=BACKGROUND_WHITE)
        logo = tk.PhotoImage(file="logo_resized.png")
        self.root.logo = logo  # keeps the logo from being garbage collected
        canvas.create_image((CANVAS_WIDTH / 2), (CANVAS_HEIGHT / 2), image=logo)
        canvas.pack()
        return canvas

    def create_fields_frame(self):
        fields_frame = tk.Frame(self.root, bg=BACKGROUND_WHITE, padx=5, pady=5)
        fields_frame.pack(expand=True, fill=tk.BOTH)
        return fields_frame

    def create_website_entry(self):
        web_entry = tk.Entry(self.fields_frame, bg='white', width=83, borderwidth=2,
                             textvariable=self.website_entry_var, justify=tk.LEFT)
        web_entry.insert(0, "Enter website url")
        web_entry.grid(row=0, column=0, columnspan=3, sticky=tk.NSEW, padx=2, pady=2)
        return web_entry

    def create_username_entry(self):
        user_entry = tk.Entry(self.fields_frame, bg='white', width=83, borderwidth=2,
                              textvariable=self.username_var, justify=tk.LEFT)
        user_entry.insert(0, "Enter email or username")
        user_entry.grid(row=1, column=0, columnspan=3, sticky=tk.NSEW, padx=2, pady=2)
        return user_entry

    def create_password_entry(self):
        password_entry = tk.Entry(self.fields_frame, bg='white', width=50, borderwidth=2,
                                  textvariable=self.password_var, justify=tk.LEFT)
        password_entry.insert(0, "Enter your own password or click generate button")
        password_entry.grid(row=2, column=0, columnspan=2, sticky=tk.NSEW, padx=2, pady=2)
        return password_entry

    def create_gen_pass_btn(self):
        gen_pass = tk.Button(self.fields_frame, bg=BUTTON_GRAY, command=self.generate_password,
                             width=5, text="Generate password")
        gen_pass.grid(row=2, column=2, sticky=tk.NSEW, padx=2, pady=2)
        return gen_pass

    def generate_password(self):
        password_list = []
        for i in range(len(MERGED_CHARS)):
            password_list += random.sample(MERGED_CHARS[i], 4)
        password = ''.join(sorted(password_list, key=lambda x: random.random()))
        self.password_var.set(password)
        self.save_password()

    def create_get_pass_btn(self):
        get_pass = tk.Button(self.fields_frame, bg=BUTTON_GRAY, command=self.get_password,
                             width=20, text="Retrieve password")
        get_pass.grid(row=3, column=0, sticky=tk.NSEW, padx=2, pady=2)
        return get_pass

    def get_password(self):
        pass

    def create_save_pass_btn(self):
        add_pass = tk.Button(self.fields_frame, bg=BUTTON_GRAY, command=self.create_save_toplevel,
                             width=20, text="Save password")
        add_pass.grid(row=3, column=1, sticky=tk.NSEW, padx=2, pady=2)
        return add_pass

    def create_save_toplevel(self):
        save_acct = tk.Toplevel(width=200, height=200)
        save_acct.wm_transient(self.root)
        label_frame = tk.Frame(save_acct, width=190, height=160)
        label_frame.pack(expand=True, fill=tk.BOTH)
        btn_frame = tk.Frame(save_acct, width=190, height=30)
        btn_frame.pack(expand=True, fill=tk.BOTH)
        header = tk.Label(label_frame, text="Confirm the following details:")
        site_label = tk.Label(label_frame, text=f"website: {self.website_entry_var.get()}")
        user_label = tk.Label(label_frame, text=f"username: {self.username_var.get()}")
        pass_label = tk.Label(label_frame, text=f"password: {self.username_var.get()}")
        header.grid(row=0, column=0, sticky=tk.NSEW)
        site_label.grid(row=1, column=0, sticky=tk.NSEW)
        user_label.grid(row=2, column=0, sticky=tk.NSEW)
        pass_label.grid(row=3, column=0, sticky=tk.NSEW)
        save_btn = tk.Button(btn_frame, text="Save", anchor=tk.CENTER, command=self.save_password)
        save_btn.pack(expand=True, fill=tk.BOTH)
        save_acct.mainloop()

    def save_password(self):
        pass

    def create_del_pass_btn(self):
        del_pas = tk.Button(self.fields_frame, bg=BUTTON_GRAY, command=self.delete_password,
                            width=20, text="Delete password")
        del_pas.grid(row=3, column=2, sticky=tk.NSEW, padx=2, pady=2)
        return del_pas

    def delete_password(self):
        pass

    def get_account_elements(self):
        website = self.website_entry_var.get()
        username = self.username_var.get()
        password = self.password_var.get()
        return website, username, password

    def run_app(self):
        self.root.mainloop()


if __name__ == '__main__':
    ui = UI()
    ui.run_app()
