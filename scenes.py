# Module for scene functions.
import time
import char     # Imports character info.
import os       # For finding file directories.

# == TO ADD: some kind of scene change function ==
# == TO ADD: a choice text file to improve readability ==
# == TO FINISH: recognising dialogue and variables function ==

def get_filepath(filename):
    """Returns the filepath for Game Dialogue file."""
    # Get the directory of the current script
    current_dir = os.path.dirname(__file__)
    # Construct the path to the text file
    file_path = os.path.join(current_dir, "Game Dialogue", filename)
    return file_path

def t_print(text: list[str]):
    """Print list of game dialogue strings with a delay."""
    # Set game dialogue pace.
    speed = 0.5
    for s in text:
        print(s)
        time.sleep(speed)
    return

def input_choice(op1, op2, op3):
    """Returns a valid choice from 3 options."""

    # List options and create input variable.
    t_print([op1, op2, op3])
    choice = input("Choose an option: (1/2/3)")

    # Check for valid input reponse.
    valid_choices = ["1", "2", "3"]

    if choice not in valid_choices:
        # If invalid input, reprompt and recurse.
        print("Enter a valid reponse.")
        return input_choice(op1, op2, op3)

    # If input passes check, return it.
    return choice

def speak(char, dialogue = str):
    """Prints character name and dialogue."""
    return t_print([f"{char.name}: '{dialogue}'"])

def extract_dialogue(line):
    # == TO ADD: recognise when Variables are called. ==
    index = line.index(":")
    # Separate character name and dialogue.
    char_name = line[:index]
    dialogue = line[(index + 1):]
    try:
        # Check if character name matches an object.
        speak(char.name_index[char_name], dialogue)
    except:
        # If not, skip the line of dialogue.
        None
    return 

def choice1():
    """Function for choice 1."""
    # Prepare player for Choice 1.
    print("Time to make your first choice!")
    # Trigger choice based on options.
    choice1 = input_choice("1. Who are you?", 
                        "2. No, I don't want a drink.", 
                        "3. Thanks a lot! Can I have another?")
    # Generate dialogue based on choice.
    if choice1 == "1":
        speak(char.c2, "I'm one of Big Joe's best, come watch me sing some time.")
    elif choice1 == "2":
        speak(char.c2, "You might not get another chance at such a cheap night!")
        speak(char.c2, "Joe's feeling very generous tonight! Might be that deal with Diego.")
    elif choice1 == "3":
        speak(char.c2,"Alright, then! Luckily Joe's feeling very generous tonight!")
        speak(char.c2, "Might be that deal with Diego.")
    return

def game_intro():
    """Start game introuction and gather player data."""

    # Intro sequence.
    game_name = "Python Game"
    t_print([f"Welcome to {game_name}!", 
            "This is a game of choice.", 
            "You will be prompted when a choice needs to be made."])

    # Get player data.
    name = input("What is your name, Player? ")
    start_hp = 50
    player = (name, start_hp)

    # Use name.
    t_print([f"Well, {name}, we hope you can solve the mystery!"])

    # Return player data as an output.
    return player

def scene1(plyr_name):
    """Runs Scene 1."""

    file_path = get_filepath("Scene1.txt")
    # Print lines in Scene 1 text file.
    with open(file_path, "r") as fin:
        for line in fin:
            # Leaves out lines.
            if line[0] == "#":
                continue
            # Indicates choice sequence.
            elif line[0] == "=":
                choice1()
                continue
            # Indicates dialogue.
            elif line[0] == "$":
                extract_dialogue((line[1:]).strip())
                continue
            t_print([line.strip()])
    
    # Dramatic pause.
    time.sleep(1)
    t_print(["Your Task: Find the murderer."])
    return

def scene2():
    """Details a player's visit to murder scene."""
    file_path = get_filepath("Scene2.txt")
    # Print lines in Scene 1 text file.
    with open(file_path, "r") as fin:
        for line in fin:
            # Check for conditions as specified by `Dialogue.md`.
            # Leaves out lines.
            if line[0] == "#":
                continue
            # Indicates choice sequence.
            elif line[0] == "=":
                choice1()
                continue
            # Indicates dialogue.
            elif line[0] == "$":
                extract_dialogue(line)
            # Print the lines of regular game dialogue.
            t_print([line.strip()])
    return

def scene3():
    return None

def scene4():
    return None

def scene5():
    return None

def scene6():
    return None
