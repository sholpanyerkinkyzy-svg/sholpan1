from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

# -------- 1-2 Player --------
class Player:
    def __init__(self, player_id: int, name: str, hp: int):
        self._id = player_id
        self._name = name.strip().title()

        self._hp = max(0, hp)

    def __str__(self):
        return f"Player(id={self._id}, name='{self._name}', hp={self._hp})"

    @classmethod
    def from_string(cls, data: str):
        parts = data.split(',')
        if len(parts) != 3:
            raise ValueError("Неверный формат строки")
        return cls(int(parts[0]), parts[1], int(parts[2]))


@app.get("/")
def home():
    return {"message": "Сервер работает"}


@app.get("/player")
def player_info():
    p = Player(1, " john ", 120)
    return {"player": str(p)}


@app.get("/player-from-string")
def player_from_string():
    try:
        p = Player.from_string("2, alice , 90")
        return {"player": str(p)}
    except ValueError as e:
        return {"error": str(e)}


# 3
class Item:
    def __init__(self, item_id: int, name: str, power: int):
        self.id = item_id
        self.name = name.strip().title()
        self.power = power

    def __str__(self):
        return f"Item(id={self.id}, name='{self.name}', power={self.power})"

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)


@app.get("/item")
def item_info():
    i = Item(1, " Sword ", 50)
    return {"item": str(i)}