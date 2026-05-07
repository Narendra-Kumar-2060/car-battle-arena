import random
import json
import os
from car import Car

SAVE_FILE = "save.json"


def capture_chance(health):
    enemy_hp_percent = health / 100
    chance = (1 - enemy_hp_percent) * 100
    roll = random.randint(1, 100)
    if roll <= chance:
        return True
    return False


def save_game(player_car, captured_cars):

    save_data = {
        "player_car": {
            "name": player_car.name,
            "speed": player_car.speed,
            "durability": player_car.durability,
            "fuel": player_car.fuel,
            "hp": player_car.hp,
        },
        "captured_cars": [],
    }

    for car in captured_cars:
        save_data["captured_cars"].append(
            {
                "name": car.name,
                "speed": car.speed,
                "durability": car.durability,
                "fuel": car.fuel,
                "hp": car.hp,
            }
        )

    with open(SAVE_FILE, "w") as f:
        json.dump(save_data, f, indent=4)

    print(f"\n💾 Game saved! ({len(captured_cars)} cars in garage)")


def load_game():
    if not os.path.exists(SAVE_FILE):
        return None, None

    with open(SAVE_FILE, "r") as f:
        save_data = json.load(f)

    player_data = save_data["player_car"]
    player_car = Car(
        player_data["name"],
        player_data["speed"],
        player_data["durability"],
        player_data["fuel"],
    )
    player_car.hp = player_data["hp"]

    captured_cars = []
    for car_data in save_data["captured_cars"]:
        car = Car(
            car_data["name"],
            car_data["speed"],
            car_data["durability"],
            car_data["fuel"],
        )
        car.hp = car_data["hp"]
        captured_cars.append(car)

    print(f"\n📀 Game loaded! ({len(captured_cars)} cars in garage)")
    return player_car, captured_cars
