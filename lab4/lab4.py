
from fastapi import FastAPI

app = FastAPI()


class Player:
    def __init__(self, _id, name, hp):
        self._id = _id
        self._name = name.strip().title()
        self._hp = hp if hp >= 0 else 0

    def __str__(self):
        return f"Player(id={self._id}, name='{self._name}', hp={self._hp})"

    def __del__(self):
        print(f"Player {self._name} удалён")


@app.get("/player")
def get_player():
    p = Player(1, " john ", 120)
    return {"player": str(p)}cd