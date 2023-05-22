import tkinter as tk
from accounts import Account
from constants import *


class Toplevel(Account):
    def __init__(self, root, web_var, user_var, pass_var):
        Account.__init__(self, "password_accounts.db")
        self.root = root
        self.web_var = web_var.get()
        self.user_var = user_var.get()
        self.pass_var = pass_var.get()

    def save_record_toplevel(self):
        save_acct = tk.Toplevel(padx=5, pady=5)
        save_acct.geometry(("{}x{}".format(TL_WIDTH, TL_HEIGHT)))
        save_acct.title("Save Account Details")
        save_acct.wm_transient(self.root)
        label_frame = tk.Frame(save_acct, width=(TL_WIDTH-20), height=(TL_HEIGHT*.75))
        label_frame.pack(expand=True, fill=tk.BOTH)
        btn_frame = tk.Frame(save_acct, width=(TL_WIDTH-20), height=(TL_HEIGHT*.2))
        btn_frame.pack(expand=True, fill=tk.BOTH, pady=5)
        header = tk.Label(label_frame, text="Confirm the following details:", font=FONT_TOPLEVEL)
        site_label = tk.Label(label_frame, text=f"website: {self.web_var}", font=FONT_TOPLEVEL)
        user_label = tk.Label(label_frame, text=f"username: {self.user_var}", font=FONT_TOPLEVEL)
        pass_label = tk.Label(label_frame, text=f"password: {self.pass_var}", font=FONT_TOPLEVEL)
        header.grid(row=0, column=0, sticky=tk.NSEW, pady=5)
        site_label.grid(row=1, column=0, sticky=tk.W)
        user_label.grid(row=2, column=0, sticky=tk.W)
        pass_label.grid(row=3, column=0, sticky=tk.W)
        save_btn = tk.Button(btn_frame, text="Save", anchor=tk.CENTER,
                             command=lambda: [self.create_record(self.web_var,
                                                                 self.user_var,
                                                                 self.pass_var),
                                              save_acct.destroy()])
        save_btn.pack(expand=True, fill=tk.BOTH)
        save_acct.mainloop()

    def delete_record_toplevel(self):
        delete_record = tk.Toplevel()
        delete_record.geometry(("{}x{}".format(TL_WIDTH, TL_HEIGHT)))
        delete_record.title("Delete Record")
        delete_record.wm_transient(self.root)
        label_frame = tk.Frame(delete_record, width=(TL_WIDTH-20), height=(TL_HEIGHT*.75))
        label_frame.pack(expand=True, fill=tk.BOTH)
        btn_frame = tk.Frame(delete_record, width=(TL_WIDTH-20), height=(TL_HEIGHT*.2))
        btn_frame.pack(expand=True, fill=tk.BOTH)
        header = tk.Label(label_frame, text="Please confirm the deletion of the following record:", font=FONT_TOPLEVEL)
        header.pack(expand=True, fill=tk.BOTH)
        site = tk.Label(label_frame, text=f"Website: {self.web_var}", font=FONT_TOPLEVEL, anchor=tk.W)
        site.pack(expand=True, fill=tk.BOTH)
        user = tk.Label(label_frame, text=f"Username: {self.user_var}", font=FONT_TOPLEVEL, anchor=tk.W)
        user.pack(expand=True, fill=tk.BOTH)
        confirm_btn = tk.Button(btn_frame, text="Confirm delete", bg=BUTTON_GRAY,
                                command=lambda: [self.delete_record(self.web_var, self.user_var),
                                                 delete_record.destroy()])
        confirm_btn.pack(expand=True, fill=tk.BOTH)
        delete_record.mainloop()

    def retrieve_password_toplevel(self):
        web_var = self.website_var.get()
        user_var = self.username_var.get()
        pass_var = self.fetch_password(web_var, user_var)
        retrieve_pass = tk.Toplevel(width=200, height=200, pady=5, padx=5)
        retrieve_pass.title("Retrieve Password")
        retrieve_pass.wm_transient(self.root)
        header = tk.Label(retrieve_pass, text="The password for:", font=FONT_TOPLEVEL)
        header.pack(expand=True, fill=tk.BOTH)
        site = tk.Label(retrieve_pass, text=f"Website: {web_var}", anchor=tk.W, font=FONT_TOPLEVEL)
        site.pack(expand=True, fill=tk.BOTH)
        user = tk.Label(retrieve_pass, text=f"Username: {user_var}", anchor=tk.W, font=FONT_TOPLEVEL)
        user.pack(expand=True, fill=tk.BOTH)
        password = tk.Label(retrieve_pass, text=f"is: {pass_var}", anchor=tk.W, font=FONT_TOPLEVEL)
        password.pack(expand=True, fill=tk.BOTH)

    def update_password_toplevel(self):
        update_pass = tk.Toplevel(width=200, height=200, padx=5, pady=5)
        update_pass.title("Update Password")
        update_pass.wm_transient(self.root)
        label_frame = tk.Frame(update_pass, width=190, height=160)
        label_frame.pack(expand=True, fill=tk.BOTH)
        btn_frame = tk.Frame(update_pass, width=190, height=30, pady=5)
        btn_frame.pack(expand=True, fill=tk.BOTH)
        header = tk.Label(label_frame, text="You are updating your password for:", font=FONT_TOPLEVEL)
        header.pack(expand=True, fill=tk.BOTH)
        site = tk.Label(label_frame, text=f"Website: {self.web_var}", anchor=tk.W, font=FONT_TOPLEVEL)
        site.pack(expand=True, fill=tk.BOTH)
        user = tk.Label(label_frame, text=f"Username: {self.user_var}", anchor=tk.W, font=FONT_TOPLEVEL)
        user.pack(expand=True, fill=tk.BOTH)
        password = tk.Label(label_frame, text=f"To: {self.pass_var}", anchor=tk.W, font=FONT_TOPLEVEL)
        password.pack(expand=True, fill=tk.BOTH)
        confirm_btn = tk.Button(btn_frame, text="Update password",
                                command=lambda: [self.update_record(self.pass_var, self.web_var, self.user_var),
                                                 update_pass.destroy()])
        confirm_btn.pack(expand=True, fill=tk.BOTH)
        update_pass.mainloop()
