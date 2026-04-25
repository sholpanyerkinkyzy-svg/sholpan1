import datetime
import numpy as np
import pandas as pd
from datetime import date
from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI()

#1 және 2
class User:
    def __init__(self, user_id: int, name: str, email: str):
        self._id = user_id
        self._name = name.strip().title()
        if "@" not in email: raise ValueError("Email-да @ болуы керек")
        self._email = email.lower().strip()

    @classmethod
    def from_string(cls, data: str):
        parts = [p.strip() for p in data.split(',')]
        return cls(int(parts[0]), parts[1], parts[2])

    def to_dict(self):
        return {"id": self._id, "name": self._name, "email": self._email}

@app.get("/task1-2")
def task_1_2():
    u = User(1, " alibi ", "Alibi@Example.kz")
    u2 = User.from_string("2, Asel, asel@mail.kz")
    return {"user1": u.to_dict(), "user2": u2.to_dict()}

#3 Есеп
class Product:
    def __init__(self, product_id: int, name: str, price: float, category: str):
        self.id = product_id
        self.name = name.strip().title()
        self.price = float(price)
        self.category = category.strip().capitalize()

    def to_dict(self):
        return {"id": self.id, "name": self.name, "price": self.price, "category": self.category}

@app.get("/task3")
def task_3():
    p = Product(101, " Smartphone ", 800, "electronics")
    return p.to_dict()

#4 және 5 Есеп
class Inventory:
    def __init__(self):
        self.products = []
    def add(self, p: Product):
        self.products.append(p)
    def filter_price(self, min_p):
        return [p for p in self.products if p.price >= min_p]

@app.get("/task4-5")
def task_4_5():
    Пример:
    inv = Inventory()
    inv.add_product(Product(1, "Laptop", 1200.0, "Electronics"))
    inv.add_product(Product(2, "Mouse", 25.0, "Electronics"))
    expensive = inv.filter_by_price(100.0)

    return {"expensive_items": [i.to_dict() for i in expensive]}

#6 Есеп
@app.get("/task6")
def task_6():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"{now};1;BUY_PRODUCT;101\n"
    with open("actions.log", "a") as f: f.write(log_line)
    return {"message": "Лог жазылды (Alibi әрекеті)", "file": "actions.log"}

#7 және 8 Есеп
class Order:
    def __init__(self, order_id, user):
        self.id = order_id
        self.user = user
        self.items = []
    def add(self, p): self.items.append(p)
    def total(self): return sum(p.price for p in self.items)
    def top_n(self, n): return sorted(self.items, key=lambda x: x.price, reverse=True)[:n]

@app.get("/task7-8")
def task_7_8():
    u = User(1, "Alibi", "alibi@mail.kz")
    o = Order(77, u)
    o.add(Product(1, "Watch", 300, "Tech"))
    o.add(Product(2, "Smartphone", 800, "Tech"))
    return {"user": u._name, "total": o.total(), "top_1": o.top_n(1)[0].to_dict()}

#9 және 10
@app.get("/task9-10")
def task_9_10():
    prices = [150, 300, 450]
    def price_gen(lst):
        for p in lst: yield p
    gen = price_gen(prices)
    return {"generator_prices": list(gen)}

#11, 12, 13
@app.get("/task11-13")
def task_11_13():
    arr = np.array([500, 1000, 1500, 2000])
    mean_v = np.mean(arr)
    norm = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))
    return {"mean": float(mean_v), "normalized": norm.tolist()}

# 14, 15, 16
@app.get("/task14-16")
def task_14_16():
    cats = np.array(["Office", "Home", "Office", "Garden"])
    unique_count = len(np.unique(cats))
    return {"unique_categories_count": unique_count}

#17, 18, 19, 20
@app.get("/task17-20")
def task_17_20():
    prices = np.array([1200, 2500, 400])
    discounted = prices * 0.8
    expensive_idx = np.where(prices > 1000)[0].tolist()
    return {"discounted_20pct": discounted.tolist(), "expensive_indices": expensive_idx}

# 21, 22
@app.get("/task21-22", response_class=HTMLResponse)
def task_21_22():
    df = pd.DataFrame([{"id": 1, "name": "Alibi"}, {"id": 2, "name": "Asel"}])
    return df.to_html(classes="table table-striped")

# 23, 24, 25
@app.get("/task23-25")
def task_23_25():
    u_df = pd.DataFrame({"id": [1, 2], "name": ["Alibi", "Asel"]})
    o_df = pd.DataFrame({"user_id": [1, 2], "total": [8000, 4500]})
    merged = pd.merge(u_df, o_df, left_on="id", right_on="user_id")
    return merged.to_dict(orient="records")

