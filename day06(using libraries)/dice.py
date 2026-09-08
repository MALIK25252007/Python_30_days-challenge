#WAP that generates random number between 1 and 6 (simulates a dice)
import random
min=1
max=6
roll_again='y'
while roll_again=='y'or roll_again=='Y':
    print("Rolling the dice...")
    val=random.randint(min,max)
    print("you get...",val)
    roll_again=input("Roll the dice again? (y/n) : ")