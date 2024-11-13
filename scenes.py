# Module for scene functions.

import time

def dialogue(character, dialogue):
    return None

def slow_print(text):
    speed = 0.5
    print(text)
    time.sleep(speed)
    return

def game_intro():

    # Intro sequence.
    game_name = "Python Game"
    slow_print(f"Welcome to {game_name}!")
    slow_print("This is a game of choice.")
    slow_print("You will be prompted when a choice needs to be made.")

    # Get player data.
    name = input("What is your name, Player? ")
    start_hp = 50
    player = (name, start_hp)

    # Use name.
    slow_print(f"Well, {name}, we hope you can solve the mystery!")

    # Return player data as an output.
    return player

def scene1():

    # Scene setting.
    slow_print("The year is 1924.")
    slow_print("You have been invited to the party of the year.")
    
    return

def scene2():

    #Scene setting.
    slow_print("You approach the scene.")

    return