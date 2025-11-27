# Snake Water Gun Game 

'''
Snake = 1
Water = -1 
Gun = 0
'''

import random

computer = random.choice([1,-1,0])
youstr = input("Enter your choice : ")
youDict ={"s":1,"w":-1,"g":0}    
reverseDict = {1:"snake",-1:"water",0:"gun"}  

you = youDict[youstr]

print(f"your choice : {reverseDict[you]} \ncomputer choice : {reverseDict[computer]}")


if (computer == you):
    print("it is draw")

else:
    if computer == 1 and you == -1:
        print("you lose!")

    elif computer == 1 and you == 0:
        print("you win!")

    elif computer == -1 and you == 1:
        print("you win!")

    elif computer == -1 and you == 0:
        print("you lose!")

    elif computer == 0 and you == 1:
        print("you lose!")

    elif computer == 0 and you == -1:
        print("you win!")

    else:
        print("Something went wrong ")
