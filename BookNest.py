# Author: Destiny Harris
# Date: 04/19/2025
# Assignment: Making an online bookstore

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # Requires Pillow library

# Simulated user database
users = {"demo": "password123"}

def main_login_window():
    def validate_login():
        username = username_var.get()
        password = password_var.get()
        if not username or not password:
            messagebox.showwarning("Input Error", "Username and password are required.")
            return
        if len(password) < 4:
            messagebox.showwarning("Weak Password", "Password must be at least 4 characters.")
            return
        if username in users and users[username] == password:
            messagebox.showinfo("Success", f"Welcome, {username}!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def open_signup_window():
        signup = tk.Toplevel(window)
        signup.title("Sign Up")
        signup.geometry("300x250")

        new_user = tk.StringVar()
        new_pass = tk.StringVar()

        ttk.Label(signup, text="Create a New Account", font=("Helvetica", 12)).pack(pady=10)
        ttk.Label(signup, text="Username:").pack()
        ttk.Entry(signup, textvariable=new_user).pack()

        ttk.Label(signup, text="Password:").pack()
        ttk.Entry(signup, textvariable=new_pass, show="*").pack()

        def register():
            u = new_user.get()
            p = new_pass.get()
            if len(u) < 3 or len(p) < 4:
                messagebox.showwarning("Invalid", "Username must be 3+ chars, password 4+ chars.")
                return
            if u in users:
                messagebox.showwarning("Taken", "Username already exists.")
                return
            users[u] = p
            messagebox.showinfo("Success", "Account created!")
            signup.destroy()

        ttk.Button(signup, text="Sign Up", command=register).pack(pady=10)

    def exit_app():
        window.quit()

    # --- Main Window ---
    window = tk.Tk()
    window.title("BookNest - Login")
    window.geometry("500x400")
    window.resizable(False, False)

    frame = ttk.Frame(window, padding=20)
    frame.pack(expand=True)

    # --- Logo or Image ---
    try:
        img = Image.open("book_logo.png")
        img = img.resize((100, 100))
        logo_img = ImageTk.PhotoImage(img)
        logo = ttk.Label(frame, image=logo_img)
        logo.image = logo_img  # Keep reference
        logo.pack()
    except:
        ttk.Label(frame, text="📚", font=("Arial", 40)).pack()

    # --- Labels & Entry Fields ---
    ttk.Label(frame, text="Welcome to BookNest!", font=("Helvetica", 18)).pack(pady=10)
    ttk.Label(frame, text="Please Login or Sign Up to get started.").pack(pady=5)

    username_var = tk.StringVar()
    password_var = tk.StringVar()

    ttk.Label(frame, text="Username:").pack(anchor="w", pady=(10, 0))
    ttk.Entry(frame, textvariable=username_var).pack(fill='x')

    ttk.Label(frame, text="Password:").pack(anchor="w", pady=(10, 0))
    ttk.Entry(frame, textvariable=password_var, show="*").pack(fill='x')

    # --- Buttons ---
    button_frame = ttk.Frame(frame)
    button_frame.pack(pady=20)

    ttk.Button(button_frame, text="Login", command=validate_login).grid(row=0, column=0, padx=5)
    ttk.Button(button_frame, text="Sign Up", command=open_signup_window).grid(row=0, column=1, padx=5)
    ttk.Button(button_frame, text="Exit", command=exit_app).grid(row=0, column=2, padx=5)

    window.mainloop()

# --- Run the login window ---
main_login_window()