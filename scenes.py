# Module for scene functions.
import time
import char     # Imports character info.

# == TO ADD: some kind of scene change function ==
# == FIX READABIITY: for scene game dialogue ==

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
    """Start opening scene."""

    # Scene setting.
    t_print(["The year is 1924.", 
        "You have been invited to the party of the year.", 
        "A red-faced man in a bowler hat approaches."])
    speak(char.c1, f"Hi {plyr_name}, I'm glad you could make it!")
    t_print(["He leads you to a door around the side."])
    speak(char.c1, "Welcome to Big Joe's.")
    t_print(["The door opens to reveal a glamourous club.", 
        "There are dancing ladies and long counters with many glasses.",
        "The cigar smoke hangs thick in the air."])
    speak(char.c1, "For a famous author like yourself, it's on the house!")
    speak(char.c2, "Here, take this drink.")

    choice1()

    t_print(["A man stumbles into you and slurs incoherently.",
            "He slips into the crowd before you can confront him."])
    speak(char.c2, "That's Clint. Don't mind him, just stay out of his way.")
    speak(char.c6, "He's harmless. Just can't handle the drink.")
    speak(char.c2, f"Fletch! I thought you'd be working tonight.")
    t_print(["Fletcher nods his head in your direction. Missy grabs onto his arm."])
    speak(char.c2, "Fletch works with Missy McLeary. Big Joe isn't a fan of her.")
    speak(char.c6, "Mhm.")
    speak(char.c2, "Strange that Missy didn't show up. She usually likes to scout the competition.")
    
    # More dialogue here
    
    t_print(["Suddenly the music cuts out.",
            "Big Joe appears on stage with a strange expression."])
    speak(char.c1, "I've just received a message.")
    t_print(["Everyone is silent, confused and anxious."])
    speak(char.c1, "Diego is dead. He's been murdered.")

    time.sleep(1)
    t_print(["Your Task: Find the murderer."])
    return

def scene2():
    """Details a player's visit to murder scene."""
    # Scene setting.
    t_print(["You approach the scene.", "The cold night air whips around you."])

    return

def scene3():
    return None

def scene4():
    return None

def scene5():
    return None

def scene6():
    return None