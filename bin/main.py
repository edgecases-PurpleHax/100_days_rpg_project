#! /usr/bin/python3
# 100 Days of Code Challenge
from characters.characters import *


test_player = Player(name='Test Player', strength=100, intelligence=100, health=100, charisma=100, stealth=100)
print(test_player.display_character_stats())
test_player.take_damage(10)
print(test_player.display_character_stats())


