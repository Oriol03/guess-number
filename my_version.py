from random import randint
from art import logo
import os

EASY_LEVEL_REPEAT= 10
HARD_LEVEL_REPEAT =5

def compare(pc_n ,player_n):
    if pc_n==player_n:
        print(f"Congratulation ,you guess the right number {pc_n}")
        
    elif player_n< pc_n:
        print("Too low ")
         
    elif player_n> pc_n :
        print("Too high ")
         

def play_session (repeat):
    player_n=0
    
    while player_n !=pc_number and repeat > 0 :
               
        print(f"You have {repeat} attempts remaining to guess the number  ")
        player_n= int(input("Make a guess :  "))
        compare(pc_number,player_n)
        repeat-=1
        
    if repeat==0 :
        print("You have run out of guesses, you lose ")
def game ():
    print(logo)
    
    print("Welcomme to Number Guessing Game ")
    print("I\' m thinking of a number between 1 and 100 ")
    level=input("Choose a level. Type \"easy\" or \"hard\" :   ").lower()
    if level=='hard':
        play_session(HARD_LEVEL_REPEAT)
    else :
        play_session(EASY_LEVEL_REPEAT)

    print(f"The right number is {pc_number} ") 

while input("Type \'y\' to replay or \'n\' to stop ").lower()== "y" :
    os.system("cls")
    pc_number=randint(1,100)
    game()
