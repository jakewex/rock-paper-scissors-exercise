#game.py
import random
print("Rock, Paper, Scissors, Shoot!")

#PROMPT USER FOR INPUT
usermove = input("Game on! Choose 'rock' or 'paper' or 'scissors'!")
print("The user chose", usermove)

#DETERMINE CPU CHOICE Randomly
options = ["rock", "paper", "scissors"]
random.shuffle(options)
cpumove = random.choice(options)
print("The computer chose", cpumove)

#DETERMINE WINNER BASED ON CHOICES
if cpumove == usermove:
    print("User and computer both chose", usermove)
    print("Please try again to determine a winner")