#26, 27, 28
@app.get("/task26-28")
def task_26_28():
    df = pd.DataFrame({"category": ["Tech", "Home", "Tech"], "price": [1200, 300, 800]})
    mean_cat = df.groupby("category")["price"].mean().to_dict()
    return {"mean_by_category": mean_cat}

#29, 30
@app.get("/task29-30", response_class=HTMLResponse)
def task_29_30():
    df = pd.DataFrame({"name": ["Smartphone", "Watch", "Laptop"], "price": [800, 300, 1500]})
    df["discounted"] = df["price"] * 0.95 # 5% жеңілдік
    df_sorted = df.sort_values(by="price", ascending=False)
    return df_sorted.to_html(classes="table table-bordered")

@app.get("/")
def welcome():
    return {"message": "Сервер қосулы. Alibi және Asel есімдері қолданылды. /docs арқылы тексеріңіз"}


# 31 . 32
@app.get("/task31-32")
def task_31_32():
    data = {
        "order_id": [101, 102],
        "product_name": ["Laptop", "Mouse"],
        "price": [1200, 25]
    }
    df = pd.DataFrame(data)
    # 31
    df["quantity"] = [1, 2]
    # 32
    df["total_price"] = df["price"] * df["quantity"]
    return df.to_dict(orient="records")

# 33, 34, 35
@app.get("/task33-35")
def task_33_35():
    data = {
        "product_name": ["Laptop", "Mouse", "Shirt"],
        "category": ["Electronics", "Electronics", "Clothing"],
        "price": [1200, 25, 20]
    }
    df = pd.DataFrame(data)
    # 33
    electronics = df[df["category"] == "Electronics"]
    # 34
    counts = df.groupby("category").size().reset_index(name="count")
    # 35
    mean_prices = df.groupby("category")["price"].mean().reset_index(name="mean_price")
    return {
        "electronics": electronics.to_dict(orient="records"),
        "counts": counts.to_dict(orient="records"),
        "means": mean_prices.to_dict(orient="records")
    }

# 36
@app.get("/task36-37")
def task_36_37():
    data = {
        "order_id": [101, 102, 103, 104],
        "total_price": [1200, 50, 500, 1500]
    }
    df = pd.DataFrame(data)
    # 36
    df_sorted = df.sort_values(by="total_price", ascending=False)
    # 37
    top_3 = df_sorted.head(3)
    return top_3.to_dict(orient="records")

# 38, 39, 40
@app.get("/task38-40")
def task_38_40():
    users_df = pd.DataFrame({"user_id": [1, 2], "user_name": ["John", "Alice"]})
    orders_df = pd.DataFrame({"order_id": [101, 102, 103], "user_id": [1, 2, 1], "total_price": [1200, 50, 500]})
    # 38
    merged = pd.merge(orders_df, users_df, on="user_id")
    # 39
    mean_total = merged.groupby("user_name")["total_price"].mean().reset_index(name="mean_total")
    # 40
    order_counts = merged.groupby("user_name")["order_id"].count().reset_index(name="orders_count")
    return {"merged": merged.to_dict(orient="records"), "stats": order_counts.to_dict(orient="records")}

# 41, 42, 43, 44
@app.get("/task41-44")
def task_41_44():
    data = {
        "user_name": ["John", "John", "Alice", "Bob"],
        "total_price": [1200, 500, 25, 1700],
        "category": ["Electronics", "Clothing", "Clothing", "Electronics"]
    }
    df = pd.DataFrame(data)
    # 41
    max_order = df.groupby("user_name")["total_price"].max().reset_index(name="max_order")
    # 42
    unique_cats = df.groupby("user_name")["category"].nunique().reset_index(name="unique_categories")
    user_sums = df.groupby("user_name")["total_price"].sum().reset_index(name="total_sum")
    user_sums["VIP"] = user_sums["total_sum"] > 1000
    user_means = df.groupby("user_name")["total_price"].mean().reset_index(name="mean_total")
    final_sort = pd.merge(user_sums, user_means, on="user_name")
    sorted_df = final_sort.sort_values(by=["total_sum", "mean_total"], ascending=[False, True])
    return sorted_df.to_dict(orient="records")

# 45 Есеп
@app.get("/task45", response_class=HTMLResponse)
def task_45():
    data = {
        "user_name": ["John", "John", "Alice"],
        "order_id": [101, 103, 102],
        "total_price": [1200, 500, 25],
        "category": ["Electronics", "Clothing", "Clothing"]
    }
    df = pd.DataFrame(data)
    report = df.groupby("user_name").agg(
        total_orders=("order_id", "count"),
        total_sum=("total_price", "sum"),
        mean_total=("total_price", "mean"),
        max_order=("total_price", "max"),
        unique_categories=("category", "nunique")
    ).reset_index()
    report["VIP"] = report["total_sum"] > 1000
    return report.to_html(classes="table table-bordered table-striped")