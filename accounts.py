import random
import tkinter as tk


class Account:

    def __init__(self):
        self.accounts_dictionary = {}
        self.new_account = {}
        self.website = None
        self.username = None
        self.password = None
        self.up_cap_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                               "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.low_cap_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.symbols = []

    def save_account(self, website, username, password):
        account = {website: [username, password]}
        self.accounts_dictionary.update(account)
