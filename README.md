# Snake Game - Pygame Edition

A classic, retro Snake Game built using Python and the `pygame` library. Guide the snake, eat the red food to grow longer, and try to achieve the highest score without hitting the walls or your own tail!

---

## Features
- **Smooth Grid-Based Movement:** Fully aligned movement and collision detection preventing bugs.
- **Adjustable Speed:** Configured to a casual speed (`8 FPS`) that is easy to control.
- **Clean Controls:** Prevents instant self-reversals (e.g., pressing Left while moving Right won't crash you).
- **Restart & Quit Options:** Easily replay or exit upon losing.

---

## Prerequisites

Make sure you have Python installed on your system. You will need to install the `pygame` library to run the game.

Open your terminal or command prompt and run:
```bash
pip install pygame
How to Run
Clone or download this repository / code file.

Save the code into a file named snake_game.py.

Open your terminal/command prompt in the folder containing the file.

Run the game using:

Bash
python snake_game.py
Controls
Arrow Keys:

↑ Up Arrow: Move Up

↓ Down Arrow: Move Down

← Left Arrow: Move Left

→ Right Arrow: Move Right

Game Over Screen:

C: Play Again

Q: Quit Game

Code Structure Highlights
WIDTH & HEIGHT: Window dimensions set to 1000x700.

BLOCK_SIZE: Set to 20px to map out the grid cells.

SNAKE_SPEED: Framerate controller set to 8 for a comfortable, slower pace.