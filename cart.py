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