#game.py

print("Rock, Paper, Scissors, Shoot!")

#PROMPT USER FOR INPUT
usermove = input("Game on! Choose 'rock' or 'paper' or 'scissors'!")
print(usermove)

if usermove == "rock":
    print("The computer chose paper")
    print("Paper beats rock")
    print("You lost to the computer")
    print("Please play again!")
elif usermove == "paper":
    print("The computer chose scissors")
    print("Scissors beats paper")
    print("You lost to the computer")
    print("Please play again!")  
elif usermove == "scissors":
    print("The computer chose rock")
    print("Rock beats scissors")
    print("You lost to the computer")
    print("Please play again!")  
else:
    print("Please play again, schoosing either rock, paper, or scissors")