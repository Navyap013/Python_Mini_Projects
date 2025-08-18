import tkinter as tk
from tkinter import messagebox
import random

# Constants
MAX_SCORE = 50

# Game state
players = 2  # You can change this to 2, 3, or 4
player_scores = [0] * players
current_score = 0
current_player = 0

# Dice roll function
def roll_dice():
    global current_score, current_player

    value = random.randint(1, 6)
    roll_result_label.config(text=f"You rolled a {value}")

    if value == 1:
        current_score = 0
        messagebox.showinfo("Oops!", f"Player {current_player+1} rolled a 1! Turn over.")
        end_turn()
    else:
        current_score += value
        current_score_label.config(text=f"Current Score: {current_score}")

def hold():
    global current_player, current_score

    player_scores[current_player] += current_score
    scores_label.config(text=get_score_text())

    if player_scores[current_player] >= MAX_SCORE:
        messagebox.showinfo("Game Over", f"Player {current_player+1} wins!")
        root.quit()
    else:
        current_score_label.config(text="Current Score: 0")
        current_score = 0
        end_turn()

def end_turn():
    global current_player, current_score
    current_score = 0
    current_score_label.config(text="Current Score: 0")
    current_player = (current_player + 1) % players
    player_turn_label.config(text=f"Player {current_player+1}'s Turn")

def get_score_text():
    return "\n".join([f"Player {i+1}: {score}" for i, score in enumerate(player_scores)])

# GUI setup
root = tk.Tk()
root.title("Pig Dice Game")

player_turn_label = tk.Label(root, text=f"Player {current_player+1}'s Turn", font=('Helvetica', 16))
player_turn_label.pack(pady=10)

roll_button = tk.Button(root, text="Roll", command=roll_dice, font=('Helvetica', 14))
roll_button.pack(pady=5)

hold_button = tk.Button(root, text="Hold", command=hold, font=('Helvetica', 14))
hold_button.pack(pady=5)

roll_result_label = tk.Label(root, text="", font=('Helvetica', 14))
roll_result_label.pack(pady=5)

current_score_label = tk.Label(root, text="Current Score: 0", font=('Helvetica', 14))
current_score_label.pack(pady=5)

scores_label = tk.Label(root, text=get_score_text(), font=('Helvetica', 14))
scores_label.pack(pady=10)

# Start the GUI loop
root.mainloop()