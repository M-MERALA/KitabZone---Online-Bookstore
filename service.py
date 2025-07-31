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