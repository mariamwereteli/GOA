import sys
import random

print('')
playerchoice = input("Enter...\n1 for 1,\n2 for 2, or \n3 for 3,\n4 for 4,\n5 for 5,\n6 for 6:n\n")

player = int(playerchoice)

if player < 1 | player > 6:
    sys.exit("you must enter 1, 2, 3, 4, 5 or 6")
    
    computerchoice = random.choice("123456")
    computer = int(computerchoice)
    
    print("")
    print("you chose " + playerchoice + ".") 
    print("you chose " + computerchoice + ".")
    print("")
    
    if player == 1 and computer == 6:
        print("Computer wins!")
    if player == 2 and computer == 6:
        print("computer wins!")
    if player == 3 and computer == 6:
        print("Computer wins!")
    if player == 5 and computer == 6:
        print("computer wins!")
    if player == 6 and computer == 6:
        print("its a  tie!")
    if player == 1 and computer == 6:
        print("Computer wins!")
    if player == 2 and computer == 5:
        print("computer wins!")
    if player == 3 and computer == 5:
        print("Computer wins!")
    if player == 4 and computer == 5:
        print("computer wins!")
    if player == 5 and computer == 5:
        print("Its a tie")
    if player == 6 and computer == 5:
        print("you win!")
    if player == 1 and computer == 4:
        print("Computer wins!")
    if player == 2 and computer == 4:
        print("computer wins!")
    if player == 3 and computer == 4:
        print("Computer wins!")
    if player == 4 and computer == 4:
        print("its a tie!")
    if player == 5 and computer == 4:
        print("You win!")
    if player == 6 and computer == 4:
        print("You win!")
    if player == 1 and computer == 3:
        print("Computer wins!")
    if player == 2 and computer == 3:
        print("computer wins!")
    if player == 3 and computer == 3:
        print("Its a tie!")
    if player == 4 and computer == 3:
        print("you win!")
    if player == 5 and computer == 3:
        print("You win!")
    if player == 6 and computer == 3:
        print("you win!")
    if player == 1 and computer == 2:
        print("Computer wins!")
    if player == 2 and computer == 2:
        print("its a tie!")
    if player == 3 and computer == 2:
        print("you win!")
    if player == 4 and computer == 2:
        print("you win!")
    if player == 5 and computer == 2:
        print("You win!")
    if player == 6 and computer == 2:
        print("you win!")
    if player == 1 and computer == 1:
        print("its a tie!!")
    if player == 2 and computer == 1:
        print("you win!!")
    if player == 3 and computer == 1:
        print("you win!")
        if player == 4 and computer == 1:
        print("you win!")
    if player == 5 and computer == 1:
        print("You win!")
    if player == 6 and computer == 1: