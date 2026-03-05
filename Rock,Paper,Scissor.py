import random 
# A list to store the player name and score 

player_scores = []
player_names = []

# A meun option to the different components of the game

def display_meun():
    print("\n=== ROCK PAPER SCISSORS ====")
    print("1. Play Game")
    print("2. Computer vs Player")
    print("3. Two players")
    print("4. View score")
    print("5. Remove Player Records")
    print("6. Exit")

    
# Welcome Player to the game, have them introduce themesleve, and pick who they will like to play aganist

def play_game(): 
    name = input("Enter your name")
    print("Welcome", name + "!")
    print("You are Player 1.")
