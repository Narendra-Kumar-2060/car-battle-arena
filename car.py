import time
import random


class Car:
    def __init__(self, name, speed, durability, fuel):
        self.name = name
        self.speed = speed
        self.durability = durability
        self.fuel = fuel
        self.hp = 100

    def can_use(self, cost):
        return self.fuel >= cost

    def attack(self, target):
        damage = self.speed - target.durability

        damage = max(damage, 0)

        target.hp -= damage

        target.hp = max(0, target.hp)

        print(f"{self.name} attacks {target.name} for {damage} damage!")

    def repair(self, is_enemy=False):
        if self.hp == 100:
            print("HP already full!")
            return

        if self.fuel < 10:
            print("Not enough fuel...")
            return

        self.hp += 10
        self.hp = min(self.hp, 100)
        self.fuel -= 10

        if is_enemy:
            print(f"{self.name} repairs itself!")
        else:
            print(f"{self.name} repaired 10 HP!")
            print(f"HP: {self.hp} | Fuel: {self.fuel}")

    def nitro_boost(self, target):
        if self.fuel < 15:
            return False  # instead of printing

        damage = self.speed * 2 - target.durability
        damage = max(damage, 0)

        target.hp -= damage
        target.hp = max(0, target.hp)

        self.fuel -= 15

        print(f"{self.name} uses Nitro Boost!")
        print(f"Deals {damage} damage!")

        return True

    def heavy_ram(self, target):
        if self.fuel < 10:
            print("Not enough fuel for Heavy Ram!")
            return

        damage = int(self.speed * 1.5)
        self_damage = random.randint(5, 10)

        target.hp -= damage
        target.hp = max(0, target.hp)

        self.hp -= self_damage
        self.hp = max(0, self.hp)

        self.fuel -= 10

        print(f"{self.name} uses HEAVY RAM!")
        print(f"Deals {damage} damage to {target.name}!")
        print(f"But takes {self_damage} self-damage!")

    def enemy_turn(self, target):
        print(f"{self.name} is thinking...")
        time.sleep(1)

        if self.hp < 30 and self.fuel >= 10:
            choice = random.choice(["repair", "attack"])
        else:
            choice = random.choice(["attack", "nitro", "ram"])

        if choice == "repair":
            self.repair(is_enemy=True)

        elif choice == "attack":
            self.attack(target)

        elif choice == "nitro":
            if self.can_use(15):
                self.nitro_boost(target)
            else:
                print("Fallback: attack")
                self.attack(target)

        elif choice == "ram":
            if self.can_use(10):
                self.heavy_ram(target)
            else:
                print("Fallback: attack")
                self.attack(target)
