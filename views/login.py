import tkinter as tk
from tkinter import ttk

def show_login_info(info_label):
    info_label.config(text="Please enter your credentials to login.")

    # Tạo frame cho form đăng nhập
    login_frame = ttk.Frame(info_label.master)
    login_frame.pack(pady=20)

    # Tạo các trường nhập liệu cho đăng nhập
    tk.Label(login_frame, text="Username:").pack(pady=5)
    username_entry = ttk.Entry(login_frame)
    username_entry.pack(pady=5)

    tk.Label(login_frame, text="Password:").pack(pady=5)
    password_entry = ttk.Entry(login_frame, show="*")
    password_entry.pack(pady=5)

    def login():
        username = username_entry.get()
        password = password_entry.get()
        info_label.config(text=f"Trying to login with:\nUsername: {username}\nPassword: {password}")

    # Tạo button Login
    login_button = ttk.Button(login_frame, text="Login", command=login)
    login_button.pack(pady=10)
