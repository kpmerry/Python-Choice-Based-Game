import scenes   # Scene functions.
import char     # Character information.

class Player(char.Character):

    def __init__(self, name, health):
        super().__init__(name)
        self.health = 50
    
    # Set string representation.
    def __str__(self):
        return (f"{self.name}: {self.health}hp")
    
    def assign_player(info):
        return Player(info[0],info[1])

# Gameplay in the following section.

# Introduction to game and set player.
player_info = scenes.game_intro()
player = Player.assign_player(player_info)

# Scene 1 with setting.
scenes.scene1()

# == For testing purposes ==
scenes.scene2()