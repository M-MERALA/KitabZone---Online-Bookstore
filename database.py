from datetime import datetime
import random

class Database:
    def __init__(self):
        self.users = {
            "Mohammed": {"password": "1234", "email": "mohammed@example.com", "address": "123 Main St", "is_admin": False},
            "Mariam": {"password": "1234", "email": "mariam@example.com", "address": "456 Oak Ave", "is_admin": False},
            "Meral": {"password": "1234", "email": "meral@example.com", "address": "789 Admin Blvd", "is_admin": True},
            "You": {"password": "123", "email": "you@example.com", "address": "456 Oak Ave", "is_admin": False},
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
        for item in items:
            book_id = item["book_id"]
            qty = item["quantity"]
            self.books[book_id]["stock"] -= qty
        return order_id
    
    def get_user_orders(self, username):
        return {oid: order for oid, order in self.orders.items() if order["user"] == username}
    
    def cancel_order(self, order_id):
        if order_id in self.orders and self.orders[order_id]["status"] == "Processing":
            for item in self.orders[order_id]["items"]:
                book_id = item["book_id"]
                qty = item["quantity"]
                self.books[book_id]["stock"] += qty
            self.orders[order_id]["status"] = "Cancelled"
            return True
        return False
    
    def get_promo_discount(self, code):
        return self.promos.get(code, 1.0)