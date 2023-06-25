import tkinter as tk
from constants import *
from accounts import *
import random


class UI(Account):
    def __init__(self):
        Account.__init__(self, "password_accounts.db")
        self.root = tk.Tk()
        self.root.geometry(("{}x{}".format(ROOT_WIDTH, ROOT_HEIGHT)))
        self.root.resizable(None, None)
        self.root.title("Password Manager")

        self.logo_frame = self.create_logo_frame()
        self.logo_canvas = self.create_logo_canvas()

        self.fields_frame = self.create_fields_frame()

        self.website_var = tk.StringVar()
        self.website_entry = self.create_website_entry()

        self.username_var = tk.StringVar()
        self.username_entry = self.create_username_entry()

        self.password_var = tk.StringVar()
        self.password_entry = self.create_password_entry()

        self.generate_password_btn = self.create_gen_pass_btn()
        self.save_record_btn = self.create_save_record_btn()
        self.delete_record_btn = self.create_del_record_btn()
        self.retrieve_password_btn = self.create_retrieve_pass_btn()
        self.update_password_btn = self.create_update_pass_btn()

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
        web_entry = tk.Entry(self.fields_frame, bg='white', width=82, borderwidth=2,
                             textvariable=self.website_var, justify=tk.LEFT)
        web_entry.insert(0, "Enter website url")
        web_entry.grid(row=0, column=0, columnspan=3, sticky=tk.NSEW, padx=2, pady=2)
        return web_entry

    def create_username_entry(self):
        user_entry = tk.Entry(self.fields_frame, bg='white', width=82, borderwidth=2,
                              textvariable=self.username_var, justify=tk.LEFT)
        user_entry.insert(0, "Enter email or username")
        user_entry.grid(row=1, column=0, columnspan=3, sticky=tk.NSEW, padx=2, pady=2)
        return user_entry

    def create_password_entry(self):
        password_entry = tk.Entry(self.fields_frame, bg='white', width=40, borderwidth=2,
                                  textvariable=self.password_var, justify=tk.LEFT)
        password_entry.insert(0, "Enter password or click generate button")
        password_entry.grid(row=2, column=0, sticky=tk.NSEW, padx=2, pady=2)
        return password_entry

    def create_gen_pass_btn(self):
        gen_pass = tk.Button(self.fields_frame, bg=BUTTON_GRAY, command=self.generate_password,
                             width=37, text="Generate password")
        gen_pass.grid(row=2, column=1, sticky=tk.NSEW, padx=2, pady=2)
        return gen_pass

    def generate_password(self):
        password_list = []
        for i in range(len(MERGED_CHARS)):
            password_list += random.sample(MERGED_CHARS[i], 4)
        password = ''.join(sorted(password_list, key=lambda x: random.random()))
        self.password_var.set(password)

    def create_retrieve_pass_btn(self):
        get_pass = tk.Button(self.fields_frame, bg=BUTTON_GRAY,
                             command=lambda: self.retrieve_password_toplevel(),
                             width=20, text="Retrieve password")
        get_pass.grid(row=4, column=0, sticky=tk.NSEW, padx=2, pady=2)
        return get_pass

    def retrieve_password_toplevel(self):
        web_var = self.website_var.get()
        user_var = self.username_var.get()
        pass_var = self.fetch_password(web_var, user_var)
        retrieve_pass = tk.Toplevel(width=200, height=200, pady=5, padx=5)
        retrieve_pass.title("Get Password")
        retrieve_pass.wm_transient(self.root)
        site = tk.Label(retrieve_pass, text=f"Website: {web_var}", anchor=tk.W, font=FONT_TOPLEVEL)
        site.pack(expand=True, fill=tk.BOTH)
        user = tk.Label(retrieve_pass, text=f"Username: {user_var}", anchor=tk.W, font=FONT_TOPLEVEL)
        user.pack(expand=True, fill=tk.BOTH)
        copy_pass = tk.Label(retrieve_pass, text="Copy the following:", anchor=tk.CENTER, font=("Helvetica", 10))
        copy_pass.pack(expand=True, fill=tk.BOTH)
        password = tk.Entry(retrieve_pass, bd=0, font=FONT_TOPLEVEL)
        password.insert(0, pass_var)
        password.pack(expand=True, fill=tk.BOTH)
        close_btn = tk.Button(retrieve_pass, bg=BUTTON_GRAY, text="Close Window",
                              command=lambda: retrieve_pass.destroy())
        close_btn.pack(expand=True, fill=tk.BOTH)

    def create_update_pass_btn(self):
        update_btn = tk.Button(self.fields_frame, bg=BUTTON_GRAY, text="Update password",
                               command=self.create_update_pass_toplevel)
        update_btn.grid(row=4, column=1, sticky=tk.NSEW, padx=2, pady=2)
        return update_btn

    def create_update_pass_toplevel(self):
        web_var = self.website_var.get()
        user_var = self.username_var.get()
        pass_var = self.password_var.get()
        update_pass = tk.Toplevel(width=200, height=200, padx=5, pady=5)
        update_pass.title("Update Password")
        update_pass.wm_transient(self.root)
        label_frame = tk.Frame(update_pass, width=190, height=160)
        label_frame.pack(expand=True, fill=tk.BOTH)
        btn_frame = tk.Frame(update_pass, width=190, height=30, pady=5)
        btn_frame.pack(expand=True, fill=tk.BOTH)
        header = tk.Label(label_frame, text="You are updating your password for:", font=FONT_TOPLEVEL)
        header.pack(expand=True, fill=tk.BOTH)
        site = tk.Label(label_frame, text=f"Website: {web_var}", anchor=tk.W, font=FONT_TOPLEVEL)
        site.pack(expand=True, fill=tk.BOTH)
        user = tk.Label(label_frame, text=f"Username: {user_var}", anchor=tk.W, font=FONT_TOPLEVEL)
        user.pack(expand=True, fill=tk.BOTH)
        password = tk.Label(label_frame, text=f"To: {pass_var}", anchor=tk.W, font=FONT_TOPLEVEL)
        password.pack(expand=True, fill=tk.BOTH)
        confirm_btn = tk.Button(btn_frame, text="Update password",
                                command=lambda: [self.update_record(pass_var, web_var, user_var),
                                                 self.confirm_record_input(), update_pass.destroy()])
        confirm_btn.pack(expand=True, fill=tk.BOTH)

    def create_save_record_btn(self):
        add_pass = tk.Button(self.fields_frame, bg=BUTTON_GRAY, command=self.create_save_toplevel,
                             width=20, text="Save record")
        add_pass.grid(row=3, column=0, sticky=tk.NSEW, padx=2, pady=2)
        return add_pass

    def create_save_toplevel(self):
        save_acct = tk.Toplevel(width=200, height=200, pady=5, padx=5)
        save_acct.title("Save Account Details")
        save_acct.wm_transient(self.root)
        label_frame = tk.Frame(save_acct, width=190, height=160)
        label_frame.pack(expand=True, fill=tk.BOTH)
        btn_frame = tk.Frame(save_acct, width=190, height=30)
        btn_frame.pack(expand=True, fill=tk.BOTH, pady=5)
        header = tk.Label(label_frame, text="Confirm the following details:", font=FONT_TOPLEVEL)
        site_label = tk.Label(label_frame, text=f"website: {self.website_var.get()}", font=FONT_TOPLEVEL)
        user_label = tk.Label(label_frame, text=f"username: {self.username_var.get()}", font=FONT_TOPLEVEL)
        pass_label = tk.Label(label_frame, text=f"password: {self.password_var.get()}", font=FONT_TOPLEVEL)
        header.grid(row=0, column=0, sticky=tk.NSEW, pady=5)
        site_label.grid(row=1, column=0, sticky=tk.W)
        user_label.grid(row=2, column=0, sticky=tk.W)
        pass_label.grid(row=3, column=0, sticky=tk.W)
        save_btn = tk.Button(btn_frame, text="Save", anchor=tk.CENTER,
                             command=lambda: [self.create_record(self.website_var.get(),
                                                                 self.username_var.get(),
                                                                 self.password_var.get()),
                                              self.confirm_record_input(),
                                              save_acct.destroy()], )
        save_btn.pack(expand=True, fill=tk.BOTH)
        save_acct.mainloop()

    def create_del_record_btn(self):
        del_pas = tk.Button(self.fields_frame, bg=BUTTON_GRAY,
                            command=lambda: self.create_delete_toplevel(),
                            width=20, text="Delete record")
        del_pas.grid(row=3, column=1, sticky=tk.NSEW, padx=2, pady=2)
        return del_pas

    def create_delete_toplevel(self):
        web_var = self.website_var.get()
        user_var = self.username_var.get()
        delete_record = tk.Toplevel(width=200, height=200, pady=5, padx=5)
        delete_record.title("Delete Record")
        delete_record.wm_transient(self.root)
        label_frame = tk.Frame(delete_record, width=190, height=160)
        label_frame.pack(expand=True, fill=tk.BOTH)
        btn_frame = tk.Frame(delete_record, width=190, height=30)
        btn_frame.pack(expand=True, fill=tk.BOTH)
        header = tk.Label(label_frame, text="Please confirm the deletion of the following record:", font=FONT_TOPLEVEL)
        header.pack(expand=True, fill=tk.BOTH)
        site = tk.Label(label_frame, text=f"Website: {web_var}", font=FONT_TOPLEVEL, anchor=tk.W)
        site.pack(expand=True, fill=tk.BOTH)
        user = tk.Label(label_frame, text=f"Username: {user_var}", font=FONT_TOPLEVEL, anchor=tk.W)
        user.pack(expand=True, fill=tk.BOTH)
        confirm_btn = tk.Button(btn_frame, text="Confirm delete", bg=BUTTON_GRAY,
                                command=lambda: [self.delete_record(web_var, user_var),
                                                 self.confirm_record_input(), delete_record.destroy()])
        confirm_btn.pack(expand=True, fill=tk.BOTH)



    def get_account_elements(self):
        website = self.website_var.get()
        username = self.username_var.get()
        password = self.password_var.get()
        return website, username, password

    def run_app(self):
        self.root.mainloop()


if __name__ == '__main__':
    ui = UI()
    ui.run_app()
