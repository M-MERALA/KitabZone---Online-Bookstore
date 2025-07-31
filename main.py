import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import random
import time
import tkinter as tk
from bookstore_app import BookstoreApp
from database import Database
from auth_service import AuthService
from shopping_cart import ShoppingCart

if __name__ == "__main__":
    root = tk.Tk()
    app = BookstoreApp(root)
    root.mainloop()