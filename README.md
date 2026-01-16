# 🎯 21 Matchstick Game (Python)

A simple command-line based Python game built using basic programming concepts.  
This project is ideal for beginners to understand **loops, conditionals, functions, and user input handling** in Python.

---

## 📖 Game Description

The **21 Matchstick Game** is a classic logic game played between a user and the computer.

### 🧠 Rules:
- There are **21 matchsticks** initially.
- Players take turns picking **1 to 4 matchsticks**.
- You play first.
- The player who is **forced to pick the last matchstick loses**.

The computer uses a simple strategy to ensure a competitive game.

---

## 🛠️ Technologies Used
- **Python 3**
- Command Line / Terminal

---

## ▶️ How to Run the Game

1. Make sure Python is installed on your system  
   Check using:
   ```bash
   python --version
   Clone this repository:

2. git clone https://github.com/ishika0310/python-project01.git


3. Navigate to the project folder:

```cd python-project01```


4. Run the Python file:

```python matchstick_game.py```

🧩 Game Logic (Brief)

The computer always picks 5 - player_choice

This strategy helps the computer maintain control of the game

Input validation ensures only valid moves (1–4 sticks) are allowed

# 🎮 Tic Tac Toe Game (Python Tkinter)

A simple two-player Tic Tac Toe GUI application built using Python and Tkinter.
This project demonstrates basic GUI programming, event handling, and game logic in Python.

📌 Features

🧑‍🤝‍🧑 Two-player mode (Player X vs Player O)

✍️ Player name input

🖥️ Interactive GUI using Tkinter

🏆 Automatic winner detection

🤝 Tie (draw) detection

🚫 Prevents overwriting already clicked buttons

🎨 Simple and colorful interface

🛠️ Technologies Used

Python 3

Tkinter (Standard Python GUI library)

No external libraries are required.

🚀 How to Run the Project

1️⃣ Prerequisites

Make sure Python is installed:

    python --version

2️⃣ Clone or Download the Repository
git clone https://github.com/Ishika0310/python-project01/blob/main/Tic_Tac_Toe.py

3️⃣ Run the Program
python Tic_Tac_Toe.py

🎮 How to Play

1- Enter Player 1 and Player 2 names.

2- Player 1 starts with X, Player 2 plays O.

3- Click on any empty cell to make a move.

4- The game automatically:

   - Declares the winner 🏆

   - Detects a tie 🤝

   - Disables buttons after game ends

🧠 Game Logic Overview

- Uses a 9-button grid to represent the board.

- Tracks turns using a boolean flag.

- Checks all possible winning combinations:

   - Rows

   - Columns

   - Diagonals

- Displays result using tkinter.messagebox.
