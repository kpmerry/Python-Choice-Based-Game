# Module for Characters

class Character:

    def __init__(self, name):
        self.name = name

    def say_dialogue(self, dialogue = str):
        return print(f"{self.name}: '{dialogue}'")

c0 = Character("Diego Deadman")
c1 = Character("Big Joe")
c2 = Character("Lisa Larson")
c3 = Character("Clint Carding")
c4 = Character("Missy McLeary")
c5 = Character("Reese Riesling")
c6 = Character("Fletcher Finnegan")