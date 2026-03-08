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
       (c1 == "paper" and c2 == "rock") or \
       (c1 == "scissors" and c2 == "paper"):

       return 1 

    return 2 

# Creat a function that save view and remove score from the file

def save_score(name, score):

    with open("score.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer. writerow([name,score])

def view_score():

    try:
        with  open("score.csv", "r") as file:
            reader = csv.reader(file)
            print("\n Score Leadboard")
            for row in reader:
                print("Name:", row[0], "|  Score:", row[1])

    except: 
        print("No score saved.")

def remove_score():
    name = input("Enter name to remove: ")
    rows = []
    try: 
    
        with open ("score.csv", "r") as file: 
            reader = csv. reader(file)
        for row in reader:
            if row[0] != name:
                rows.append(row)
        with open("score.csv", "w") as file:
            writer = csv. writer(file)
            writer.writerows(rows)
        print("Player removed if existed.")
    except:
        print("File not found.")


# Rock, Paper, Scissors between player vs computer 

def play_vs_computer ():
    name = get_player_name()
    
    player = Player(name)
    rounds = get_round()
    
    for i in range(rounds):
        print("\nRound, i + 1")

        player_choice = get_choice(player)
        comp_choice= computer_choice()
        print("Computer chose:", comp_choice)
        result = check_winner(player_choice, comp_choice)

        if result == 1:
            player.score += 1
            print("You win!")
        elif result == 2: 
            print("Computer wins!")
        else:
            print("Tie!")
    print("\nFinal score:", player.score)
    save_score(player.name, player.score)

# Rocke, Paper, Scissors two players

def play_two_player():
    name1 = get_player_name()
    name2 = get_player_name()

    player1 = Player(name1)
    player2 = Player(name2)
    rounds = get_rounds()

    for i in range(rounds):
        print("\nRound", i + 1)
        c1 = get_choice(player1)
        c2 = get_choice(player2)
        result = check_winner(c1,c2)
        
        if result == 1:
            player1.score += 1
            print(name1, "WINS!")
        elif result == 2:
            player2.score += 1
            print(name2, "WINS!")
        else:
            print("Tie!")
    
    print("\nFinal Scores")
    print(name1, player1.score)
    print(name2, player2.score)

    save_score(name1, player1.score)
    save_score(name2, player2.score)

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

# Get the player to chose who to play aganist 
def opponent(): 
    print("Who would you like to compete against?")
    print("1. Computer")
    print("2. Another Player")

    choice = input ("Enter 1 or 2: ")

    while choice != "1" and choice != "2":
        print("Invalid choice")
        choice = input("Enter 1 or 2: ")

        return choice 
# A meun option to the different components of the game

def main():

    while True: 

      print("\n=== ROCK PAPER SCISSORS ====")
      print("1. Play Game")
      print("2. View Scores")
      print("3. Remove Player Score")
      print("4. Exit")
      
      choice = input("Choose Option: ")

      if choice == "1":
          opponent = opponent()
          if opponent == "1":
              play_vs_computer()
          else:
              play_two_player()
      elif choice == "2":
          view_score()
      elif choice == "3":
          remove_score()
      elif choice == "4":
          print("Goodbye")
          break 
      
      else:
          print("Invalid option")


main() 
 