import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import random
import time

# Database simulation
class Database:
    def __init__(self):
        self.users = {
            "Mohammed": {"password": "1234", "email": "mohammed@example.com", "address": "123 Main St", "is_admin": False},
            "Meraa": {"password": "1234", "email": "mariam@example.com", "address": "456 Oak Ave", "is_admin": False},
            "Meral": {"password": "1234", "email": "meral@example.com", "address": "789 Admin Blvd", "is_admin": True},
            "You": {"password": "123", "email": "you@example.com", "address": "456 Oak Ave", "is_admin": False},
            "Mohammed": {"password": "1234", "email": "mohammed@example.com", "address": "123 Main St", "is_admin": False},
            "Mariam": {"password": "1234", "email": "mariam@example.com", "address": "456 Oak Ave", "is_admin": False},
            "Meral": {"password": "1234", "email": "meral@example.com", "address": "789 Admin Blvd", "is_admin": True},
            "Mahmoud": {"password": "1234", "email": "mahmoud@example.com", "address": "123 Main St", "is_admin": False},
            "Mera": {"password": "1234", "email": "meral@example.com", "address": "789 Admin Blvd", "is_admin": False}
        }
        self.books = {
            1: {"title": "Python Programming", "author": "John Smith", "price": 49.99, "stock": 10, "description": "Learn Python from scratch", "category": "Programming"},
            2: {"title": "Web Development", "author": "Sarah Johnson", "price": 39.99, "stock": 5, "description": "Master modern web technologies", "category": "Web"},
            3: {"title": "Data Science", "author": "Mike Brown", "price": 59.99, "stock": 8, "description": "Data analysis and visualization", "category": "Data"},
            4: {"title": "Algorithms", "author": "Alice White", "price": 45.99, "stock": 3, "description": "Computer science fundamentals", "category": "CS"},
            5: {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "price": 12.99, "stock": 15, "description": "Classic American novel", "category": "Literature"},
            6: {"title": "To Kill a Mockingbird", "author": "Harper Lee", "price": 14.99, "stock": 12, "description": "Powerful story of racial injustice", "category": "Literature"},
            7: {"title": "1984", "author": "George Orwell", "price": 10.99, "stock": 20, "description": "Dystopian masterpiece", "category": "Fiction"},
            8: {"title": "The Hobbit", "author": "J.R.R. Tolkien", "price": 18.99, "stock": 7, "description": "Fantasy adventure", "category": "Fantasy"},
            9: {"title": "The Art of War", "author": "Sun Tzu", "price": 9.99, "stock": 25, "description": "Ancient military strategy", "category": "Philosophy"},
            10: {"title": "The Lean Startup", "author": "Eric Ries", "price": 22.99, "stock": 10, "description": "Modern business strategies", "category": "Business"},
            11: {"title": "Sapiens", "author": "Yuval Noah Harari", "price": 19.99, "stock": 18, "description": "Brief history of humankind", "category": "History"},
            12: {"title": "Atomic Habits", "author": "James Clear", "price": 16.99, "stock": 22, "description": "Build good habits and break bad ones", "category": "Self-Help"},
            13: {"title": "The Silent Patient", "author": "Alex Michaelides", "price": 14.99, "stock": 9, "description": "Psychological thriller", "category": "Mystery"},
            14: {"title": "Educated", "author": "Tara Westover", "price": 17.99, "stock": 11, "description": "Memoir of self-discovery", "category": "Biography"},
            15: {"title": "The Midnight Library", "author": "Matt Haig", "price": 15.99, "stock": 14, "description": "Exploration of life's possibilities", "category": "Fiction"},
            16: {"title": "Dune", "author": "Frank Herbert", "price": 13.99, "stock": 8, "description": "Epic science fiction novel", "category": "Sci-Fi"},
            17: {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "price": 11.99, "stock": 10, "description": "Coming-of-age story", "category": "Literature"},
            18: {"title": "Pride and Prejudice", "author": "Jane Austen", "price": 9.99, "stock": 15, "description": "Classic romantic novel", "category": "Romance"},
            19: {"title": "The Da Vinci Code", "author": "Dan Brown", "price": 12.99, "stock": 7, "description": "Mystery thriller", "category": "Mystery"},
            20: {"title": "The Alchemist", "author": "Paulo Coelho", "price": 10.99, "stock": 20, "description": "Philosophical novel", "category": "Philosophy"},
            21: {"title": "The Hunger Games", "author": "Suzanne Collins", "price": 14.99, "stock": 12, "description": "Dystopian adventure", "category": "Young Adult"},
            22: {"title": "The Girl with the Dragon Tattoo", "author": "Stieg Larsson", "price": 13.99, "stock": 9, "description": "Crime thriller", "category": "Mystery"},
            23: {"title": "The Shining", "author": "Stephen King", "price": 11.99, "stock": 11, "description": "Horror classic", "category": "Horror"},
            24: {"title": "Brave New World", "author": "Aldous Huxley", "price": 10.99, "stock": 8, "description": "Dystopian novel", "category": "Fiction"},
            25: {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "price": 24.99, "stock": 6, "description": "Epic fantasy trilogy", "category": "Fantasy"},
            26: {"title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams", "price": 12.99, "stock": 10, "description": "Science fiction comedy", "category": "Sci-Fi"},
            27: {"title": "The Book Thief", "author": "Markus Zusak", "price": 13.99, "stock": 9, "description": "Historical fiction", "category": "Historical"},
            28: {"title": "The Kite Runner", "author": "Khaled Hosseini", "price": 11.99, "stock": 12, "description": "Drama novel", "category": "Fiction"},
            29: {"title": "The Martian", "author": "Andy Weir", "price": 14.99, "stock": 8, "description": "Science fiction survival", "category": "Sci-Fi"},
            30: {"title": "Gone Girl", "author": "Gillian Flynn", "price": 12.99, "stock": 7, "description": "Psychological thriller", "category": "Mystery"},
            31: {"title": "The Road", "author": "Cormac McCarthy", "price": 10.99, "stock": 6, "description": "Post-apocalyptic novel", "category": "Fiction"},
            32: {"title": "The Handmaid's Tale", "author": "Margaret Atwood", "price": 11.99, "stock": 10, "description": "Dystopian fiction", "category": "Fiction"},
            33: {"title": "The Name of the Wind", "author": "Patrick Rothfuss", "price": 15.99, "stock": 5, "description": "Fantasy novel", "category": "Fantasy"},
            34: {"title": "The Goldfinch", "author": "Donna Tartt", "price": 16.99, "stock": 7, "description": "Literary fiction", "category": "Literature"},
            35: {"title": "The Night Circus", "author": "Erin Morgenstern", "price": 13.99, "stock": 9, "description": "Fantasy romance", "category": "Fantasy"}
        }
        self.orders = {}
        self.promos = {"DISCOUNT10": 0.9, "BOOKLOVER": 0.85, "READMORE": 0.8, "WELCOME20": 0.8, "SUMMER25": 0.75}

    def query_user(self, username):
        return self.users.get(username)
    
    def add_user(self, username, password, email, address):
        if username in self.users:
            return False
        self.users[username] = {"password": password, "email": email, "address": address, "is_admin": False}
        return True
    
    def get_books(self):
        return self.books
    
    def update_book(self, book_id, title, author, price, stock, description, category):
        if book_id in self.books:
            self.books[book_id] = {
                "title": title,
                "author": author,
                "price": price,
                "stock": stock,
                "description": description,
                "category": category
            }
            return True
        return False
    
    def add_book(self, title, author, price, stock, description, category):
        new_id = max(self.books.keys()) + 1 if self.books else 1
        self.books[new_id] = {
            "title": title,
            "author": author,
            "price": price,
            "stock": stock,
            "description": description,
            "category": category
        }
        return new_id
    
    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            return True
        return False
    
    def create_order(self, user, items, total, shipping, promo=None):
        order_id = random.randint(1000, 9999)
        self.orders[order_id] = {
            "user": user,
            "items": items,
            "total": total,
            "status": "Processing",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "shipping": shipping,
            "promo": promo
        }
        # Update stock
        for item in items:
            book_id = item["book_id"]
            qty = item["quantity"]
            self.books[book_id]["stock"] -= qty
        return order_id
    
    def get_user_orders(self, username):
        return {oid: order for oid, order in self.orders.items() if order["user"] == username}
    
    def cancel_order(self, order_id):
        if order_id in self.orders and self.orders[order_id]["status"] == "Processing":
            # Restore stock
            for item in self.orders[order_id]["items"]:
                book_id = item["book_id"]
                qty = item["quantity"]
                self.books[book_id]["stock"] += qty
            self.orders[order_id]["status"] = "Cancelled"
            return True
        return False
    
    def get_promo_discount(self, code):
        return self.promos.get(code, 1.0)
 

# Auth Service
class AuthService:
    def __init__(self, db):
        self.db = db
        self.current_user = None
    
    def authenticate(self, username, password):
        user = self.db.query_user(username)
        if user and user["password"] == password:
            self.current_user = username
            return True
        return False
    
    def signup(self, username, password, email, address):
        return self.db.add_user(username, password, email, address)
    
    def logout(self):
        self.current_user = None
    
    def is_admin(self):
        if self.current_user:
            return self.db.query_user(self.current_user)["is_admin"]
        return False


# Shopping Cart

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0.0
        self.discount = 1.0
        self.promo_code = ""
    
    def add_item(self, book_id, title, price, quantity):
        for item in self.items:
            if item["book_id"] == book_id:
                item["quantity"] += quantity
                self.calculate_total()
                return
        
        self.items.append({
            "book_id": book_id,
            "title": title,
            "price": price,
            "quantity": quantity
        })
        self.calculate_total()
    
    def remove_item(self, book_id):
        self.items = [item for item in self.items if item["book_id"] != book_id]
        self.calculate_total()
    
    def update_quantity(self, book_id, quantity):
        for item in self.items:
            if item["book_id"] == book_id:
                item["quantity"] = quantity
                break
        self.calculate_total()
    
    def calculate_total(self):
        self.total = sum(item["price"] * item["quantity"] for item in self.items) * self.discount
    
    def apply_discount(self, discount, promo_code):
        self.discount = discount
        self.promo_code = promo_code
        self.calculate_total()
    
    def clear(self):
        self.items = []
        self.total = 0.0
        self.discount = 1.0
        self.promo_code = ""
    
    def get_items(self):
        return self.items
    
    def get_total(self):
        return self.total
    
    def get_discounted_total(self):
        return self.total * self.discount

