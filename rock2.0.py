import random

player = input("rock, paper, or scissors?") #Set vairable to player for the user

chosen = random.randint(0,2) #Chosen will use the random.randint function

# Chosen will use the numbers from 0-2

if chosen == 0:
    computer = 'rock'

elif chosen == 1:
    computer = 'scissors'

else:
    computer = 'paper'

#Set the conditions

if player == computer:
    print('Tie')

elif player == 'rock' and computer == 'paper':
        print("Computer wins")

elif player == 'paper' and computer == 'rock':
    print("Player wins")

elif player == 'paper' and computer == 'scissors':
    print("Computer wins")

elif player == 'scissors' and computer == 'paper':
    print("Player wins")

elif player == 'scissors' and computer == 'rock':
    print("Computer wins")

else:
    print("Player wins")


