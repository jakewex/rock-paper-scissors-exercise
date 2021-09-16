#game.py
import random
print("Rock, Paper, Scissors, Shoot!")

#PROMPT USER FOR INPUT
usermove = input("Game on! Choose 'rock' or 'paper' or 'scissors'!")
print(usermove)

#DETERMINE CPU CHOICE
options = ["rock", "paper", "scissors"]
random.shuffle(options)
cpumove = random.choice(options)
print("Computer chose")
print(cpumove)