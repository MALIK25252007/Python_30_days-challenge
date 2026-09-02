#WAP that generates random number between 1 and 6 (simulates a dice)
import random
choice=['rock','paper','scissors']
play_again='y'
while play_again=='y'or play_again=='Y':
    print("Starting the game...")
    val=random.randint(0,2)
    print("first player ...",choice[val])
    val1=random.randint(0,2)
    print("first player ...",choice[val1])
    roll_again=input("Do you want to play again? (y/n) : ")