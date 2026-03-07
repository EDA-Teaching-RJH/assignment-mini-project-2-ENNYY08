import random 
import csv
import re
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




