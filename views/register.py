import tkinter as tk
from tkinter import ttk

def show_register_info(info_label):
    info_label.config(text="Please fill out the registration form.")

    # Tạo frame cho form đăng ký
    register_frame = ttk.Frame(info_label.master)
    register_frame.pack(pady=20)

    # Tạo các trường nhập liệu cho đăng ký
    tk.Label(register_frame, text="First Name:").pack(pady=5)
    first_name_entry = ttk.Entry(register_frame)
    first_name_entry.pack(pady=5)

    tk.Label(register_frame, text="Last Name:").pack(pady=5)
    last_name_entry = ttk.Entry(register_frame)
    last_name_entry.pack(pady=5)

    tk.Label(register_frame, text="Email:").pack(pady=5)
    email_entry = ttk.Entry(register_frame)
    email_entry.pack(pady=5)

    tk.Label(register_frame, text="Username:").pack(pady=5)
    reg_username_entry = ttk.Entry(register_frame)
    reg_username_entry.pack(pady=5)

    tk.Label(register_frame, text="Password:").pack(pady=5)
    reg_password_entry = ttk.Entry(register_frame, show="*")
    reg_password_entry.pack(pady=5)

    def register():
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        email = email_entry.get()
        username = reg_username_entry.get()
        password = reg_password_entry.get()
        info_label.config(text=f"Registering user:\nName: {first_name} {last_name}\nEmail: {email}\nUsername: {username}")

    # Tạo button Register
    register_button = ttk.Button(register_frame, text="Register", command=register)
    register_button.pack(pady=10)
