import time
class Person:
    def __init__(self, name, health):
        self.health = health

def game_intro():
    print(f"Welcome to {game_name}!")
    
    name = input("What is your name, Player?")
    start_hp = 50
    player = Person(name, start_hp)
    
    pirnt(f"Well, {player.name}, we hope you can solve the mystery!")
    return
