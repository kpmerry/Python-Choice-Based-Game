import time     # Will use to break up multiple print statements.
import random

class Person:
    # Set attributes.
    def __init__(self, name, health):
        self.name = name
        self.health = health
    # Set string representation.
    def __str__(self):
        return (f"{self.name}: {self.health}hp")

def game_intro():
    # Intro sequence.
    game_name = "Python Game"
    print(f"Welcome to {game_name}!")
    print("This is a game of choice.")
    print("You will be prompted when a choice needs to be made.")
    # Get player data.
    name = input("What is your name, Player?")
    start_hp = 50
    player = Person(name, start_hp)
    # Use name.
    print(f"Well, {player.name}, we hope you can solve the mystery!")
    # Return player as an output.
    return player

def scene1():
    print("The year is 1924.")
    print("You have been invited to the party of the year.")
    return

# Gameplay in the following section.

# Introduction to game and set player.
player = game_intro()

# Scene 1 with setting.
scene1()