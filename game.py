import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Function to update the game
import tkinter as tk
import random

# Initialize scores
user_score = 0
computer_score = 0

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        return "It's a tie!", user_score, computer_score
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        user_score += 1
        return "You win!", user_score, computer_score
    else:
        computer_score += 1
        return "Computer wins!", user_score, computer_score

# Function to play a round
def play_round():
    user_choice = user_choice_var.get()
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    result, user_score, computer_score = determine_winner(user_choice, computer_choice)

    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\nResult: {result}")
    score_label.config(text=f"Your score: {user_score}\nComputer's score: {computer_score}")
    play_button.config(state=tk.NORMAL)

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_var.set("")  # Clear the user's choice
    result_label.config(text="Make your choice...")
    score_label.config(text="Your score: 0\nComputer's score: 0")
    play_button.config(state=tk.NORMAL)

# Create the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")

# Create label and entry for user choice
user_choice_label = tk.Label(window, text="Choose Rock, Paper, or Scissors:")
user_choice_label.pack()
user_choice_var = tk.StringVar()
user_choice_entry = tk.Entry(window, textvariable=user_choice_var)
user_choice_entry.pack()

# Create play button
play_button = tk.Button(window, text="Play", command=play_round)
play_button.pack()

# Create label to display the result
result_label = tk.Label(window, text="Make your choice...")
result_label.pack()

# Create label to display the scores
score_label = tk.Label(window, text="Your score: 0\nComputer's score: 0")
score_label.pack()

# Create reset button
reset_button = tk.Button(window, text="Reset", command=reset_game)
reset_button.pack()

# Start the GUI event loop
window.mainloop()
