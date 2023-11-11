from ._base import Base


class Customer(Base):
    @property
    def _base_path(self):
        return "customers"
        
    def data(self, name, email, username):
        return {
            "name": name,
            "email": email,
            "username": username
        }
