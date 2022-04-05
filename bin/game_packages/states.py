import pickle
from .characters import *
from .factories import *


class Game:
    def __init__(self):
        self.player = Player(name=input("What is your name? \r\n"), strength=100, intelligence=100, stealth=100,
                             charisma=100, health=100)
        self.armorer = Armorer(name=NameFactory('any').name)
        self.spellseller = SpellSeller(name=NameFactory('any').name)
        self.librarian = Librarian(name=NameFactory('any').name)
        self.missionnpc1 = MissionNpc(name=NameFactory('any').name, mission_number="1")
        self.missionnpc2 = MissionNpc(name=NameFactory('any').name, mission_number="2")
        self.missionnpc3 = MissionNpc(name=NameFactory('any').name, mission_number="3")
        self.missionnpc4 = MissionNpc(name=NameFactory('any').name, mission_number="4")
        self.missionnpc5 = MissionNpc(name=NameFactory('any').name, mission_number="5")

    def save_game(self):
        pickle.dump(self, open(f'{self.player.name}_save', 'wb'))

    def load_game(self):
        return pickle.load(open(f'{input("Enter Save file to load: ")}', "rb"))

    def startMission(self, missionNumber):
        with open('missions.json') as f:
            missions = json.load(f)
            return missions[missionNumber]
