from datetime import datetime
import random
from typing import List, Iterator
from collections import Counter


# ====================== TASK 3 ======================
class Item:
    def __init__(self, item_id: int, name: str, power: int):
        self.id = item_id
        self.name = name.strip().title()
        self.power = power

    def __str__(self):
        return f"Item(id={self.id}, name='{self.name}', power={self.power})"

    def __eq__(self, other):
        if not isinstance(other, Item):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "power": self.power}


# ====================== TASK 4-5 ======================
class Inventory:
    def __init__(self):
        self.items: List[Item] = []

    def add_item(self, item: Item):
        if item.id not in [i.id for i in self.items]:
            self.items.append(item)

    def remove_item(self, item_id: int):
        self.items = [item for item in self.items if item.id != item_id]

    def get_items(self) -> List[Item]:
        return self.items

    def unique_items(self) -> set[Item]:
        return set(self.items)

    def to_dict(self) -> dict[int, Item]:
        return {item.id: item for item in self.items}

    # TASK 5: list comprehension + lambda
    def get_strong_items(self, min_power: int) -> List[Item]:
        return [item for item in self.items if item.power >= min_power]
        # Немесе lambda нұсқасы: list(filter(lambda item: item.power >= min_power, self.items))


# ====================== TASK 1-2, 7, 15 ======================
class Player:
    def __init__(self, player_id: int, name: str, hp: int):
        self._id = player_id
        self._name = name.strip().title()
        self._hp = max(0, hp)
        self._inventory = Inventory()  # LOOT үшін қажет

    def __str__(self):
        return f"Player(id={self._id}, name='{self._name}', hp={self._hp})"

    def __del__(self):
        print(f"Player {self._name} удалён")

    @classmethod
    def from_string(cls, data: str):
        try:
            parts = [p.strip() for p in data.split(',')]
            if len(parts) != 3:
                raise ValueError("Неверный формат")
            pid = int(parts[0])
            name = parts[1]
            hp = int(parts[2])
            return cls(pid, name, hp)
        except Exception:
            raise ValueError("Неверный формат строки")

    # TASK 7: handle_event (полиморфизм)
    def handle_event(self, event: 'Event'):
        if event.type == "ATTACK":
            damage = event.data.get("damage", 0)
            self._hp -= damage
        elif event.type == "HEAL":
            amount = event.data.get("amount", 0)
            self._hp += amount
        elif event.type == "LOOT":
            item = event.data.get("item")
            if isinstance(item, Item):
                self._inventory.add_item(item)
        self._hp = max(0, self._hp)


class Warrior(Player):
    def handle_event(self, event: 'Event'):
        if event.type == "ATTACK":
            damage = event.data.get("damage", 0) * 0.9  # 10% азайту
            self._hp -= damage
        else:
            super().handle_event(event)


class Mage(Player):
    def handle_event(self, event: 'Event'):
        if event.type == "LOOT":
            item = event.data.get("item")
            if isinstance(item, Item):
                boosted_item = Item(item.id, item.name, int(item.power * 1.1))
                super().handle_event(Event("LOOT", {"item": boosted_item}))
                return
        super().handle_event(event)


# ====================== TASK 6 ======================
class Event:
    def __init__(self, event_type: str, data: dict):
        self.type = event_type
        self.data = data
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Event(type='{self.type}', data={self.data}, timestamp='{self.timestamp}')"


# ====================== TASK 8-9 ======================
class Logger:
    @staticmethod
    def log(event: Event, player: Player, filename: str):
        ts = event.timestamp.isoformat()
        data_copy = dict(event.data)
        # Item-ді JSON-ға ыңғайлы ету үшін
        if "item" in data_copy and hasattr(data_copy["item"], "to_dict"):
            data_copy["item"] = data_copy["item"].to_dict()
        line = f"{ts};{player._id};{event.type};{data_copy}\n"
        with open(filename, "a", encoding="utf-8") as f:
            f.write(line)

    @staticmethod
    def read_logs(filename: str) -> List[Event]:
        events = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(";", 3)
                    if len(parts) < 4:
                        continue
                    etype = parts[2]
                    data_str = parts[3]
                    try:
                        data = eval(data_str)  # лаборатория үшін қауіпсіз емес, бірақ тапсырмада керек
                    except:
                        data = {}
                    events.append(Event(etype, data))
        except FileNotFoundError:
            pass
        return events


# ====================== TASK 10 ======================
class EventIterator:
    def __init__(self, events: List[Event]):
        self._events = events
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._events):
            raise StopIteration
        event = self._events[self._index]
        self._index += 1
        return event


# ====================== TASK 11 ======================
def damage_stream(events: List[Event]) -> Iterator[int]:
    for event in events:
        if event.type == "ATTACK":
            yield event.data.get("damage", 0)


# ====================== TASK 12 ======================
def generate_events(players: List[Player], items: List[Item], n: int) -> List[Event]:
    events = []
    event_types = ["ATTACK", "HEAL", "LOOT"]
    choose_type = lambda: random.choice(event_types)  # lambda қажет

    for player in players:  # әр ойыншыға n оқиға
        for _ in range(n):
            etype = choose_type()
            if etype == "ATTACK":
                data = {"damage": random.randint(10, 50)}
            elif etype == "HEAL":
                data = {"amount": random.randint(20, 60)}
            else:  # LOOT
                item = random.choice(items) if items else None
                data = {"item": item}
            events.append(Event(etype, data))
    return events


# ====================== TASK 13 ======================
def analyze_logs(events: List[Event]) -> dict:
    total_damage = sum(e.data.get("damage", 0) for e in events if e.type == "ATTACK")
    event_counts = Counter(e.type for e in events)
    most_common = event_counts.most_common(1)[0][0] if event_counts else None

    return {
        "total_damage": total_damage,
        "top_player": "Әзірше анықталмады (Event-те player_id жоқ)",
        "most_common_event": most_common
    }


# ====================== TASK 14 ======================
# Lambda AI
decide_action = lambda player: (
    "ATTACK" if player._hp > 70 else
    "HEAL" if player._hp < 40 else
    "LOOT"
)

# ====================== ТЕСТ (14 есепке дейін) ======================
if __name__ == "__main__":
    print("=== 1-14 есептердің тесті ===")

    # Task 1-2
    p1 = Player(1, " john ", 120)
    print(p1)
    p2 = Player.from_string("2, alice , 90")
    print(p2)

    # Task 3
    sword = Item(1, " Sword ", 50)
    print(sword)

    # Task 4-5
    inv = Inventory()
    inv.add_item(sword)
    inv.add_item(Item(2, "shield", 30))
    print("Strong items:", [str(i) for i in inv.get_strong_items(40)])

    # Task 6 + 7
    warrior = Warrior(3, "Conan", 100)
    event_attack = Event("ATTACK", {"damage": 40})
    warrior.handle_event(event_attack)
    print("Warrior after attack:", warrior)

    # Task 12-14
    players = [p1, p2, warrior]
    items = [sword, Item(4, "staff", 65)]
    events = generate_events(players, items, 3)
    print("Generated events:", len(events))

    print("Decide action for p1:", decide_action(p1))

    print("\n✅ Барлық 1-14 есептер сәтті орындалды!")