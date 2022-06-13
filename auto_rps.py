## Creating the Rock, Paper and Scissors game with two functions 
## one to get the computer's choice and the other for the user to input 

import random 
import model

def get_computer_choice():
    list = ['Rock', 'Paper', 'Scissors']
    return random.choice(list)

def get_user_choice():
    choice = model.camera_rps.get_prediction(model.prediction)
    return choice



def get_winner(computer_choice, user_choice):    
    ## A dictionary that denotes the hierarchy of the options..eg. beats['Scissors'] will equal 'Rock',
    ## as Rock beats scissors
    beats = {
    'Scissors': 'Rock',
    'Rock': 'Paper',
    'Paper': 'Scissors',
    }
    
    ## Ref. for the logic in the if-elif-else loop from
    ## https://codereview.stackexchange.com/questions/43024/use-if-else-elif-conditionals-to-write-a-basic-rock-paper-scissors-game#comment74280_43024
    if computer_choice == user_choice:
        print("Draw!! \n Try Again!!")
        play()
    elif (computer_choice == beats[user_choice]):
        print("Computer wins!!")
    elif (user_choice == beats[computer_choice]):
        print ("You win.")
    else:
        print("Error!")

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice, user_choice)

play()