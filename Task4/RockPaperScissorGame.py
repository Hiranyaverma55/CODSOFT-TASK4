import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(game, play):
        game.play = play
        game.play.title("Rock, Paper, Scissors Game")
        
        game.user_score = 0
        game.computer_score = 0
        
        game.create_game()

    def create_game(game):
        game.info_label = tk.Label(game.play, text="Choose Rock, Paper, or Scissors:", font=("Times New Roman", 16))
        game.info_label.pack(pady=20)
        
        game.rock_button = tk.Button(game.play, text="Rock", command=lambda: game.user_choice("rock"))
        game.rock_button.pack(side=tk.RIGHT, padx=20)
        
        game.paper_button = tk.Button(game.play, text="Paper", command=lambda: game.user_choice("paper"))
        game.paper_button.pack(side=tk.RIGHT, padx=20)
        
        game.scissors_button = tk.Button(game.play, text="Scissors", command=lambda: game.user_choice("scissors"))
        game.scissors_button.pack(side=tk.RIGHT, padx=20)
        
        game.score_label = tk.Label(game.play, text=f"Score - You: {game.user_score}, Computer: {game.computer_score}", font=("Times New Roman", 14))
        game.score_label.pack(pady=20)
        
        game.result_label = tk.Label(game.play, text="", font=("Times New Roman", 14))
        game.result_label.pack(pady=20)

    def user_choice(game, choice):
        computer_choice = game.get_computer_choice()
        winner = game.determine_winner(choice, computer_choice)
        
        game.display_result(choice, computer_choice, winner)
        
    def get_computer_choice(game):
        return random.choice(['rock', 'paper', 'scissors'])
    
    def determine_winner(game, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'tie'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return 'user'
        else:
            return 'computer'
    
    def display_result(game, user_choice, computer_choice, winner):
        result_text = f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n"
        if winner == 'tie':
            result_text += "It's a tie!"
        elif winner == 'user':
            result_text += "You win!"
            game.user_score += 1
        else:
            result_text += "You lose!"
            game.computer_score += 1
        
        game.score_label.config(text=f"Score - You: {game.user_score}, Computer: {game.computer_score}")
        game.result_label.config(text=result_text)

        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if not play_again:
            game.play.quit()

if __name__ == "__main__":
    play = tk.Tk()
    app = RockPaperScissorsApp(play)
    play.mainloop()
