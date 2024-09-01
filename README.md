Here's a README file for the provided Python script (`FINAL_OXO_GAME.py`).

---

# OXO Game

This project is a graphical implementation of the classic Tic-Tac-Toe game (OXO Game) using Python and PyQt5 for the graphical user interface (GUI). It allows two players to connect and play the game over a network.

## Features

- **Graphical User Interface (GUI):** The game is implemented with a user-friendly GUI using PyQt5.
- **Networked Gameplay:** Players can connect over a network to play against each other.
- **Game Board:** The game board displays the current state of the game, including each player's moves.
- **Score Tracking:** The game tracks the score for both players.
- **Play Again Option:** After a game ends, players have the option to start a new game or exit.

## Prerequisites

Before running the game, ensure you have the following installed:

- Python 3.x
- PyQt5
- Necessary images (`images.jfif`, `time-lapse-moving-cloud-on-blue-sky-background.png`, `blank.gif`, `cross.gif`, `nought.gif`)

To install PyQt5, you can use pip:

```bash
pip install PyQt5
```

## Usage

1. **Run the Game:**
   - Start the game by running the `FINAL_OXO_GAME.py` script.

   ```bash
   python FINAL_OXO_GAME.py
   ```

2. **Connect to Opponent:**
   - Enter the opponent's IP address in the "SERVER" input field and click "CONNECT".
   - Once connected, the game will automatically start.

3. **Playing the Game:**
   - Use the buttons labeled `0` to `8` to make your move.
   - The game will notify whose turn it is, and display the winner or if the game is a tie.

4. **Exit the Game:**
   - After the game ends, you can choose to play again or exit by clicking the "EXIT" button.

## Files and Structure

- `FINAL_OXO_GAME.py`: The main Python script for the game.
- `LoopThread.py`: Manages the threading required for handling the game loop.
- `GameClient.py`: Contains the logic for connecting to the game server and managing game states.
- `images.jfif`: The icon for the game window.
- `time-lapse-moving-cloud-on-blue-sky-background.png`: Background image for the game.
- `blank.gif`, `cross.gif`, `nought.gif`: Images used for representing the game board and player moves.

## How the Game Works

- **GUI Layout:**
  - The game window is divided into several sections: connection settings, game board, player shapes, and messages.
  - The game board is represented by 9 positions that players can click to make their move.
  - A message box displays important game notifications like whose turn it is, invalid moves, and game results.

- **Game Logic:**
  - The game communicates over a network using the provided IP address to sync the game state between two players.
  - Each player is assigned a shape (`X` or `O`) and takes turns making moves on the game board.
  - The game checks for a winner or a tie after each move and updates the score accordingly.

## Acknowledgements

- This project utilizes the PyQt5 framework for creating the GUI.
- The images used in this project are sourced from various free image resources.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

This README provides a comprehensive overview of the project, including instructions for installation, usage, and an explanation of the game's structure and logic.
