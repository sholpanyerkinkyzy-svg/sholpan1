#1-2
class User:
    def __init__(self, user_id: int, name: str, email: str):
        self._id = user_id
        self._name = name.strip().title()

        if "@" not in email:
            raise ValueError("Қате кетті")

        self._email = email.lower().strip()

    @classmethod
    def from_string(cls, data: str):
        parts = [p.strip() for p in data.split(',')]
        return cls(int(parts[0]), parts[1], parts[2])

    def to_dict(self):
        return {"id": self._id, "name": self._name, "email": self._email}


u = User(1, " john doe ", "John@Example.COM")
u2 = User.from_string("2, Alice Wonderland , alice@wonder.com")

print(u.to_dict())
print(u2.to_dict())
#3
class Product:
    def __init__(self, product_id: int, name: str, price: float, category: str):
        self.id = product_id
        self.name = name.strip().title()
        self.price = float(price)
        self.category = category.strip().capitalize()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "category": self.category
        }


p = Product(101, " Smartphone ", 800, "electronics")

print(p.to_dict())
#4
class Product:
    def __init__(self, product_id: int, name: str, price: float):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(id={self.product_id}, name='{self.name}')"


class Inventory:
    def __init__(self):
        self._products = {}

    def add_product(self, product):
        if product.product_id not in self._products:
            self._products[product.product_id] = product

    def get_all_products(self):
        return list(self._products.values())


inv = Inventory()

p1 = Product(1, "Phone", 500)
p2 = Product(2, "Laptop", 1200)

inv.add_product(p1)
inv.add_product(p2)

print(inv.get_all_products())
#5
class Inventory:
    def __init__(self):
        self._products = {}

    def add_product(self, product):
        if product.product_id not in self._products:
            self._products[product.product_id] = product

    def filter_by_price(self, min_price):
        return [p for p in self._products.values() if p.price >= min_price]


inv = Inventory()

p1 = Product(1, "Phone", 500)
p2 = Product(2, "Laptop", 1200)

inv.add_product(p1)
inv.add_product(p2)

print(inv.filter_by_price(600))