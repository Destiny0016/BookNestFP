# Author: Destiny Harris
# Date: 04/19/2025
# Assignment: Making an online bookstore


import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # Make sure Pillow is installed: pip install pillow
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

    username_var = tk.StringVar()
    password_var = tk.StringVar()
# --- Global User and Book Data ---
users = {"demo": "password123"}
books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "price": 10.99, "desc": "A classic American novel.", "image": "The_Great_gatsby.jpg"},
    {"title": "1984", "author": "George Orwell", "price": 9.99, "desc": "A dystopian novel about surveillance.", "image": "1984,jpg"},
    {"title": "Harry Potter", "author": "J.K. Rowling", "price": 12.50, "desc": "A magical fantasy adventure.", "image": "Harry_Potter.jpg"},
    {"title": "Charlotte's Web", "author": "E.B. White", "price": 7.25, "desc": "A children’s classic about friendship.", "image": "char_web.jpg"},
]
cart = []

# --- Book Catalog Window ---
def open_book_catalog():
    catalog_win = tk.Toplevel()
    catalog_win.title("BookNest - Catalog")
    catalog_win.geometry("600x500")

    search_var = tk.StringVar()
    total_label_var = tk.StringVar(value="Total Cart Value: $0.00")

    def update_cart(book):
        cart.append(book)
        total = sum(item['price'] for item in cart)
        total_label_var.set(f"Total Cart Value: ${total:.2f}")
        messagebox.showinfo("Added", f"{book['title']} added to cart!")

    def search_books():
        keyword = search_var.get().lower()
        for widget in book_frame.winfo_children():
            widget.destroy()
        filtered = [b for b in books if keyword in b["title"].lower() or keyword in b["author"].lower()]
        display_books(filtered)

    def proceed_to_checkout():
        if not cart:
            messagebox.showwarning("Cart Empty", "Add some books before checking out.")
            return
        titles = "\n".join(f"{b['title']} - ${b['price']}" for b in cart)
        total = sum(b['price'] for b in cart)
        messagebox.showinfo("Checkout", f"Books in Cart:\n\n{titles}\n\nTotal: ${total:.2f}")

    ttk.Label(catalog_win, text="Book Catalog", font=("Helvetica", 18)).pack(pady=10)

    # Search
    search_frame = ttk.Frame(catalog_win)
    search_frame.pack(pady=5)
    ttk.Label(search_frame, text="Search for books:").pack(side="left")
    ttk.Entry(search_frame, textvariable=search_var).pack(side="left", padx=5)
    ttk.Button(search_frame, text="Search", command=search_books).pack(side="left")

    # Scrollable book list
    canvas = tk.Canvas(catalog_win)
    scrollbar = ttk.Scrollbar(catalog_win, orient="vertical", command=canvas.yview)
    book_frame = ttk.Frame(canvas)

    book_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=book_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def display_books(book_list):
        for book in book_list:
            frame = ttk.Frame(book_frame, padding=10, relief="raised")
            frame.pack(fill="x", pady=5)

            title = f"{book['title']} by {book['author']} - ${book['price']:.2f}"
            ttk.Label(frame, text=title, font=("Arial", 12, "bold")).pack(anchor="w")
            ttk.Label(frame, text=book['desc'], wraplength=500).pack(anchor="w")
            ttk.Button(frame, text="Add to Cart", command=lambda b=book: update_cart(b)).pack(anchor="e")

    display_books(books)

    # Cart and checkout
    bottom_frame = ttk.Frame(catalog_win, padding=10)
    bottom_frame.pack(fill="x", side="bottom")

    ttk.Label(bottom_frame, textvariable=total_label_var, font=("Arial", 12)).pack(side="left")
    ttk.Button(bottom_frame, text="Proceed to Checkout", command=proceed_to_checkout).pack(side="right")


# --- Login Window ---
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
            window.withdraw()  # Hide login window
            open_book_catalog()
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

    # --- Main Login Window ---
    global window
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
        logo.image = logo_img
        logo.pack()
    except:
        ttk.Label(frame, text="📚", font=("Arial", 40)).pack()

    # --- Labels and Entry Fields ---
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

# --- Start the App ---
main_login_window()