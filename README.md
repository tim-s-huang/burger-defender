# Burger Defender

A small arcade survival game made in Python. You're a burger in in a picnic and swarms of flies are closing in. Click to fire sesame seeds at them before they reach you.

<img width="1266" height="1065" alt="burger defender" src="https://github.com/user-attachments/assets/17285aa8-ea62-48b0-be56-2fceec9af230" />

## How to play
- **Click** anywhere to shoot a seed in that direction
- **Flies** fly in from every side and speed up their spawning over time. Each one that reaches you costs a life
- **Healing flies** occasionally appear. Let one reach you to restore a life (up to 5) and earn bonus points
- The game ends when you run out of lives. Your best score is saved between games

## Run it
Requires Python 3. It only uses the standard library (`turtle` and `tkinter`), so there's nothing to install.
```bash
git clone https://github.com/tim-s-huang/burger-defender.git
cd burger-defender
python main.py
```
Run it from inside the project folder so it can find the sprites and the high score file.

## How it's built
Object-oriented Python using the `turtle` module, with a class for each part of the game:

| File | Responsibility |
|---|---|
| `main.py` | Game loop, sprites, input and difficulty scaling |
| `burger.py` | The player and their lives |
| `bullet.py`, `bullet_manager.py` | Firing seeds towards the click and detecting hits |
| `fly.py`, `heal_fly.py`, `fly_manager.py` | Spawning flies at random screen edges and moving them towards the player |
| `score_manager.py` | Score, lives display and the saved high score |

## Credits
Sprites taken from [Unsplash](https://unsplash.com/) or drawn by me
