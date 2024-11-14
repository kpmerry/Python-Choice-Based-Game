# Module for Characters

class Char:

    def __init__(self, name):
        self.name = name

    def speak(self, dialogue = str):
        return print(f"{self.name}: '{dialogue}'")

c0 = Char("Diego Deadman")
c1 = Char("Big Joe")
c2 = Char("Lisa Larson")
c3 = Char("Clint Carding")
c4 = Char("Missy McLeary")
c5 = Char("Reese Riesling")
c6 = Char("Fletcher Finnegan")