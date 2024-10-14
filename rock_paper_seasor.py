import tkinter as tk
import random

#To determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"
    
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)

    user_choice_label.config(text=f"You chose: {user_choice}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)

    # Update scores
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_score_label.config(text="Your Score: 0")
    computer_score_label.config(text="Computer Score: 0")
    result_label.config(text="")
    user_choice_label.config(text="")
    computer_choice_label.config(text="")

user_score = 0
computer_score = 0
choices = ["rock", "paper", "scissors"]

window = tk.Tk()
window.title("Rock-Paper-Scissors Game")
window.geometry("500x600")

instruction_label = tk.Label(window, text="Choose Rock, Paper, or Scissors:", font=("Helvetica", 18))
instruction_label.pack(pady=20)

user_choice_label = tk.Label(window, text="", font=("Helvetica", 16))
user_choice_label.pack(pady=10)

computer_choice_label = tk.Label(window, text="", font=("Helvetica", 16))
computer_choice_label.pack(pady=10)

result_label = tk.Label(window, text="", font=("Helvetica", 18), fg="blue")
result_label.pack(pady=20)

rock_button = tk.Button(window, text="Rock", width=15, height=2, font=("Helvetica", 16), command=lambda: play("rock"))
rock_button.pack(pady=10)

paper_button = tk.Button(window, text="Paper", width=15, height=2, font=("Helvetica", 16), command=lambda: play("paper"))
paper_button.pack(pady=10)

scissors_button = tk.Button(window, text="Scissors", width=15, height=2, font=("Helvetica", 16), command=lambda: play("scissors"))
scissors_button.pack(pady=10)

user_score_label = tk.Label(window, text="Your Score: 0", font=("Helvetica", 14))
user_score_label.pack(pady=10)

computer_score_label = tk.Label(window, text="Computer Score: 0", font=("Helvetica", 14))
computer_score_label.pack(pady=10)

reset_button = tk.Button(window, text="Reset Game", width=15, height=2, font=("Helvetica", 16), command=reset_game)
reset_button.pack(pady=20)

window.mainloop()


