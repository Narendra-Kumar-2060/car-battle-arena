import sys
import time
import random
from car import Car
from utils import capture_chance, save_game, load_game

garage = [
    Car("Mustang", 10, 5, 40),
    Car("Ferrari", 12, 3, 35),
    Car("Lambo", 11, 4, 38),
    Car("BMW", 8, 6, 45),
]

captured_cars = []

print("\n=== GARAGE ===")
print("Choose your car:\n")

for i, car in enumerate(garage):
    print(
        f"{i + 1}. {car.name} (Speed: {car.speed}, Durability: {car.durability}, Fuel: {car.fuel})"
    )

choice = int(input("\nEnter choice: ")) - 1
player_car = garage[choice]

while True:
    print("\n" + "=" * 30)
    print("        MAIN MENU")
    print("=" * 30)
    print("1. Start Battle")
    print("2. View Garage")
    print("3. Switch Active Car")
    print("4. Save Game")
    print("5. Load Game")
    print("6. Quit")

    menu_choice = input("\nChoose: ")

    if menu_choice == "1":
        enemy_car = random.choice(garage + captured_cars)
        while enemy_car == player_car:
            enemy_car = random.choice(garage + captured_cars)

        enemy_car.hp = enemy_car.max_hp
        enemy_car.fuel = 40

        print(f"\n⚔️ BATTLE START: {player_car.name} vs {enemy_car.name} ⚔️")
        time.sleep(1)

        turn = 0

        while True:
            turn += 1

            player_car.fuel = min(player_car.fuel + 5, 50)
            enemy_car.fuel = min(enemy_car.fuel + 5, 50)

            print("\n" + "=" * 25)
            print(f"TURN {turn}")
            print(f"{player_car.name} → HP: {player_car.hp} | Fuel: {player_car.fuel}")
            print(f"{enemy_car.name} → HP: {enemy_car.hp} | Fuel: {enemy_car.fuel}")
            print("-" * 20)

            while True:
                print(
                    "1. Attack | 2. Repair | 3. Nitro Boost | 4. Heavy Ram | 5. Capture | 6. Skip"
                )
                player_choice = input("Choose: ")

                if player_choice in ["1", "2", "3", "4", "5", "6"]:
                    break
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

            elif player_choice == "5":
                if enemy_car.hp <= 0:
                    print("Cannot capture a destroyed car!")
                    continue

                print(f"\nAttempting to capture {enemy_car.name}...")
                time.sleep(1)

                if capture_chance(enemy_car.hp):
                    print(f"\n🎉 SUCCESS! You captured {enemy_car.name}! 🎉")

                    new_car = Car(
                        enemy_car.name,
                        enemy_car.speed,
                        enemy_car.durability,
                        enemy_car.fuel,
                    )
                    new_car.hp = new_car.max_hp
                    new_car.fuel = enemy_car.fuel

                    captured_cars.append(new_car)
                    print(f"{enemy_car.name} added to your garage!")
                    print(f"Garage now has {len(captured_cars)} car(s)")

                    enemy_car.hp = 0

                else:
                    print(f"\n❌ {enemy_car.name} broke free and counterattacks! ❌")
                    enemy_car.attack(player_car)

                print()

            else:
                print("Skipping Turn...")
                player_car.fuel = min(player_car.fuel + 8, 50)
                print(f"{player_car.name} gained 8 fuel!")
                print()

            if enemy_car.hp <= 0:
                print(f"\n{enemy_car.name} is destroyed!")
                print(f"🏆 {player_car.name} wins! 🏆")
                break

            time.sleep(2)
            enemy_car.enemy_turn(player_car)
            print()

            if player_car.hp <= 0:
                print(f"\n{player_car.name} is destroyed!")
                print(f"💀 {enemy_car.name} wins! 💀")
                break

            print(f"{player_car.name} HP: {player_car.hp}")
            print("-" * 20)

        input("\nPress Enter to continue...")
        continue

    if menu_choice == "2":
        if not captured_cars:
            print("\nYour garage is empty! Capture cars in battle.")
        else:
            print("\n=== YOUR GARAGE ===")
            for i, car in enumerate(captured_cars, 1):
                print(f"{i}. {car.name} (HP: {car.hp}, Fuel: {car.fuel})")
        input("\nPress Enter to continue...")

    elif menu_choice == "3":
        if not captured_cars:
            print("\nNo captured cars to switch to!")
            input("\nPress Enter to continue...")
            continue

        print("\n=== SWITCH CAR ===")
        print(f"Current car: {player_car.name}")
        print("\nChoose a car from your garage:")

        for i, car in enumerate(captured_cars, 1):
            print(f"{i}. {car.name} (HP: {car.hp}, Fuel: {car.fuel})")

        print(f"{len(captured_cars) + 1}. Cancel")

        try:
            switch_choice = int(input("\nEnter choice: "))
            if 1 <= switch_choice <= len(captured_cars):
                player_car = captured_cars[switch_choice - 1]
                print(f"\n✅ Now driving: {player_car.name}")
            elif switch_choice == len(captured_cars) + 1:
                print("Cancelled.")
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid input!")

        input("\nPress Enter to continue...")

    if menu_choice == "4":
        save_game(player_car, captured_cars)
        input("\nPress Enter to continue...")

    if menu_choice == "5":
        loaded_player, loaded_garage = load_game()
        if loaded_player is not None:
            player_car = loaded_player
            captured_cars = loaded_garage
            print("Game loaded successfully!")
        else:
            print("\nNo save file found! Start a new game first.")
        input("\nPress Enter to continue...")

    if menu_choice == "6":
        print("\nGoodbye! Thanks for playing!")
        sys.exit()

    if menu_choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid choice! Pick 1-6.")
