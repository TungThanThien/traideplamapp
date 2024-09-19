import tkinter as tk
from tkinter import ttk
from views.home import show_home_info
from views.login import show_login_info
from views.register import show_register_info

# Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Desktop Shop Application")
root.geometry("400x600")

# Tạo một frame cho header
header_frame = ttk.Frame(root)
header_frame.pack(side=tk.TOP, fill=tk.X)

# Tạo một label để hiển thị thông tin
info_label = tk.Label(root, text="", wraplength=300, justify="left")
info_label.pack(pady=20)

# Tạo các button Home, Login, Register
btn_home = ttk.Button(header_frame, text="Home", command=lambda: show_home_info(info_label))
btn_login = ttk.Button(header_frame, text="Login", command=lambda: show_login_info(info_label))
btn_register = ttk.Button(header_frame, text="Register", command=lambda: show_register_info(info_label))

# Sắp xếp các button sát nhau
btn_home.pack(side=tk.LEFT, padx=10, pady=5)
btn_login.pack(side=tk.LEFT, padx=10, pady=5)
btn_register.pack(side=tk.LEFT, padx=10, pady=5)

# Chạy vòng lặp chính
root.mainloop()
