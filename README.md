# Car Battle Arena

A Pokémon-style turn-based battle game where you capture cars instead of creatures. Fight, repair, use nitro boosts, and build your garage of captured cars!

## Features

- **Turn-based combat** with strategic choices
- **Capture system** - Lower enemy HP = higher capture chance
- **Garage collection** - Keep and switch between captured cars
- **Save/Load** - Progress persists between sessions
- **Multiple attack types**:
  - Basic Attack
  - Repair (heal HP, costs fuel)
  - Nitro Boost (heavy damage, costs fuel)
  - Heavy Ram (damage + self damage, costs fuel)
- **Enemy AI** - Opponents make intelligent choices based on HP and fuel

## How to Play

### Start the Game

```bash
python main.py
```

### Main Menu Options

Option Description

1. Start Battle Fight a random enemy car
2. View Garage See all cars you've captured
3. Switch Active Car Change which car you use
4. Save Game Save your progress to a file
5. Load Game Load a previously saved game
6. Quit Exit the game

### Battle Commands

Command Effect

1. Attack Deal damage based on speed vs enemy durability
2. Repair Restore 10 HP (costs 10 fuel)
3. Nitro Boost Deal double speed damage (costs 15 fuel)
4. Heavy Ram Deal 1.5x damage but take 5-10 self damage (costs 10 fuel)
5. Capture Try to catch the enemy car (higher chance at low HP)
6. Skip Gain 8 fuel, do nothing else

### Strategy Tips

- Lower enemy HP = higher capture chance - Weaken them first!
- Capture failure triggers a free enemy attack - Risky but rewarding
- Manage your fuel - Running out limits your options
- Switch damaged cars - Use your garage to rotate fresh cars

## Project Structure

```
car-battle-arena/
│
├── car.py          # Car class with all battle actions
├── main.py         # Game loop, menus, battle logic
├── utils.py        # Helper functions (capture chance, save/load)
└── save.json       # Auto-generated save file (after saving)
```

## Requirements

- Python 3.6 or higher
- No external libraries required (uses only standard library)

## Save System

The game saves to save.json in the same directory. Saved data includes:

- Your active car (HP, fuel, stats)
- All captured cars in your garage

## Capture Formula

```
capture_chance = (1 - enemy_hp / max_hp) × 100
```

- Enemy at 10% HP → 90% capture chance
- Enemy at 50% HP → 50% capture chance
- Enemy at 90% HP → 10% capture chance

## Example Gameplay

```
=== MAIN MENU ===
1. Start Battle
2. View Garage
3. Switch Active Car
4. Save Game
5. Load Game
6. Quit

Choose: 1

⚔️ BATTLE START: Mustang vs Ferrari ⚔️

TURN 1
Mustang → HP: 100 | Fuel: 40
Ferrari → HP: 100 | Fuel: 35

1. Attack | 2. Repair | 3. Nitro Boost | 4. Heavy Ram | 5. Capture | 6. Skip
Choose: 1

Mustang attacks Ferrari for 7 damage!
```

## Author

Narendra Kumar

## License

This project is for learning purposes. Feel free to use, modify, and share.

## Skills Demonstrated

- Object-Oriented Programming (OOP)
- Game loop design
- Probability/randomness implementation
- File I/O and JSON serialization
- User input handling and validation
- State management
