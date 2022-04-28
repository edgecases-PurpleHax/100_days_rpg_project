#! /usr/bin/python3
# 100 Days of Code Challenge
from game_packages.states import Game
test = Game()
mission_list = test.startMission("0")
for i in mission_list['StoryLine'].keys():
    print(test.mission_loops(i, mission_list))

