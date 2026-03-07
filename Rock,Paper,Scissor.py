import random 
import csv
import re
#Validation 
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0


def get_player_name():
    name = input("Enter player name: ")

    while not re.fullmatch("[A-Za-z]+", name):
        print("Invalid name, Use letters only.")
        name = input("ENTER PLAYER NAME:")

        return name 
    

def get_rounds():
    rounds = input("How many rounds(1-10): ")

    while not re.fullmatch("10[1-9]", rounds):
        print("Enter a number between 1 and 10.")
        rounds = input("How many Rounds (1-10)")


# The way the rock paper scissors game will work 

def get_choice(player):
    choice = input(player.name + " choose Rock, Paper or Scissors: ")

    while choice not in ["Rock", "Paper", "Scissors"]:
        print("Invalid choice.")
        choice = input ("Choose rock, paper or scissors: ")

        return choice
    
def computer_choice(): 
    return random.choice(["rock", "paper", "scissors"])
    
def check_winner(c1, c2):
    
    if c1 == c2:
        return 0
    
    if (c1 == "rock" and c2 == "scissors") or \
       (c1 == "paper"" and c2 == "rock") or \
       (c1 == "scissors" and c2 == "paper"):

       return 1 

    return 2 

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

    return input("Select an option: ")
    
# Welcome Player to the game, have them introduce themesleve, and pick who they will like to play aganist and how many rounds 

def play_game(): 
    name = input("Enter your name")
    print("Welcome", name + "!")
    print("You are Player 1.")

def get_round(): 
    while True: 
        try: 
            rounds = int(input("How many rounds? (1-10):"))
            if 1<= round >=10:
                return rounds
            else:
                print("Enter a number between 1 and 10.")
        except:
            print("You have entered an Invalid input. Enter a Number")

def opponent(): 
    print("Who would you like to compete against?")
    print("2. Computer")
    print("3. Another Player")

    choice = input ("Enter 2 or 3: ")




