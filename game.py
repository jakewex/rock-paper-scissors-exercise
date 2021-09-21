#game.py
import random
import os

#next handful of lines from Prof Rossetti in slack
from dotenv import load_dotenv

load_dotenv()

x = os.getenv("PLAYER_NAME")
print(x)


#PROMPT USER FOR GAME INPUT
usermove = input("Game on! Choose 'rock' or 'paper' or 'scissors'!")
print("The user chose", usermove)
if usermove == "Rock" or usermove == "ROCK":
    usermove = "rock"
elif usermove == "Paper" or usermove == "PAPER":
    usermove = "paper"
elif usermove == "Scissors" or usermove == "SCISSORS":
    usermove = "scissors"
print("The user chose", usermove)
options = ["rock", "paper", "scissors"]
if usermove not in options:
    print("User did not make a valid choice")
    print("Try again, selecting either 'rock', 'paper', or 'scissors'")
    quit()
else:
    #DETERMINE CPU CHOICE Randomly
    random.shuffle(options)
    cpumove = random.choice(options)
    print("The computer chose", cpumove)

    #DETERMINE WINNER BASED ON CHOICES
    if cpumove == usermove:
        print("User and computer both chose", usermove)
        print("Please try again to determine a winner")
    elif cpumove == "rock":
        if usermove == "paper":
            print("User chose paper. Computer chose rock. User wins!")
            print("Please play again!")
        elif usermove == "scissors":
            print("User chose scissors. Computer chose rock. Computer wins!")
            print("Please play again!")
    elif cpumove == "paper":
        if usermove == "rock":
            print("User chose rock. Computer chose paper. Computer wins!")
            print("Please play again!")
        elif usermove == "scissors":
            print("User chose scissors. Computer chose paper. User wins!")
            print("Please play again!")
    elif cpumove == "scissors":
        if usermove == "paper":
            print("User chose paper. Computer chose scissors. Computer wins!")
            print("Please play again!")
        elif usermove == "rock":
            print("User chose rock. Computer chose scissors. User wins!")
            print("Please play again!")