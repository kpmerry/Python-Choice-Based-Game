# Module for scene functions.

import time
import char

def dialogue(character, dialogue):
    return None

def input_choice(choices: tuple[str]):
    return None

def t_print(text: str):
    speed = 0.8
    print(text)
    time.sleep(speed)
    return

def game_intro():

    # Intro sequence.
    game_name = "Python Game"
    t_print(f"Welcome to {game_name}!")
    t_print("This is a game of choice.")
    t_print("You will be prompted when a choice needs to be made.")

    # Get player data.
    name = input("What is your name, Player? ")
    start_hp = 50
    player = (name, start_hp)

    # Use name.
    t_print(f"Well, {name}, we hope you can solve the mystery!")

    # Return player data as an output.
    return player

def scene1():

    # Scene setting.
    t_print("The year is 1924.")
    t_print("You have been invited to the party of the year.")
    
    return

def scene2():
    """Details a players visit to murder scene."""

    # Scene setting.
    # May need separate dialogue file for bulkier scenes.
    t_print("You approach the scene.")
    t_print("The cold night air whips around you.")

    return

def scene3():
    return None

def scene4():
    return None

def scene5():
    return None

def scene6():
    return None