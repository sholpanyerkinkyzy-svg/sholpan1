from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

# -------- 1-2 Player --------
class Player:
    def __init__(self, player_id: int, name: str, hp: int):
        self._id = player_id
        self._name = name.strip().title()
        self.inventory = Inventory()
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


# -------- 3 Item --------
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


# -------- 4-5 Inventory --------
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if item.id not in [i.id for i in self.items]:
            self.items.append(item)

    def get_items(self):
        return self.items

    def unique_items(self):
        return list(set(self.items))

    def get_strong_items(self, min_power: int):
        return [item for item in self.items if item.power >= min_power]


@app.get("/inventory")
def inventory_test():
    inv = Inventory()
    inv.add_item(Item(1, "Sword", 50))
    inv.add_item(Item(2, "Shield", 30))

    return {
        "items": [str(i) for i in inv.get_items()],
        "unique_count": len(inv.unique_items())
    }


@app.get("/strong-items")
def strong_items():
    inv = Inventory()
    inv.add_item(Item(1, "Sword", 50))
    inv.add_item(Item(2, "Shield", 30))
    inv.add_item(Item(3, "Axe", 70))

    return {"strong_items": [str(i) for i in inv.get_strong_items(50)]}


# -------- 6 Event --------
class Event:
    def __init__(self, event_type: str, data: dict):
        self.type = event_type
        self.data = data
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Event(type='{self.type}', data={self.data}, timestamp='{self.timestamp}')"


@app.get("/event")
def event_test():
    e = Event("ATTACK", {"damage": 20})
    return {"event": str(e)}


#7 Warrior
class Warrior(Player):
    def handle_event(self, even):
        if event.type == "ATTACK":
            damage = int(event.data.get("damage", 0) * 0.9)
            self._hp -= damage


class Mage(Player):
    def handle_event(self, event):
        if event.type == "LOOT":
            item = event.data.get("item")
            if item:
                item.power = int(item.power * 1.1)
                self.inventory.add_item(item)


@app.get("/event-test")
def event_test_route():
    w = Warrior(1, "Aiman", 100)
    m = Mage(2, "Ali", 100)

    attack = Event("ATTACK", {"damage": 50})
    loot = Event("LOOT", {"item": Item(1, "Sword", 50)})

    w.handle_event(attack)
    m.handle_event(loot)

    return {
        "warrior_hp": w._hp,
        "mage_item_power": m.inventory.get_items()[0].power
    }


#8-9
class Logger:
    def log(self, event, player, filename: str):
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"{event.timestamp};{player._id};{event.type};{event.data}\n")

    def read_logs(self, filename: str):
        events = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(";")
                if len(parts) == 4:
                    e = Event(parts[2], eval(parts[3]))
                    e.timestamp = parts[0]
                    events.append(str(e))
        return events


@app.get("/log-test")
def log_test():
    p = Player(1, "Aiman", 100)
    e = Event("ATTACK", {"damage": 50})
    Logger().log(e, p, "log.txt")
    return {"status": "saved"}


@app.get("/read-logs")
def read_logs():
    events = Logger().read_logs("log.txt")
    return {"logs": events}
#10
class EventIterator:
    def __init__(self, events):
        self.events = events
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.events):
            raise StopIteration
        event = self.events[self.index]
        self.index += 1
        return event


@app.get("/iterator")
def iterator_test():
    events = [
        Event("ATTACK", {"damage": 10}),
        Event("HEAL", {"heal": 5}),
        Event("LOOT", {"item": "Sword"})
    ]

    iterator = EventIterator(events)

    return [str(e) for e in iterator]
#11a
def damage_stream(events):
    for event in events:
        if event.type == "ATTACK":
            yield event.data.get("damage", 0)


@app.get("/damage-stream")
def damage_test():
    events = [
        Event("ATTACK", {"damage": 10}),
        Event("HEAL", {"heal": 5}),
        Event("ATTACK", {"damage": 20}),
    ]

    return [dmg for dmg in damage_stream(events)]
#12
def generate_events(players, items, n):
    return [Event("ATTACK", {"damage": 10}) for _ in range(n)]


@app.get("/generate")
def generate():
    events = generate_events([], [], 3)
    return [str(e) for e in events]


# 13

def analyze_logs(events):
    total = sum(e.data.get("damage", 0) for e in events if e.type == "ATTACK")
    return {"total_damage": total}


@app.get("/analyze")
def analyze():
    events = [
        Event("ATTACK", {"damage": 10}),
        Event("ATTACK", {"damage": 5})
    ]
    return analyze_logs(events)


#14
def decide_action(player):
    return "HEAL" if player._hp < 50 else "ATTACK"


@app.get("/decide")
def decide():
    p = Player(1, "Sholpan", 40)
    return {"action": decide_action(p)}