# Main Application
class BookstoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("KitabZone")
        self.root.geometry("1200x800")
        
        # Enhanced color scheme with battle of browns (dark to light)
        self.bg_color = "#F5F5DC"  # Creamy beige
        self.primary_color = "#5E3023"  # Dark brown
        self.secondary_color = "#895737"  # Medium brown
        self.accent_color = "#B88B4A"  # Light brown
        self.highlight_color = "#D8B65C"  # Golden brown
        self.text_color = "#333333"
        self.light_text = "#FFFFFF"
        self.button_color = "#895737"  # Medium brown
        self.button_hover = "#5E3023"  # Dark brown
        self.button_text = "#FFFFFF"
        self.success_color = "#4CAF50"  # Green
        self.error_color = "#F44336"   # Red
        self.info_color = "#2196F3"    # Blue
        
        # Configure styles
        self.configure_styles()
        
        self.root.configure(bg=self.bg_color)
        
        # Initialize services
        self.db = Database()
        self.auth = AuthService(self.db)
        self.cart = ShoppingCart()
        
        # Show splash screen first
        self.show_splash_screen()
    
    def configure_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure button styles
        style.configure('TButton', 
                      font=('Georgia', 12),
                      borderwidth=2,
                      relief='raised',
                      padding=6,
                      background=self.button_color,
                      foreground=self.button_text)
        
        style.map('TButton',
                 background=[('active', self.button_hover), ('pressed', self.button_hover)],
                 foreground=[('active', self.button_text), ('pressed', self.button_text)])
        
        # Configure entry styles
        style.configure('TEntry',
                      fieldbackground='white',
                      foreground=self.text_color,
                      padding=5)
        
        # Configure frame styles
        style.configure('TFrame',
                       background=self.bg_color)
        
        # Configure label styles
        style.configure('TLabel',
                       background=self.bg_color,
                       foreground=self.text_color,
                       font=('Georgia', 11))
        
        # Configure success button
        style.configure('Success.TButton',
                       background=self.success_color,
                       foreground=self.light_text)
        style.map('Success.TButton',
                 background=[('active', '#388E3C'), ('pressed', '#388E3C')])
        
        # Configure danger button
        style.configure('Danger.TButton',
                      background=self.error_color,
                      foreground=self.light_text)
        style.map('Danger.TButton',
                 background=[('active', '#D32F2F'), ('pressed', '#D32F2F')])
        
        # Configure info button
        style.configure('Info.TButton',
                      background=self.info_color,
                      foreground=self.light_text)
        style.map('Info.TButton',
                 background=[('active', '#1976D2'), ('pressed', '#1976D2')])
    
    def show_splash_screen(self):
        self.clear_window()
        
        splash_frame = tk.Frame(self.root, bg=self.primary_color)
        splash_frame.pack(fill=tk.BOTH, expand=True)
        
        # Decorative border
        border_frame = tk.Frame(splash_frame, bg=self.highlight_color, height=10)
        border_frame.pack(fill=tk.X, side=tk.TOP)
        
        # Main content frame
        content_frame = tk.Frame(splash_frame, bg=self.primary_color)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=50, pady=50)
        
        # Animated title
        title_label = tk.Label(
            content_frame, 
            text="", 
            font=("Georgia", 48, "bold"), 
            fg=self.highlight_color, 
            bg=self.primary_color
        )
        title_label.pack(pady=50)
        
        subtitle_label = tk.Label(
            content_frame, 
            text="", 
            font=("Georgia", 24), 
            fg=self.light_text, 
            bg=self.primary_color
        )
        subtitle_label.pack(pady=20)
        
        # Loading animation
        loading_label = tk.Label(
            content_frame, 
            text="", 
            font=("Georgia", 14), 
            fg=self.light_text, 
            bg=self.primary_color
        )
        loading_label.pack(pady=20)
        
        # Bottom decorative border
        border_frame2 = tk.Frame(splash_frame, bg=self.highlight_color, height=10)
        border_frame2.pack(fill=tk.X, side=tk.BOTTOM)
        
        # Animate the splash screen
        self.animate_splash(title_label, subtitle_label, loading_label)
    
    def animate_splash(self, title_label, subtitle_label, loading_label):
        title_text = "Welcome to KitabZone"
        subtitle_text = "Where Stories Come to Life"
        
        # Typewriter effect for title
        for i in range(len(title_text) + 1):
            title_label.config(text=title_text[:i])
            self.root.update()
            time.sleep(0.1)
        
        # Typewriter effect for subtitle
        for i in range(len(subtitle_text) + 1):
            subtitle_label.config(text=subtitle_text[:i])
            self.root.update()
            time.sleep(0.05)
        
        # Loading animation
        for i in range(5):
            loading_label.config(text="Loading" + "." * (i % 4))
            self.root.update()
            time.sleep(0.3)
        
        # Transition to auth page
        self.root.after(1000, self.show_auth_page)
    
    def show_auth_page(self):
        self.clear_window()
        
        # Main frame with gradient background effect
        auth_frame = tk.Frame(self.root, bg=self.primary_color)
        auth_frame.pack(fill=tk.BOTH, expand=True)
        
        # Decorative top border
        top_border = tk.Frame(auth_frame, bg=self.highlight_color, height=10)
        top_border.pack(fill=tk.X)
        
        # Content frame
        content_frame = tk.Frame(auth_frame, bg=self.primary_color)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        # App title
        title_frame = tk.Frame(content_frame, bg=self.primary_color)
        title_frame.pack(pady=(0, 30))
        
        tk.Label(
            title_frame, 
            text="KitabZone", 
            font=("Georgia", 36, "bold"), 
            fg=self.highlight_color, 
            bg=self.primary_color
        ).pack(side=tk.LEFT)
        
        # Auth container with shadow effect
        auth_container = tk.Frame(content_frame, bg=self.secondary_color, bd=0, 
                                highlightbackground=self.highlight_color, highlightthickness=2)
        auth_container.pack(fill=tk.BOTH, expand=True)
        
        # Notebook for login/signup tabs
        auth_notebook = ttk.Notebook(auth_container)
        auth_notebook.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Login tab
        login_tab = ttk.Frame(auth_notebook)
        auth_notebook.add(login_tab, text="Login")
        
        # Signup tab
        signup_tab = ttk.Frame(auth_notebook)
        auth_notebook.add(signup_tab, text="Sign Up")
        
        # Configure tab styles
        style = ttk.Style()
        style.configure('TNotebook', background=self.secondary_color)
        style.configure('TNotebook.Tab', 
                      background=self.secondary_color, 
                      foreground=self.light_text,
                      font=('Georgia', 12, 'bold'),
                      padding=[10, 5])
        style.map('TNotebook.Tab',
                 background=[('selected', self.primary_color)],
                 foreground=[('selected', self.highlight_color)])
        
        # Login form
        self.create_login_form(login_tab)
        
        # Signup form
        self.create_signup_form(signup_tab)
        
        # Decorative bottom border
        bottom_border = tk.Frame(auth_frame, bg=self.highlight_color, height=10)
        bottom_border.pack(fill=tk.X, side=tk.BOTTOM)
    
    def create_login_form(self, parent):
        form_frame = ttk.Frame(parent)
        form_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Username
        ttk.Label(form_frame, text="Username:", font=('Georgia', 14), 
                 background=self.secondary_color, foreground=self.light_text).pack(pady=(10, 5))
        self.login_username = ttk.Entry(form_frame, font=('Georgia', 14))
        self.login_username.pack(pady=5, ipadx=10, ipady=5, fill=tk.X)
        
        # Password
        ttk.Label(form_frame, text="Password:", font=('Georgia', 14), 
                 background=self.secondary_color, foreground=self.light_text).pack(pady=(10, 5))
        self.login_password = ttk.Entry(form_frame, show="*", font=('Georgia', 14))
        self.login_password.pack(pady=5, ipadx=10, ipady=5, fill=tk.X)
        
        # Login button
        login_btn = ttk.Button(form_frame, text="Login", command=self.handle_login)
        login_btn.pack(pady=20, ipadx=20, ipady=5)
        
        # Divider
        divider = ttk.Frame(form_frame, height=2, style='TFrame')
        divider.pack(fill=tk.X, pady=20)
        
        # Switch to signup
        switch_frame = ttk.Frame(form_frame)
        switch_frame.pack()
        
        ttk.Label(switch_frame, text="Don't have an account?", 
                 background=self.secondary_color, foreground=self.light_text).pack(side=tk.LEFT)
        
        switch_btn = ttk.Button(switch_frame, text="Sign Up", 
                              command=lambda: self.switch_auth_tab(1), style='TButton')
        switch_btn.pack(side=tk.LEFT, padx=5)
    
    def create_signup_form(self, parent):
        form_frame = ttk.Frame(parent)
        form_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Username
        ttk.Label(form_frame, text="Username:", font=('Georgia', 14), 
                 background=self.secondary_color, foreground=self.light_text).pack(pady=(10, 5))
        self.signup_username = ttk.Entry(form_frame, font=('Georgia', 14))
        self.signup_username.pack(pady=5, ipadx=10, ipady=5, fill=tk.X)
        
        # Password
        ttk.Label(form_frame, text="Password:", font=('Georgia', 14), 
                 background=self.secondary_color, foreground=self.light_text).pack(pady=(10, 5))
        self.signup_password = ttk.Entry(form_frame, show="*", font=('Georgia', 14))
        self.signup_password.pack(pady=5, ipadx=10, ipady=5, fill=tk.X)
        
        # Email
        ttk.Label(form_frame, text="Email:", font=('Georgia', 14), 
                 background=self.secondary_color, foreground=self.light_text).pack(pady=(10, 5))
        self.signup_email = ttk.Entry(form_frame, font=('Georgia', 14))
        self.signup_email.pack(pady=5, ipadx=10, ipady=5, fill=tk.X)
        
        # Address
        ttk.Label(form_frame, text="Address:", font=('Georgia', 14), 
                 background=self.secondary_color, foreground=self.light_text).pack(pady=(10, 5))
        self.signup_address = ttk.Entry(form_frame, font=('Georgia', 14))
        self.signup_address.pack(pady=5, ipadx=10, ipady=5, fill=tk.X)
        
        # Signup button
        signup_btn = ttk.Button(form_frame, text="Sign Up", command=self.handle_signup)
        signup_btn.pack(pady=10, ipadx=5, ipady=0)
        
        # Divider
        divider = ttk.Frame(form_frame, height=2, style='TFrame')
        divider.pack(fill=tk.X, pady=20)
        
        # Switch to login
        switch_frame = ttk.Frame(form_frame)
        switch_frame.pack()
        
        ttk.Label(switch_frame, text="Already have an account?", 
                 background=self.secondary_color, foreground=self.light_text).pack(side=tk.LEFT)
        
        switch_btn = ttk.Button(switch_frame, text="Login", 
                              command=lambda: self.switch_auth_tab(0), style='TButton')
        switch_btn.pack(side=tk.LEFT, padx=5)
    
    def switch_auth_tab(self, tab_index):
        for widget in self.root.winfo_children():
            if isinstance(widget, ttk.Notebook):
                widget.select(tab_index)
                break
    
    def handle_login(self):
        username = self.login_username.get()
        password = self.login_password.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password")
            return
        
        if self.auth.authenticate(username, password):
            if self.auth.is_admin():
                self.show_admin_dashboard()
            else:
                self.show_catalog()
        else:
            messagebox.showerror("Error", "Invalid username or password")
    
    def handle_signup(self):
        username = self.signup_username.get()
        password = self.signup_password.get()
        email = self.signup_email.get()
        address = self.signup_address.get()
        
        if not all([username, password, email, address]):
            messagebox.showerror("Error", "Please fill in all fields")
            return
        
        if self.auth.signup(username, password, email, address):
            messagebox.showinfo("Success", "Account created successfully! Please login.")
            self.login_username.delete(0, tk.END)
            self.login_password.delete(0, tk.END)
            self.login_username.insert(0, username)
            self.root.focus()
            self.switch_auth_tab(0)  # Switch to login tab
        else:
            messagebox.showerror("Error", "Username already exists")
    
    def show_catalog(self):
        self.clear_window()
        
        # Header frame
        header_frame = tk.Frame(self.root, bg=self.primary_color)
        header_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Welcome label with user's name
        welcome_label = tk.Label(
            header_frame, 
            text=f"Welcome, {self.auth.current_user}!", 
            font=("Georgia", 16, "bold"), 
            fg=self.highlight_color, 
            bg=self.primary_color
        )
        welcome_label.pack(side=tk.LEFT, padx=20)
        
        # Search frame
        search_frame = tk.Frame(header_frame, bg=self.primary_color)
        search_frame.pack(side=tk.LEFT, expand=True, padx=20)
        
        tk.Label(search_frame, text="Search:", font=("Georgia", 12), bg=self.primary_color, fg=self.light_text).pack(side=tk.LEFT)
        self.search_entry = ttk.Entry(search_frame, font=("Georgia", 12))
        self.search_entry.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        
        search_button = ttk.Button(
            search_frame, 
            text="🔍 Search", 
            command=self.search_books
        )
        search_button.pack(side=tk.LEFT, padx=5)
        
        # Action buttons
        button_frame = tk.Frame(header_frame, bg=self.primary_color)
        button_frame.pack(side=tk.RIGHT, padx=10)
        
        cart_button = ttk.Button(
            button_frame, 
            text=f"🛒 Cart ({len(self.cart.get_items())})", 
            command=self.show_cart
        )
        cart_button.pack(side=tk.LEFT, padx=5)
        
        history_button = ttk.Button(
            button_frame, 
            text="📜 History", 
            command=self.show_order_history
        )
        history_button.pack(side=tk.LEFT, padx=5)
        
        logout_button = ttk.Button(
            button_frame, 
            text="🚪 Logout", 
            command=self.logout,
            style='Danger.TButton'
        )
        logout_button.pack(side=tk.LEFT, padx=5)
        
        # Category filter
        categories = ["All"] + sorted(list(set(book["category"] for book in self.db.get_books().values())))
        category_frame = tk.Frame(self.root, bg=self.bg_color)
        category_frame.pack(fill=tk.X, padx=20, pady=5)
        
        tk.Label(category_frame, text="Filter by:", font=("Georgia", 12), bg=self.bg_color, fg=self.text_color).pack(side=tk.LEFT)
        
        self.category_var = tk.StringVar(value="All")
        for category in categories:
            rb = tk.Radiobutton(
                category_frame, 
                text=category, 
                variable=self.category_var, 
                value=category, 
                font=("Georgia", 10), 
                bg=self.bg_color,
                fg=self.text_color,
                activebackground=self.bg_color,
                selectcolor=self.primary_color,
                command=self.filter_books
            )
            rb.pack(side=tk.LEFT, padx=5)
        
        # Books frame with scrollable canvas
        books_frame = tk.Frame(self.root, bg=self.bg_color)
        books_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.books_canvas = tk.Canvas(books_frame, bg=self.bg_color, highlightthickness=0)
        self.books_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(books_frame, orient=tk.VERTICAL, command=self.books_canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.books_canvas.configure(yscrollcommand=scrollbar.set)
        self.books_canvas.bind('<Configure>', lambda e: self.books_canvas.configure(scrollregion=self.books_canvas.bbox("all")))
        
        self.books_container = tk.Frame(self.books_canvas, bg=self.bg_color)
        self.books_canvas.create_window((0, 0), window=self.books_container, anchor="nw")
        
        self.display_books(self.db.get_books())

    def display_books(self, books):
        # Clear previous books
        for widget in self.books_container.winfo_children():
            widget.destroy()

        # Display books in a grid
        row = 0
        col = 0
        for book_id, book in books.items():
            book_frame = tk.Frame(
                self.books_container,
                bg="white",
                bd=2,
                relief=tk.RAISED,
                highlightbackground=self.primary_color,
                highlightthickness=1
            )
            book_frame.grid(row=row, column=col, padx=15, pady=15, sticky="nsew")

            # Book cover placeholder with decorative border
            cover_frame = tk.Frame(book_frame, bg=self.secondary_color, width=120, height=180)
            cover_frame.pack_propagate(False)
            cover_frame.pack(pady=10)

            # Placeholder text in the cover
            title_words = book['title'].split()[:3]
            cover_text = "\n".join(title_words)
            tk.Label(
                cover_frame,
                text=cover_text,
                font=("Georgia", 10),
                bg=self.secondary_color,
                fg="white",
                wraplength=100
            ).pack(expand=True)

            # Book info
            info_frame = tk.Frame(book_frame, bg="white")
            info_frame.pack(fill=tk.X, padx=10, pady=5)

            tk.Label(
                info_frame,
                text=book['title'][:20] + ("..." if len(book['title']) > 20 else ""),
                font=("Georgia", 10, "bold"),
                bg="white",
                fg=self.text_color,
                wraplength=150
            ).pack()

            tk.Label(
                info_frame,
                text=f"by {book['author']}",
                font=("Georgia", 9),
                bg="white",
                fg=self.text_color
            ).pack()

            # Price with discount styling if applicable
            price_frame = tk.Frame(info_frame, bg="white")
            price_frame.pack()
            
            original_price = book['price']
            discounted_price = original_price
            
            # Apply discount if available (for demonstration)
            if hasattr(self, 'promo_discount') and self.promo_discount < 1.0:
                discounted_price = original_price * self.promo_discount
                tk.Label(
                    price_frame,
                    text=f"${original_price:.2f}",
                    font=("Georgia", 10),
                    bg="white",
                    fg="#999999",
                    relief="sunken"
                ).pack(side=tk.LEFT)
                tk.Label(
                    price_frame,
                    text=f" ${discounted_price:.2f}",
                    font=("Georgia", 12, "bold"),
                    bg="white",
                    fg=self.success_color
                ).pack(side=tk.LEFT)
            else:
                tk.Label(
                    price_frame,
                    text=f"${original_price:.2f}",
                    font=("Georgia", 12, "bold"),
                    bg="white",
                    fg=self.primary_color
                ).pack()

            tk.Label(
                info_frame,
                text=f"Stock: {book['stock']}",
                font=("Georgia", 8),
                bg="white",
                fg=self.text_color
            ).pack()

            # Action buttons
            action_frame = tk.Frame(book_frame, bg="white")
            action_frame.pack(fill=tk.X, pady=5)

            # Add to cart button
            add_button = ttk.Button(
                action_frame,
                text="Add to Cart",
                command=lambda bid=book_id, t=book['title'], p=discounted_price: self.add_to_cart(bid, t, p, 1)
            )
            add_button.pack(side=tk.LEFT, padx=2, ipadx=5, ipady=2)

            # View details button
            view_button = ttk.Button(
                action_frame,
                text="Details",
                style='Info.TButton',
                command=lambda bid=book_id: self.show_book_details(bid)
            )
            view_button.pack(side=tk.LEFT, padx=2, ipadx=5, ipady=2)

            # Grid layout management
            col += 1
            if col > 3:  # 4 books per row
                col = 0
                row += 1

        # Configure grid weights for responsive layout
        for i in range(4):
            self.books_container.grid_columnconfigure(i, weight=1)

    def filter_books(self):
        category = self.category_var.get()
        if category == "All":
            self.display_books(self.db.get_books())
        else:
            filtered_books = {
                bid: book
                for bid, book in self.db.get_books().items()
                if book["category"] == category
            }
            self.display_books(filtered_books)

    def show_book_details(self, book_id):
        book = self.db.get_books()[book_id]

        details_window = tk.Toplevel(self.root)
        details_window.title(book['title'])
        details_window.geometry("600x500")
        details_window.configure(bg=self.bg_color)

        # Header with book title
        header_frame = tk.Frame(details_window, bg=self.primary_color)
        header_frame.pack(fill=tk.X, pady=10)

        tk.Label(
            header_frame,
            text=book['title'],
            font=("Georgia", 18, "bold"),
            fg=self.highlight_color,
            bg=self.primary_color
        ).pack(pady=10)

        # Book info frame
        info_frame = tk.Frame(details_window, bg=self.bg_color)
        info_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Left side - book cover placeholder
        cover_frame = tk.Frame(info_frame, bg=self.secondary_color, width=200, height=300)
        cover_frame.pack_propagate(False)
        cover_frame.pack(side=tk.LEFT, padx=10)

        # Placeholder text in the cover
        title_words = book['title'].split()[:4]
        cover_text = "\n".join(title_words)
        tk.Label(
            cover_frame,
            text=cover_text,
            font=("Georgia", 12),
            bg=self.secondary_color,
            fg="white",
            wraplength=180
        ).pack(expand=True)

        # Right side - book details
        details_frame = tk.Frame(info_frame, bg=self.bg_color)
        details_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

        tk.Label(
            details_frame,
            text=f"by {book['author']}",
            font=("Georgia", 14),
            bg=self.bg_color,
            fg=self.text_color
        ).pack(anchor="w", pady=5)

        tk.Label(
            details_frame,
            text=f"Category: {book['category']}",
            font=("Georgia", 12),
            bg=self.bg_color,
            fg=self.text_color
        ).pack(anchor="w", pady=2)

        # Price display with discount if available
        price_frame = tk.Frame(details_frame, bg=self.bg_color)
        price_frame.pack(anchor="w", pady=5)
        
        original_price = book['price']
        discounted_price = original_price
        
        if hasattr(self, 'promo_discount') and self.promo_discount < 1.0:
            discounted_price = original_price * self.promo_discount
            tk.Label(
                price_frame,
                text=f"Price: ${original_price:.2f}",
                font=("Georgia", 12),
                bg=self.bg_color,
                fg="#999999",
                relief="sunken"
            ).pack(side=tk.LEFT)
            tk.Label(
                price_frame,
                text=f" ${discounted_price:.2f}",
                font=("Georgia", 14, "bold"),
                bg=self.bg_color,
                fg=self.success_color
            ).pack(side=tk.LEFT)
            tk.Label(
                price_frame,
                text=f" (Save {int((1-self.promo_discount)*100)}%)",
                font=("Georgia", 12),
                bg=self.bg_color,
                fg=self.success_color
            ).pack(side=tk.LEFT)
        else:
            tk.Label(
                price_frame,
                text=f"Price: ${original_price:.2f}",
                font=("Georgia", 14, "bold"),
                bg=self.bg_color,
                fg=self.primary_color
            ).pack()

        tk.Label(
            details_frame,
            text=f"Stock: {book['stock']}",
            font=("Georgia", 12),
            bg=self.bg_color,
            fg=self.text_color
        ).pack(anchor="w", pady=2)

        tk.Label(
            details_frame,
            text="Description:",
            font=("Georgia", 12, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        ).pack(anchor="w", pady=5)

        description_text = tk.Text(
            details_frame,
            font=("Georgia", 11),
            wrap=tk.WORD,
            height=8,
            width=40,
            bg="white",
            fg=self.text_color,
            padx=10,
            pady=10,
            relief=tk.FLAT
        )
        description_text.insert(tk.END, book['description'])
        description_text.config(state=tk.DISABLED)
        description_text.pack(fill=tk.BOTH, expand=True, pady=5)

        # Add to cart controls
        cart_frame = tk.Frame(details_window, bg=self.bg_color)
        cart_frame.pack(fill=tk.X, padx=20, pady=10)

        tk.Label(cart_frame, text="Quantity:", font=("Georgia", 12), bg=self.bg_color, fg=self.text_color).pack(side=tk.LEFT)
        qty_spinbox = tk.Spinbox(cart_frame, from_=1, to=10, width=3, font=("Georgia", 12))
        qty_spinbox.pack(side=tk.LEFT, padx=5)

        add_button = ttk.Button(
            cart_frame,
            text="Add to Cart",
            command=lambda: self.add_to_cart(book_id, book['title'], discounted_price, int(qty_spinbox.get()))
        )
        add_button.pack(side=tk.LEFT, padx=10, ipadx=10, ipady=3)

        close_button = ttk.Button(
            details_window,
            text="Close",
            style='Danger.TButton',
            command=details_window.destroy
        )
        close_button.pack(pady=10, ipadx=20, ipady=3)

    def add_to_cart(self, book_id, title, price, quantity):
        book = self.db.get_books()[book_id]
        if quantity > book['stock']:
            messagebox.showerror("Error", f"Only {book['stock']} available in stock")
            return

        self.cart.add_item(book_id, title, price, quantity)
        messagebox.showinfo("Success", f"Added {quantity} x {title} to cart")
        self.update_cart_count()

    def update_cart_count(self):
        # Find the cart button in the header and update its text
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame) and widget.winfo_children()[0].cget("text").startswith("Welcome"):
                for child in widget.winfo_children():
                    if isinstance(child, tk.Frame):
                        for button in child.winfo_children():
                            if "Cart" in button.cget("text"):
                                button.config(text=f"🛒 Cart ({len(self.cart.get_items())})")
                                break
                break

    # ... [Previous code remains the same until the show_cart method] ...

    def show_cart(self):
        self.clear_window()

        # Header frame
        header_frame = tk.Frame(self.root, bg=self.primary_color)
        header_frame.pack(fill=tk.X, padx=5, pady=5)

        welcome_label = tk.Label(
            header_frame,
            text=f"Your Shopping Cart",
            font=("Georgia", 16, "bold"),
            fg=self.highlight_color,
            bg=self.primary_color
        )
        welcome_label.pack(side=tk.LEFT, padx=20)

        back_button = ttk.Button(
            header_frame,
            text="⬅ Back to Catalog",
            command=self.show_catalog
        )
        back_button.pack(side=tk.RIGHT, padx=10, ipadx=10, ipady=3)

        # Cart items frame
        cart_frame = tk.Frame(self.root, bg=self.bg_color)
        cart_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        if not self.cart.get_items():
            empty_frame = tk.Frame(cart_frame, bg=self.bg_color)
            empty_frame.pack(expand=True, pady=50)

            tk.Label(
                empty_frame,
                text="🛒 Your cart is empty",
                font=("Georgia", 24),
                bg=self.bg_color,
                fg=self.text_color
            ).pack(pady=20)

            ttk.Button(
                empty_frame,
                text="Browse Books",
                command=self.show_catalog
            ).pack(pady=20, ipadx=20, ipady=5)

            return

        # Create a canvas for scrollable cart items
        cart_canvas = tk.Canvas(cart_frame, bg=self.bg_color, highlightthickness=0)
        scrollbar = ttk.Scrollbar(cart_frame, orient=tk.VERTICAL, command=cart_canvas.yview)
        
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        cart_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        cart_canvas.configure(yscrollcommand=scrollbar.set)
        
        # Create a frame inside the canvas to hold the items
        items_container = tk.Frame(cart_canvas, bg=self.bg_color)
        cart_canvas.create_window((0, 0), window=items_container, anchor="nw")
        
        # Function to update the scroll region
        def on_frame_configure(event):
            cart_canvas.configure(scrollregion=cart_canvas.bbox("all"))
        
        items_container.bind("<Configure>", on_frame_configure)

        # Display cart items
        for item in self.cart.get_items():
            item_frame = tk.Frame(
                items_container,
                bg="white",
                bd=2,
                relief=tk.RAISED,
                highlightbackground=self.primary_color,
                highlightthickness=1
            )
            item_frame.pack(fill=tk.X, padx=10, pady=5, ipadx=10, ipady=10)

            # Item info
            tk.Label(
                item_frame,
                text=item['title'],
                font=("Georgia", 12, "bold"),
                bg="white",
                fg=self.text_color
            ).grid(row=0, column=0, sticky="w", padx=10, pady=2)

            tk.Label(
                item_frame,
                text=f"${item['price']:.2f} x {item['quantity']} = ${item['price'] * item['quantity']:.2f}",
                font=("Georgia", 12),
                bg="white",
                fg=self.text_color
            ).grid(row=1, column=0, sticky="w", padx=10, pady=2)

            # Update/remove controls
            controls_frame = tk.Frame(item_frame, bg="white")
            controls_frame.grid(row=2, column=0, sticky="w", padx=10, pady=5)

            tk.Label(controls_frame, text="Qty:", font=("Georgia", 10), bg="white", fg=self.text_color).pack(side=tk.LEFT)
            qty_spinbox = tk.Spinbox(
                controls_frame,
                from_=1,
                to=10,
                width=3,
                font=("Georgia", 10)
            )
            qty_spinbox.delete(0, tk.END)
            qty_spinbox.insert(0, item['quantity'])
            qty_spinbox.pack(side=tk.LEFT, padx=5)

            update_button = ttk.Button(
                controls_frame,
                text="Update",
                command=lambda bid=item['book_id'], sb=qty_spinbox: self.update_cart_item_qty(bid, int(sb.get()))
            )
            update_button.pack(side=tk.LEFT, padx=5, ipadx=5, ipady=1)

            remove_button = ttk.Button(
                controls_frame,
                text="Remove",
                style='Danger.TButton',
                command=lambda bid=item['book_id']: self.remove_cart_item(bid)
            )
            remove_button.pack(side=tk.LEFT, padx=5, ipadx=5, ipady=1)

        # Total and checkout button
        total_frame = tk.Frame(self.root, bg=self.bg_color)  # Changed from items_container to self.root
        total_frame.pack(fill=tk.X, pady=20)

        # Apply promo code section
        promo_frame = tk.Frame(total_frame, bg=self.bg_color)
        promo_frame.pack(fill=tk.X, pady=5)

        tk.Label(
            promo_frame,
            text="Promo Code:",
            font=("Georgia", 12),
            bg=self.bg_color,
            fg=self.text_color
        ).pack(side=tk.LEFT)

        self.promo_entry = ttk.Entry(promo_frame, font=("Georgia", 12))
        self.promo_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        apply_promo_button = ttk.Button(
            promo_frame,
            text="Apply",
            style='Info.TButton',
            command=self.apply_promo
        )
        apply_promo_button.pack(side=tk.LEFT, padx=5, ipadx=10, ipady=2)

        # Display discount if applied
        if hasattr(self, 'promo_discount') and self.promo_discount < 1.0:
            discount_frame = tk.Frame(total_frame, bg=self.bg_color)
            discount_frame.pack(fill=tk.X, pady=5)

            tk.Label(
                discount_frame,
                text=f"Discount Applied ({self.promo_code}): -{int((1-self.promo_discount)*100)}%",
                font=("Georgia", 12),
                bg=self.bg_color,
                fg=self.success_color
            ).pack(side=tk.LEFT)

            remove_discount_button = ttk.Button(
                discount_frame,
                text="Remove",
                style='Danger.TButton',
                command=self.remove_discount
            )
            remove_discount_button.pack(side=tk.RIGHT, padx=5, ipadx=5, ipady=1)

        # Display totals
        subtotal = sum(item['price'] * item['quantity'] for item in self.cart.get_items())
        discount_amount = subtotal * (1 - self.cart.discount) if hasattr(self.cart, 'discount') and self.cart.discount < 1.0 else 0
        total = subtotal - discount_amount

        tk.Label(
            total_frame,
            text=f"Subtotal: ${subtotal:.2f}",
            font=("Georgia", 12),
            bg=self.bg_color,
            fg=self.text_color
        ).pack(anchor="w", padx=10, pady=2)

        if discount_amount > 0:
            tk.Label(
                total_frame,
                text=f"Discount: -${discount_amount:.2f}",
                font=("Georgia", 12),
                bg=self.bg_color,
                fg=self.success_color
            ).pack(anchor="w", padx=10, pady=2)

        tk.Label(
            total_frame,
            text=f"Total: ${total:.2f}",
            font=("Georgia", 14, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        ).pack(anchor="w", padx=10, pady=5)

        # Checkout button
        checkout_button = ttk.Button(
            total_frame,
            text="Proceed to Checkout",
            style='Success.TButton',
            command=self.show_checkout
        )
        checkout_button.pack(pady=10, ipadx=20, ipady=5)

# ... [Rest of the code remains the same] ...

    def update_cart_item_qty(self, book_id, new_qty):
        book = self.db.get_books()[book_id]
        if new_qty > book['stock']:
            messagebox.showerror("Error", f"Only {book['stock']} available in stock")
            return

        self.cart.update_quantity(book_id, new_qty)
        self.show_cart()
        self.update_cart_count()

    def remove_cart_item(self, book_id):
        self.cart.remove_item(book_id)
        self.show_cart()
        self.update_cart_count()

    def apply_promo(self):
        promo_code = self.promo_entry.get().strip().upper()
        discount = self.db.get_promo_discount(promo_code)

        if discount < 1.0:
            self.promo_discount = discount
            self.promo_code = promo_code
            self.cart.apply_discount(discount, promo_code)
            messagebox.showinfo("Success", f"Promo code applied! {int((1 - discount) * 100)}% discount")
            self.show_cart()  # Refresh to show updated total
        else:
            messagebox.showerror("Error", "Invalid promo code")

    def remove_discount(self):
        if hasattr(self, 'promo_discount'):
            del self.promo_discount
            del self.promo_code
            self.cart.apply_discount(1.0, "")
            self.show_cart()

    def show_checkout(self):
        self.clear_window()

        # Header frame
        header_frame = tk.Frame(self.root, bg=self.primary_color)
        header_frame.pack(fill=tk.X, padx=5, pady=2)

        welcome_label = tk.Label(
            header_frame,
            text=f"Checkout",
            font=("Georgia", 16, "bold"),
            fg=self.highlight_color,
            bg=self.primary_color
        )
        welcome_label.pack(side=tk.LEFT, padx=20)

        back_button = ttk.Button(
            header_frame,
            text="⬅ Back to Cart",
            command=self.show_cart
        )
        back_button.pack(side=tk.RIGHT, padx=10, ipadx=10, ipady=3)

        # Checkout form frame
        checkout_frame = tk.Frame(self.root, bg=self.bg_color)
        checkout_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Shipping address
        address_frame = tk.LabelFrame(
            checkout_frame,
            text="Shipping Address",
            font=("Georgia", 12, "bold"),
            bg=self.bg_color,
            fg=self.text_color,
            relief=tk.RAISED,
            bd=2
        )
        address_frame.pack(fill=tk.X, padx=.1, pady=0.1, ipadx=0.1, ipady=0.1)

        user = self.db.query_user(self.auth.current_user)
        tk.Label(
            address_frame,
            text=user['address'],
            font=("Georgia", 12),
            bg=self.bg_color,
            fg=self.text_color
        ).pack(pady=5)

        # Shipping options - now with more details
        shipping_frame = tk.LabelFrame(
            checkout_frame,
            text="Shipping Method",
            font=("Georgia", 12, "bold"),
            bg=self.bg_color,
            fg=self.text_color,
            relief=tk.RAISED,
            bd=2
        )
        shipping_frame.pack(fill=tk.X, padx=0.1, pady=0.1, ipadx=.1, ipady=.1)

        self.shipping_var = tk.StringVar(value="standard")
        shipping_options = [
            ("Standard Shipping (3-5 business days) - Free", "standard"),
            ("Express Shipping (1-2 business days) - $5.99", "express"),
            ("Overnight Shipping (Next business day) - $12.99", "overnight"),
            ("In-Store Pickup (Available immediately) - Free", "pickup")
        ]

        for text, mode in shipping_options:
            tk.Radiobutton(
                shipping_frame,
                text=text,
                variable=self.shipping_var,
                value=mode,
                font=("Georgia", 11),
                bg=self.bg_color,
                fg=self.text_color,
                activebackground=self.bg_color,
                selectcolor=self.primary_color
            ).pack(anchor="w", padx=10, pady=2)

        # Payment method - expanded with more details
        payment_frame = tk.LabelFrame(
            checkout_frame,
            text="Payment Method",
            font=("Georgia", 12, "bold"),
            bg=self.bg_color,
            fg=self.text_color,
            relief=tk.RAISED,
            bd=2
        )
        payment_frame.pack(fill=tk.X, padx=.00000, pady=.00000, ipadx=.00000000000000000000000000, ipady=.000000000000000000000)

        self.payment_var = tk.StringVar(value="credit")
        
        # Credit Card Frame
        credit_frame = tk.Frame(payment_frame, bg=self.bg_color)
        credit_frame.pack(fill=tk.X, pady=1)
        
        tk.Radiobutton(
            credit_frame,
            text="Credit/Debit Card",
            variable=self.payment_var,
            value="credit",
            font=("Georgia", 11),
            bg=self.bg_color,
            fg=self.text_color,
            activebackground=self.bg_color,
            selectcolor=self.primary_color,
            command=self.toggle_payment_fields
        ).pack(anchor="w", padx=10, pady=2)
        
        # Credit card fields (hidden by default)
        self.credit_card_frame = tk.Frame(payment_frame, bg=self.bg_color)
        
        tk.Label(self.credit_card_frame, text="Card Number:", font=("Georgia", 10), bg=self.bg_color).pack(anchor="w", padx=10)
        self.card_number_entry = ttk.Entry(self.credit_card_frame, font=("Georgia", 10))
        self.card_number_entry.pack(fill=tk.X, padx=10, pady=2)
        

        
        # PayPal Frame
        paypal_frame = tk.Frame(payment_frame, bg=self.bg_color)
        paypal_frame.pack(fill=tk.X, pady=5)
        
        tk.Radiobutton(
            paypal_frame,
            text="PayPal",
            variable=self.payment_var,
            value="paypal",
            font=("Georgia", 11),
            bg=self.bg_color,
            fg=self.text_color,
            activebackground=self.bg_color,
            selectcolor=self.primary_color,
            command=self.toggle_payment_fields
        ).pack(anchor="w", padx=10, pady=2)
        
        # PayPal info (hidden by default)
        self.paypal_frame = tk.Frame(payment_frame, bg=self.bg_color)
        tk.Label(self.paypal_frame, 
                text="You'll be redirected to PayPal to complete your payment", 
                font=("Georgia", 10), 
                bg=self.bg_color).pack(anchor="w", padx=30, pady=5)
        
        # Cash Frame
        cash_frame = tk.Frame(payment_frame, bg=self.bg_color)
        cash_frame.pack(fill=tk.X, pady=1)
        
        tk.Radiobutton(
            cash_frame,
            text="Cash on Delivery",
            variable=self.payment_var,
            value="cash",
            font=("Georgia", 11),
            bg=self.bg_color,
            fg=self.text_color,
            activebackground=self.bg_color,
            selectcolor=self.primary_color,
            command=self.toggle_payment_fields
        ).pack(anchor="w", padx=10, pady=2)
        
        # Cash info (hidden by default)
        self.cash_frame = tk.Frame(payment_frame, bg=self.bg_color)
        tk.Label(self.cash_frame, 
                text="Pay with cash when your order is delivered", 
                font=("Georgia", 10), 
                bg=self.bg_color).pack(anchor="w", padx=30, pady=5)
        
        # Initialize payment fields
        self.toggle_payment_fields()

        # Order summary
        summary_frame = tk.LabelFrame(
            checkout_frame,
            text="Order Summary",
            font=("Georgia", 12, "bold"),
            bg=self.bg_color,
            fg=self.text_color,
            relief=tk.RAISED,
            bd=2
        )
        summary_frame.pack(fill=tk.X, padx=0.1, pady=0.1, ipadx=0.0, ipady=0.0)

        # Calculate shipping cost
        shipping_cost = 0.0
        if self.shipping_var.get() == "express":
            shipping_cost = 5.99
        elif self.shipping_var.get() == "overnight":
            shipping_cost = 12.99

        # Calculate total with shipping
        subtotal = sum(item['price'] * item['quantity'] for item in self.cart.get_items())
        total = subtotal + shipping_cost

        # Apply promo discount if any
        if hasattr(self.cart, 'discount') and self.cart.discount < 1.0:
            total *= self.cart.discount
            discount_text = f"Discount ({self.cart.promo_code}): -${subtotal * (1 - self.cart.discount):.2f}"
        else:
            discount_text = "Discount: $0.00"

        # Display order summary
        tk.Label(
            summary_frame,
            text=f"Subtotal: ${subtotal:.2f}",
            font=("Georgia", 11),
            bg=self.bg_color,
            fg=self.text_color
        ).pack(anchor="w", padx=2, pady=2)

        tk.Label(
            summary_frame,
            text=f"Shipping: ${shipping_cost:.2f}",
            font=("Georgia", 11),
            bg=self.bg_color,
            fg=self.text_color
        ).pack(anchor="w", padx=2, pady=2)

        tk.Label(
            summary_frame,
            text=discount_text,
            font=("Georgia", 11),
            bg=self.bg_color,
            fg=self.success_color if hasattr(self.cart, 'discount') and self.cart.discount < 1.0 else self.text_color
        ).pack(anchor="w", padx=2, pady=2)

        tk.Label(
            summary_frame,
            text=f"Total: ${total:.2f}",
            font=("Georgia", 12, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        ).pack(anchor="w", padx=2, pady=2)

        # Confirm order button
        confirm_button = ttk.Button(
            checkout_frame,
            text="Confirm Order",
            style='Success.TButton',
            command=lambda: self.process_order(total, shipping_cost)
        )
        confirm_button.pack(pady=2, ipadx=2, ipady=2)

    def toggle_payment_fields(self):
        # Hide all payment frames first
        self.credit_card_frame.pack_forget()
        self.paypal_frame.pack_forget()
        self.cash_frame.pack_forget()
        
        # Show the selected payment method frame
        if self.payment_var.get() == "credit":
            self.credit_card_frame.pack(fill=tk.X, padx=10, pady=5)
        elif self.payment_var.get() == "paypal":
            self.paypal_frame.pack(fill=tk.X, padx=10, pady=5)
        elif self.payment_var.get() == "cash":
            self.cash_frame.pack(fill=tk.X, padx=10, pady=5)

    def process_order(self, total, shipping_cost):
        payment_method = self.payment_var.get()
        shipping_method = self.shipping_var.get()

        # Validate payment details based on method
        if payment_method == "credit":
            card_number = self.card_number_entry.get().strip()

            
            if not all([card_number]):
                messagebox.showerror("Error", "Please fill in all credit card details")
                return
                
            # Simple validation for demo purposes
            if len(card_number.replace(" ", "")) != 16 or not card_number.replace(" ", "").isdigit():
                messagebox.showerror("Error", "Please enter a valid 16-digit card number")
                return
                
            # if len(cvv) != 3 or not cvv.isdigit():
            #     messagebox.showerror("Error", "Please enter a valid 3-digit CVV")
            #     return

        # Get promo code if applied
        promo_code = getattr(self.cart, 'promo_code', None)

        # Create order in database
        order_id = self.db.create_order(
            self.auth.current_user,
            self.cart.get_items(),
            total,
            shipping_method,
            promo_code
        )

        # Clear cart
        self.cart.clear()
        self.update_cart_count()

        # Show order confirmation with payment method
        self.show_order_confirmation(order_id, total, payment_method)

    def show_order_confirmation(self, order_id, total, payment_method):
        self.clear_window()

        # Header frame
        header_frame = tk.Frame(self.root, bg=self.primary_color)
        header_frame.pack(fill=tk.X, padx=10, pady=10)

        welcome_label = tk.Label(
            header_frame,
            text=f"Order Confirmation",
            font=("Georgia", 16, "bold"),
            fg=self.highlight_color,
            bg=self.primary_color
        )
        welcome_label.pack(side=tk.LEFT, padx=20)

        home_button = ttk.Button(
            header_frame,
            text="🏠 Back to Catalog",
            command=self.show_catalog
        )
        home_button.pack(side=tk.RIGHT, padx=10, ipadx=10, ipady=3)

        # Confirmation frame
        confirm_frame = tk.Frame(self.root, bg=self.bg_color)
        confirm_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Confirmation icon and message
        icon_frame = tk.Frame(confirm_frame, bg=self.bg_color)
        icon_frame.pack(pady=20)

        tk.Label(
            icon_frame,
            text="✓",
            font=("Georgia", 48),
            bg=self.bg_color,
            fg=self.success_color
        ).pack()

        tk.Label(
            confirm_frame,
            text="Thank you for your order!",
            font=("Georgia", 20, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        ).pack(pady=10)

        # Order details
        details_frame = tk.Frame(confirm_frame, bg=self.bg_color)
        details_frame.pack(pady=20)

        tk.Label(
            details_frame,
            text=f"Order ID: #{order_id}",
            font=("Georgia", 16),
            bg=self.bg_color,
            fg=self.text_color
        ).grid(row=0, column=0, sticky="w", pady=5)

        tk.Label(
            details_frame,
            text=f"Total: ${total:.2f}",
            font=("Georgia", 16),
            bg=self.bg_color,
            fg=self.text_color
        ).grid(row=1, column=0, sticky="w", pady=5)

        tk.Label(
            details_frame,
            text=f"Payment Method: {self.get_payment_method_name(payment_method)}",
            font=("Georgia", 16),
            bg=self.bg_color,
            fg=self.text_color
        ).grid(row=2, column=0, sticky="w", pady=5)

        tk.Label(
            confirm_frame,
            text="You can track your order in the Order History section.",
            font=("Georgia", 14),
            bg=self.bg_color,
            fg=self.text_color
        ).pack(pady=20)

        # Order history button
        history_button = ttk.Button(
            confirm_frame,
            text="📜 View Order History",
            command=self.show_order_history
        )
        history_button.pack(pady=20, ipadx=20, ipady=5)

    def get_payment_method_name(self, method_code):
        methods = {
            "credit": "Credit/Debit Card",
            "paypal": "PayPal",
            "cash": "Cash on Delivery"
        }
        return methods.get(method_code, "Unknown")

    def show_order_history(self):
        self.clear_window()

        # Header frame
        header_frame = tk.Frame(self.root, bg=self.primary_color)
        header_frame.pack(fill=tk.X, padx=10, pady=10)

        welcome_label = tk.Label(
            header_frame,
            text="Order History",
            font=("Georgia", 16, "bold"),
            fg=self.highlight_color,
            bg=self.primary_color
        )
        welcome_label.pack(side=tk.LEFT, padx=20)

        home_button = ttk.Button(
            header_frame,
            text="🏠 Back to Catalog",
            command=self.show_catalog
        )
        home_button.pack(side=tk.RIGHT, padx=10, ipadx=10, ipady=3)

        # Orders frame
        orders_frame = tk.Frame(self.root, bg=self.bg_color)
        orders_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        orders = self.db.get_user_orders(self.auth.current_user)

        if not orders:
            empty_frame = tk.Frame(orders_frame, bg=self.bg_color)
            empty_frame.pack(expand=True, pady=50)

            tk.Label(
                empty_frame,
                text="📜 You haven't placed any orders yet.",
                font=("Georgia", 16),
                bg=self.bg_color,
                fg=self.text_color
            ).pack(pady=20)

            ttk.Button(
                empty_frame,
                text="Browse Books",
                command=self.show_catalog
            ).pack(pady=20, ipadx=20, ipady=5)

            return

        # Create a canvas for scrollable orders
        orders_canvas = tk.Canvas(orders_frame, bg=self.bg_color, highlightthickness=0)
        orders_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(orders_frame, orient=tk.VERTICAL, command=orders_canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        orders_canvas.configure(yscrollcommand=scrollbar.set)
        orders_canvas.bind('<Configure>', lambda e: orders_canvas.configure(scrollregion=orders_canvas.bbox("all")))

        orders_container = tk.Frame(orders_canvas, bg=self.bg_color)
        orders_canvas.create_window((0, 0), window=orders_container, anchor="nw")

        # Display orders
        for order_id, order in sorted(orders.items(), key=lambda x: x[1]['date'], reverse=True):
            order_frame = tk.Frame(
                orders_container,
                bg="white",
                bd=2,
                relief=tk.RAISED,
                highlightbackground=self.primary_color,
                highlightthickness=1
            )
            order_frame.pack(fill=tk.X, padx=10, pady=10, ipadx=10, ipady=10)

            # Order header with date and status
            header_frame = tk.Frame(order_frame, bg="white")
            header_frame.pack(fill=tk.X, pady=5)

            tk.Label(
                header_frame,
                text=f"Order #{order_id}",
                font=("Georgia", 14, "bold"),
                bg="white",
                fg=self.text_color
            ).pack(side=tk.LEFT, padx=10)

            tk.Label(
                header_frame,
                text=f"Date: {order['date']}",
                font=("Georgia", 12),
                bg="white",
                fg=self.text_color
            ).pack(side=tk.LEFT, padx=20)

            status_color = self.success_color if order['status'] == "Processing" else self.error_color
            status_label = tk.Label(
                header_frame,
                text=f"Status: {order['status']}",
                font=("Georgia", 12),
                bg="white",
                fg=status_color
            )
            status_label.pack(side=tk.LEFT, padx=20)

            # Order items
            items_frame = tk.Frame(order_frame, bg="white")
            items_frame.pack(fill=tk.X, padx=10, pady=5)

            for item in order['items']:
                tk.Label(
                    items_frame,
                    text=f"{item['quantity']} x {item['title']} @ ${item['price']:.2f}",
                    font=("Georgia", 11),
                    bg="white",
                    fg=self.text_color,
                    anchor="w"
                ).pack(fill=tk.X, pady=2)

            # Order summary
            summary_frame = tk.Frame(order_frame, bg="white")
            summary_frame.pack(fill=tk.X, padx=10, pady=5)

            tk.Label(
                summary_frame,
                text=f"Shipping: {order['shipping']}",
                font=("Georgia", 11),
                bg="white",
                fg=self.text_color
            ).pack(anchor="w", pady=2)

            if order['promo']:
                tk.Label(
                    summary_frame,
                    text=f"Promo Code: {order['promo']}",
                    font=("Georgia", 11),
                    bg="white",
                    fg=self.success_color
                ).pack(anchor="w", pady=2)

            tk.Label(
                summary_frame,
                text=f"Total: ${order['total']:.2f}",
                font=("Georgia", 12, "bold"),
                bg="white",
                fg=self.primary_color
            ).pack(anchor="w", pady=5)

            # Cancel button if order is still processing
            if order['status'] == "Processing":
                cancel_button = ttk.Button(
                    order_frame,
                    text="Cancel Order",
                    style='Danger.TButton',
                    command=lambda oid=order_id: self.cancel_order(oid)
                )
                cancel_button.pack(pady=5, ipadx=5, ipady=2)

    def cancel_order(self, order_id):
        if messagebox.askyesno("Confirm", "Are you sure you want to cancel this order?"):
            if self.db.cancel_order(order_id):
                messagebox.showinfo("Success", "Order has been cancelled")
                self.show_order_history()
            else:
                messagebox.showerror("Error", "Could not cancel order")

    def search_books(self):
        query = self.search_entry.get().lower()
        if not query:
            self.display_books(self.db.get_books())
            return

        matching_books = {
            bid: book 
            for bid, book in self.db.get_books().items() 
            if query in book['title'].lower() or query in book['author'].lower()
        }

        self.display_books(matching_books)

    def show_admin_dashboard(self):
        self.clear_window()

        # Header frame
        header_frame = tk.Frame(self.root, bg=self.primary_color)
        header_frame.pack(fill=tk.X, padx=10, pady=10)

        welcome_label = tk.Label(
            header_frame,
            text="Admin Dashboard",
            font=("Georgia", 16, "bold"),
            fg=self.highlight_color,
            bg=self.primary_color
        )
        welcome_label.pack(side=tk.LEFT, padx=20)

        logout_button = ttk.Button(
            header_frame,
            text="🚪 Logout",
            style='Danger.TButton',
            command=self.logout
        )
        logout_button.pack(side=tk.RIGHT, padx=10, ipadx=10, ipady=3)

        # Main content frame
        content_frame = tk.Frame(self.root, bg=self.bg_color)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Decorative top border
        top_border = tk.Frame(content_frame, bg=self.highlight_color, height=5)
        top_border.pack(fill=tk.X, pady=(0, 20))

        # Dashboard buttons frame
        buttons_frame = tk.Frame(content_frame, bg=self.bg_color)
        buttons_frame.pack(expand=True)

        # Configure grid for buttons
        buttons_frame.grid_columnconfigure(0, weight=1)
        buttons_frame.grid_columnconfigure(1, weight=1)
        buttons_frame.grid_rowconfigure(0, weight=1)
        buttons_frame.grid_rowconfigure(1, weight=1)

        # Manage Books button
        manage_books_btn = ttk.Button(
            buttons_frame,
            text="📚 Manage Books",
            command=self.manage_books,
            style='TButton'
        )
        manage_books_btn.grid(row=0, column=0, padx=20, pady=20, sticky="nsew", ipadx=20, ipady=15)

        # Manage Users button
        manage_users_btn = ttk.Button(
            buttons_frame,
            text="👥 Manage Users",
            command=self.manage_users,
            style='TButton'
        )
        manage_users_btn.grid(row=0, column=1, padx=20, pady=20, sticky="nsew", ipadx=20, ipady=15)

        # View Reports button
        view_reports_btn = ttk.Button(
            buttons_frame,
            text="📊 View Reports",
            command=self.view_reports,
            style='TButton'
        )
        view_reports_btn.grid(row=1, column=0, padx=20, pady=20, sticky="nsew", ipadx=20, ipady=15)

        # Manage Promos button
        manage_promos_btn = ttk.Button(
            buttons_frame,
            text="🎫 Manage Promos",
            command=self.manage_promos,
            style='TButton'
        )
        manage_promos_btn.grid(row=1, column=1, padx=20, pady=20, sticky="nsew", ipadx=20, ipady=15)

        # Decorative bottom border
        bottom_border = tk.Frame(content_frame, bg=self.highlight_color, height=5)
        bottom_border.pack(fill=tk.X, pady=(20, 0))

    def manage_users(self):
        self.clear_window()
        
        # Header frame
        header_frame = tk.Frame(self.root, bg=self.accent_color)
        header_frame.pack(fill=tk.X, padx=10, pady=10)
        
        welcome_label = tk.Label(
            header_frame, 
            text=f"Manage Users", 
            font=("Georgia", 16, "bold"), 
            fg=self.primary_color, 
            bg=self.accent_color
        )
        welcome_label.pack(side=tk.LEFT, padx=20)
        
        back_button = tk.Button(
            header_frame, 
            text="⬅ Back to Dashboard", 
            font=("Georgia", 14), 
            bg=self.button_color, 
            fg=self.button_text,
            relief=tk.RAISED,
            bd=3,
            command=self.show_admin_dashboard
        )
        back_button.pack(side=tk.RIGHT, padx=10, ipadx=10, ipady=3)
        
        # Users frame
        users_frame = tk.Frame(self.root, bg=self.bg_color)
        users_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Create a canvas for scrollable users
        users_canvas = tk.Canvas(users_frame, bg=self.bg_color, highlightthickness=0)
        users_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(users_frame, orient=tk.VERTICAL, command=users_canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        users_canvas.configure(yscrollcommand=scrollbar.set)
        users_canvas.bind('<Configure>', lambda e: users_canvas.configure(scrollregion=users_canvas.bbox("all")))
        
        users_container = tk.Frame(users_canvas, bg=self.bg_color)
        users_canvas.create_window((0, 0), window=users_container, anchor="nw")
        
        # Display users with admin toggle and block options
        for username, user in sorted(self.db.users.items()):
            if username == self.auth.current_user:  # Skip current admin
                continue
                
            user_frame = tk.Frame(
                users_container, 
                bg="white", 
                bd=2, 
                relief=tk.RAISED,
                highlightbackground=self.primary_color,
                highlightthickness=1
            )
            user_frame.pack(fill=tk.X, padx=10, pady=10, ipadx=10, ipady=10)
            
            # User info
            tk.Label(
                user_frame, 
                text=f"Username: {username}", 
                font=("Georgia", 12, "bold"), 
                bg="white",
                fg=self.text_color
            ).grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=2)
            
            tk.Label(
                user_frame, 
                text=f"Email: {user['email']}", 
                font=("Georgia", 11), 
                bg="white",
                fg=self.text_color
            ).grid(row=1, column=0, columnspan=2, sticky="w", padx=10, pady=2)
            
            tk.Label(
                user_frame, 
                text=f"Address: {user['address']}", 
                font=("Georgia", 11), 
                bg="white",
                fg=self.text_color
            ).grid(row=2, column=0, columnspan=2, sticky="w", padx=10, pady=2)
            
            # Admin toggle
            admin_var = tk.BooleanVar(value=user['is_admin'])
            admin_check = tk.Checkbutton(
                user_frame, 
                text="Admin", 
                variable=admin_var, 
                font=("Georgia", 11), 
                bg="white",
                fg=self.text_color,
                activebackground="white",
                selectcolor=self.primary_color,
                command=lambda un=username, av=admin_var: self.toggle_admin(un, av.get())
            )
            admin_check.grid(row=3, column=0, padx=10, pady=5, sticky="w")
            
            # Block button
            block_button = tk.Button(
                user_frame, 
                text="Block User", 
                font=("Georgia", 11), 
                bg="#ff3333", 
                fg="white",
                relief=tk.RAISED,
                bd=2,
                command=lambda un=username: self.block_user(un)
            )
            block_button.grid(row=3, column=1, padx=10, pady=5, sticky="e")
    
    def toggle_admin(self, username, is_admin):
        self.db.users[username]['is_admin'] = is_admin
        status = "granted" if is_admin else "revoked"
        messagebox.showinfo("Success", f"Admin privileges {status} for {username}")
    
    def block_user(self, username):
        if messagebox.askyesno("Confirm", f"Are you sure you want to block {username}?"):
            del self.db.users[username]
            messagebox.showinfo("Success", f"User {username} has been blocked")
            self.manage_users()  # Refresh the user list
    
    def view_reports(self):
        self.clear_window()
        
        # Header frame
        header_frame = tk.Frame(self.root, bg=self.accent_color)
        header_frame.pack(fill=tk.X, padx=10, pady=10)
        
        welcome_label = tk.Label(
            header_frame, 
            text=f"Sales Reports", 
            font=("Georgia", 16, "bold"), 
            fg=self.primary_color, 
            bg=self.accent_color
        )
        welcome_label.pack(side=tk.LEFT, padx=20)
        
        back_button = tk.Button(
            header_frame, 
            text="⬅ Back to Dashboard", 
            font=("Georgia", 14), 
            bg=self.button_color, 
            fg=self.button_text,
            relief=tk.RAISED,
            bd=3,
            command=self.show_admin_dashboard
        )
        back_button.pack(side=tk.RIGHT, padx=10, ipadx=10, ipady=3)
        
        # Reports frame
        reports_frame = tk.Frame(self.root, bg=self.bg_color)
        reports_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Calculate some simple reports
        total_orders = len(self.db.orders)
        total_revenue = sum(order['total'] for order in self.db.orders.values())
        total_books_sold = sum(
            sum(item['quantity'] for item in order['items']) 
            for order in self.db.orders.values()
        )
        
        # Display reports
        tk.Label(
            reports_frame, 
            text="Sales Summary", 
            font=("Georgia", 16, "bold"), 
            bg=self.bg_color,
            fg=self.primary_color
        ).pack(pady=10)
        
        # Summary frame
        summary_frame = tk.Frame(reports_frame, bg=self.bg_color)
        summary_frame.pack(pady=10)
        
        tk.Label(
            summary_frame, 
            text=f"📦 Total Orders: {total_orders}", 
            font=("Georgia", 14), 
            bg=self.bg_color,
            fg=self.text_color
        ).grid(row=0, column=0, sticky="w", padx=20, pady=5)
        
        tk.Label(
            summary_frame, 
            text=f"💰 Total Revenue: ${total_revenue:.2f}", 
            font=("Georgia", 14), 
            bg=self.bg_color,
            fg=self.text_color
        ).grid(row=1, column=0, sticky="w", padx=20, pady=5)
        
        tk.Label(
            summary_frame, 
            text=f"📚 Total Books Sold: {total_books_sold}", 
            font=("Georgia", 14), 
            bg=self.bg_color,
            fg=self.text_color
        ).grid(row=2, column=0, sticky="w", padx=20, pady=5)
        
        # Recent orders
        tk.Label(
            reports_frame, 
            text="Recent Orders", 
            font=("Georgia", 14, "bold"), 
            bg=self.bg_color,
            fg=self.text_color
        ).pack(pady=10)
        
        recent_orders_frame = tk.Frame(reports_frame, bg=self.bg_color)
        recent_orders_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Create a canvas for scrollable recent orders
        orders_canvas = tk.Canvas(recent_orders_frame, bg=self.bg_color, highlightthickness=0)
        orders_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(recent_orders_frame, orient=tk.VERTICAL, command=orders_canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        orders_canvas.configure(yscrollcommand=scrollbar.set)
        orders_canvas.bind('<Configure>', lambda e: orders_canvas.configure(scrollregion=orders_canvas.bbox("all")))
        
        orders_container = tk.Frame(orders_canvas, bg=self.bg_color)
        orders_canvas.create_window((0, 0), window=orders_container, anchor="nw")
        
        # Display recent orders
        for order_id, order in sorted(self.db.orders.items(), key=lambda x: x[1]['date'], reverse=True)[:10]:
            order_frame = tk.Frame(
                orders_container, 
                bg="white", 
                bd=2, 
                relief=tk.RAISED,
                highlightbackground=self.primary_color,
                highlightthickness=1
            )
            order_frame.pack(fill=tk.X, padx=10, pady=5, ipadx=10, ipady=5)
            
            tk.Label(
                order_frame, 
                text=f"📦 Order #{order_id} by {order['user']} - {order['date']}", 
                font=("Georgia", 11, "bold"), 
                bg="white",
                fg=self.text_color
            ).pack(pady=5)
            
            tk.Label(
                order_frame, 
                text=f"📦 Items: {len(order['items'])} | 💰 Total: ${order['total']:.2f} | 🚚 Status: {order['status']}", 
                font=("Georgia", 11), 
                bg="white",
                fg=self.text_color
            ).pack(pady=5)
    
    def manage_books(self):
        self.clear_window()

        # Header frame
        header_frame = tk.Frame(self.root, bg=self.primary_color)
        header_frame.pack(fill=tk.X, padx=10, pady=10)

        welcome_label = tk.Label(
            header_frame,
            text="Manage Books",
            font=("Georgia", 16, "bold"),
            fg=self.highlight_color,
            bg=self.primary_color
        )
        welcome_label.pack(side=tk.LEFT, padx=20)

        back_button = ttk.Button(
            header_frame,
            text="⬅ Back to Dashboard",
            command=self.show_admin_dashboard
        )
        back_button.pack(side=tk.RIGHT, padx=10, ipadx=10, ipady=3)

        add_button = ttk.Button(
            header_frame,
            text="➕ Add New Book",
            style='Success.TButton',
            command=self.show_add_book_form
        )
        add_button.pack(side=tk.RIGHT, padx=10, ipadx=10, ipady=3)

        # Books frame
        books_frame = tk.Frame(self.root, bg=self.bg_color)
        books_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Create a canvas for scrollable books
        books_canvas = tk.Canvas(books_frame, bg=self.bg_color, highlightthickness=0)
        books_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(books_frame, orient=tk.VERTICAL, command=books_canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        books_canvas.configure(yscrollcommand=scrollbar.set)
        books_canvas.bind('<Configure>', lambda e: books_canvas.configure(scrollregion=books_canvas.bbox("all")))

        books_container = tk.Frame(books_canvas, bg=self.bg_color)
        books_canvas.create_window((0, 0), window=books_container, anchor="nw")

        # Display books with edit/delete options
        for book_id, book in self.db.get_books().items():
            book_frame = tk.Frame(
                books_container,
                bg="white",
                bd=2,
                relief=tk.RAISED,
                highlightbackground=self.primary_color,
                highlightthickness=1
            )
            book_frame.pack(fill=tk.X, padx=10, pady=10, ipadx=10, ipady=10)

            # Book info
            tk.Label(
                book_frame,
                text=f"{book['title']} by {book['author']}",
                font=("Georgia", 12, "bold"),
                bg="white",
                fg=self.text_color
            ).grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=2)

            tk.Label(
                book_frame,
                text=f"Price: ${book['price']:.2f} | Stock: {book['stock']} | Category: {book['category']}",
                font=("Georgia", 11),
                bg="white",
                fg=self.text_color
            ).grid(row=1, column=0, sticky="w", padx=10, pady=2)

            tk.Label(
                book_frame,
                text=book['description'],
                font=("Georgia", 11),
                bg="white",
                fg=self.text_color,
                wraplength=600
            ).grid(row=2, column=0, columnspan=2, sticky="w", padx=10, pady=5)

            # Edit/delete buttons
            edit_button = ttk.Button(
                book_frame,
                text="✏ Edit",
                command=lambda bid=book_id: self.show_edit_book_form(bid)
            )
            edit_button.grid(row=3, column=0, padx=10, pady=5, ipadx=5, ipady=2)

            delete_button = ttk.Button(
                book_frame,
                text="🗑 Delete",
                style='Danger.TButton',
                command=lambda bid=book_id: self.delete_book(bid)
            )
            delete_button.grid(row=3, column=1, padx=10, pady=5, ipadx=5, ipady=2)

    def show_add_book_form(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add New Book")
        add_window.geometry("500x500")
        add_window.configure(bg=self.bg_color)

        tk.Label(
            add_window,
            text="Add New Book",
            font=("Georgia", 16, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        ).pack(pady=10)

        form_frame = tk.Frame(add_window, bg=self.bg_color)
        form_frame.pack(pady=10, padx=20)

        # Title
        tk.Label(form_frame, text="Title:", font=("Georgia", 12), bg=self.bg_color, fg=self.text_color).grid(row=0, column=0, sticky="w", pady=5)
        title_entry = ttk.Entry(form_frame, font=("Georgia", 12))
        title_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        # Author
        tk.Label(form_frame, text="Author:", font=("Georgia", 12), bg=self.bg_color, fg=self.text_color).grid(row=1, column=0, sticky="w", pady=5)
        author_entry = ttk.Entry(form_frame, font=("Georgia", 12))
        author_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        # Price
        tk.Label(form_frame, text="Price:", font=("Georgia", 12), bg=self.bg_color, fg=self.text_color).grid(row=2, column=0, sticky="w", pady=5)
        price_entry = ttk.Entry(form_frame, font=("Georgia", 12))
        price_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        # Stock
        tk.Label(form_frame, text="Stock:", font=("Georgia", 12), bg=self.bg_color, fg=self.text_color).grid(row=3, column=0, sticky="w", pady=5)
        stock_entry = ttk.Entry(form_frame, font=("Georgia", 12))
        stock_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        # Category
        categories = sorted(list(set(book["category"] for book in self.db.get_books().values())))
        tk.Label(form_frame, text="Category:", font=("Georgia", 12), bg=self.bg_color, fg=self.text_color).grid(row=4, column=0, sticky="w", pady=5)
        category_entry = ttk.Combobox(form_frame, values=categories, font=("Georgia", 12))
        category_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

        # Description
        tk.Label(form_frame, text="Description:", font=("Georgia", 12), bg=self.bg_color, fg=self.text_color).grid(row=5, column=0, sticky="nw", pady=5)
        description_text = tk.Text(form_frame, font=("Georgia", 12), height=5, width=30, bg="white", fg=self.text_color)
        description_text.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

        # Buttons
        button_frame = tk.Frame(add_window, bg=self.bg_color)
        button_frame.pack(pady=10)

        save_button = ttk.Button(
            button_frame,
            text="💾 Save",
            style='Success.TButton',
            command=lambda: self.save_new_book(
                title_entry.get(),
                author_entry.get(),
                price_entry.get(),
                stock_entry.get(),
                description_text.get("1.0", tk.END).strip(),
                category_entry.get(),
                add_window
            )
        )
        save_button.pack(side=tk.LEFT, padx=10, ipadx=10, ipady=5)

        cancel_button = ttk.Button(
            button_frame,
            text="✖ Cancel",
            style='Danger.TButton',
            command=add_window.destroy
        )
        cancel_button.pack(side=tk.LEFT, padx=10, ipadx=10, ipady=5)

    def save_new_book(self, title, author, price, stock, description, category, window):
        if not all([title, author, price, stock, description, category]):
            messagebox.showerror("Error", "Please fill in all fields")
            return

        try:
            price = float(price)
            stock = int(stock)
            if price <= 0 or stock < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Price must be a positive number and stock a non-negative integer")
            return

        book_id = self.db.add_book(title, author, price, stock, description, category)
        messagebox.showinfo("Success", f"Book added successfully with ID: {book_id}")
        window.destroy()
        self.manage_books()  # Refresh the book list

    def delete_book(self, book_id):
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this book?"):
            if self.db.remove_book(book_id):
                messagebox.showinfo("Success", "Book deleted successfully")
                self.manage_books()  # Refresh the book list
            else:
                messagebox.showerror("Error", "Failed to delete book")
                
    def manage_promos(self):
        self.clear_window()

        # Header frame
        header_frame = tk.Frame(self.root, bg=self.primary_color)
        header_frame.pack(fill=tk.X, padx=10, pady=10)

        welcome_label = tk.Label(
            header_frame,
            text="Manage Promo Codes",
            font=("Georgia", 16, "bold"),
            fg=self.highlight_color,
            bg=self.primary_color
        )
        welcome_label.pack(side=tk.LEFT, padx=20)

        back_button = ttk.Button(
            header_frame,
            text="⬅ Back to Dashboard",
            command=self.show_admin_dashboard
        )
        back_button.pack(side=tk.RIGHT, padx=10, ipadx=10, ipady=3)

        add_button = ttk.Button(
            header_frame,
            text="➕ Add New Promo",
            style='Success.TButton',
            command=self.show_add_promo_form
        )
        add_button.pack(side=tk.RIGHT, padx=10, ipadx=10, ipady=3)

        # Promos frame
        promos_frame = tk.Frame(self.root, bg=self.bg_color)
        promos_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Create a canvas for scrollable promos
        promos_canvas = tk.Canvas(promos_frame, bg=self.bg_color, highlightthickness=0)
        promos_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(promos_frame, orient=tk.VERTICAL, command=promos_canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        promos_canvas.configure(yscrollcommand=scrollbar.set)
        promos_canvas.bind('<Configure>', lambda e: promos_canvas.configure(scrollregion=promos_canvas.bbox("all")))

        promos_container = tk.Frame(promos_canvas, bg=self.bg_color)
        promos_canvas.create_window((0, 0), window=promos_container, anchor="nw")

        # Display promos
        for code, discount in self.db.promos.items():
            promo_frame = tk.Frame(
                promos_container,
                bg="white",
                bd=2,
                relief=tk.RAISED,
                highlightbackground=self.primary_color,
                highlightthickness=1
            )
            promo_frame.pack(fill=tk.X, padx=10, pady=10, ipadx=10, ipady=10)

            # Promo info
            tk.Label(
                promo_frame,
                text=f"Code: {code}",
                font=("Georgia", 14, "bold"),
                bg="white",
                fg=self.text_color
            ).grid(row=0, column=0, sticky="w", padx=10, pady=2)

            tk.Label(
                promo_frame,
                text=f"Discount: {int((1-discount)*100)}% off",
                font=("Georgia", 12),
                bg="white",
                fg=self.text_color
            ).grid(row=1, column=0, sticky="w", padx=10, pady=2)

            # Delete button
            delete_button = ttk.Button(
                promo_frame,
                text="Delete",
                style='Danger.TButton',
                command=lambda c=code: self.delete_promo(c)
            )
            delete_button.grid(row=0, column=1, rowspan=2, padx=10, pady=5, sticky="e")

    def show_add_promo_form(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add New Promo Code")
        add_window.geometry("400x300")
        add_window.configure(bg=self.bg_color)

        tk.Label(
            add_window,
            text="Add New Promo Code",
            font=("Georgia", 16, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        ).pack(pady=10)

        form_frame = tk.Frame(add_window, bg=self.bg_color)
        form_frame.pack(pady=10, padx=20)

        # Promo Code
        tk.Label(form_frame, text="Promo Code:", font=("Georgia", 12), bg=self.bg_color, fg=self.text_color).grid(row=0, column=0, sticky="w", pady=5)
        code_entry = ttk.Entry(form_frame, font=("Georgia", 12))
        code_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        # Discount Percentage
        tk.Label(form_frame, text="Discount (%):", font=("Georgia", 12), bg=self.bg_color, fg=self.text_color).grid(row=1, column=0, sticky="w", pady=5)
        discount_entry = ttk.Entry(form_frame, font=("Georgia", 12))
        discount_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        # Buttons
        button_frame = tk.Frame(add_window, bg=self.bg_color)
        button_frame.pack(pady=10)

        save_button = ttk.Button(
            button_frame,
            text="💾 Save",
            style='Success.TButton',
            command=lambda: self.save_new_promo(
                code_entry.get().strip().upper(),
                discount_entry.get(),
                add_window
            )
        )
        save_button.pack(side=tk.LEFT, padx=10, ipadx=10, ipady=5)

        cancel_button = ttk.Button(
            button_frame,
            text="✖ Cancel",
            style='Danger.TButton',
            command=add_window.destroy
        )
        cancel_button.pack(side=tk.LEFT, padx=10, ipadx=10, ipady=5)

    def save_new_promo(self, code, discount, window):
        if not code or not discount:
            messagebox.showerror("Error", "Please fill in all fields")
            return

        try:
            discount = float(discount)
            if discount <= 0 or discount >= 100:
                raise ValueError
            discount_factor = 1 - (discount / 100)
        except ValueError:
            messagebox.showerror("Error", "Discount must be a number between 0 and 100")
            return

        if code in self.db.promos:
            messagebox.showerror("Error", "Promo code already exists")
            return

        self.db.promos[code] = discount_factor
        messagebox.showinfo("Success", f"Promo code {code} added successfully!")
        window.destroy()
        self.manage_promos()  # Refresh the promo list

    def delete_promo(self, code):
        if messagebox.askyesno("Confirm", f"Are you sure you want to delete promo code {code}?"):
            del self.db.promos[code]
            messagebox.showinfo("Success", "Promo code deleted successfully")
            self.manage_promos()  # Refresh the promo list
    
    def logout(self):
        self.auth.logout()
        self.cart.clear()
        self.show_auth_page()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Main function
if __name__ == "__main__":
    root = tk.Tk()
    app = BookstoreApp(root)
    root.mainloop()