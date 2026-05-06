from car import Car
import time
import random

garage = [
    Car("Mustang", 10, 5, 50),
    Car("Ferrari", 8, 3, 40),
    Car("Lambo", 12, 4, 45),
    Car("BMW", 9, 6, 55),
]

print("\n=== GARAGE ===")
print("Choose your car:\n")

for i, car in enumerate(garage):
    print(
        f"{i + 1}. {car.name} (Speed: {car.speed}, Durability: {car.durability}, Fuel: {car.fuel})"
    )

choice = int(input("\nEnter choice: ")) - 1

player_car = garage[choice]

enemy_car = random.choice(garage)

while enemy_car == player_car:
    enemy_car = random.choice(garage)

i = 0
while True:
    i += 1
    print("\n" + "=" * 25)
    print(f"Turn {i}")
    print(f"{player_car.name} → HP: {player_car.hp} | Fuel: {player_car.fuel}")
    print(f"{enemy_car.name} → HP: {enemy_car.hp} | Fuel: {enemy_car.fuel}")
    print("-" * 20)
    while True:
        print("1. Attack | 2. Repair | 3. Nitro Boost | 4. Heavy Ram | 5. Skip")
        player_choice = input("Choose: ")

        if player_choice in ["1", "2", "3", "4", "5"]:
            break
        else:
            print("Invalid choice! Try again.\n")

    if player_choice == "1":
        player_car.attack(enemy_car)
        print()

    elif player_choice == "2":
        player_car.repair()
        print()

    elif player_choice == "3":
        player_car.nitro_boost(enemy_car)
        print()

    elif player_choice == "4":
        player_car.heavy_ram(enemy_car)
        print()

    else:
        print("Skipping Turn...")
        player_car.fuel = min(player_car.fuel + 8, 50)
        print(f"{player_car.name} gained 10 fuel!")
        print()

    if enemy_car.hp <= 0:
        print(f"{enemy_car.name} is destroyed!")
        print(f"{player_car.name} wins!")
        break

    time.sleep(2)

    enemy_car.enemy_turn(player_car)
    print()
    # 🔥 Fuel regeneration per turn
    player_car.fuel = min(player_car.fuel + 5, 50)
    enemy_car.fuel = min(enemy_car.fuel + 5, 50)

    if player_car.hp <= 0:
        print(f"{player_car.name} is destroyed!")
        print(f"{enemy_car.name} wins!")
        break

    print(f"{player_car.name} HP: {player_car.hp}")
    print("-" * 20)
