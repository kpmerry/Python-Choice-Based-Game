# Module for scene functions.

def game_intro():
    # Intro sequence.
    game_name = "Python Game"
    print(f"Welcome to {game_name}!")
    print("This is a game of choice.")
    print("You will be prompted when a choice needs to be made.")
    # Get player data.
    name = input("What is your name, Player?")
    start_hp = 50
    player = (name, start_hp)
    # Use name.
    print(f"Well, {name}, we hope you can solve the mystery!")
    # Return player as an output.
    return player

def scene1():
    print("The year is 1924.")
    print("You have been invited to the party of the year.")
    return
