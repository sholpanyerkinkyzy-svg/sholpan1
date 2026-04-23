from fastapi import FastAPI
from datetime import datetime

app = FastAPI()
#1
class Player:
    def __init__(self,player_id : int , name : str , hp : int):
        self._id = player_id
        self._name = name.strip().title()
        self._hp = max(0,hp)

    def __str__(self):
        return f"Player(id={self._id},name={self._name},hp={self._hp})"

    def __del__(self):
        print(f"Player {self._name} удален")

@app.get("/player")
def player_info:
    p=PLayer(1,"john",120)
    return{"player": str(p)}

    @classmethod
    def from_string(cls,data: str)
        parts = data.split(",")
        if len(parts) != 3
            raise ValueError("Неверный формат")
        p_id = int(parts[0].strip())
        p_name = str(parts[1].strip())
        p_hp = int(parts[2].strip())

        return cls(p_id,p_name,p_hp)


@app.get("/player-from-string")
def player_from_string():
    try:
        p = Player.from_string("2, alice , 90")
        return {"player": str(p)}
    except ValueError as e:
        return {"error": str(e)}

#3
class Item:
    def __init__(self, item_id: int , name:str, power:int):
        self_id = item_id
        self_name = name.strip().title()
        self_power = power

    def __str__(self):
        return f"Item(id={self.id},name={self.name},power={self.power}"
    def __eq__(self):
        return self.id == other.id
    def __hash__(self):
        return hash(self.id)
@app.get("/item")
def item_info:
    i = Item(1, " Sword ", 50)
    return{"item": str(i)}

print(i)
print(p)









