import pickle
from .characters import *
from .factories import *


class Game:
    def __init__(self):
        self.player_info = self.create_player()
        self.player = Player(name=self.player_info[0],major_type=self.player_info[1], minor_type=self.player_info[2])
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

    def create_player(self):
        name=input("What is your name? \r\n")
        mapping = {"majortype": {"1": "Soldier", "2": "Traveller", "3":"Assassin"}, "minortype":{"1":"Charismatic", "2":"Agile", "3":"Endurance"}}
        major_type = input("Would you like to be:\r\n1. Soldier\r\n2. Traveller\r\n3. Assassin")
        minor_type = input("Would you like to be:\r\n1. Charismatic\r\n2. Agile\r\n3. Endurance")
        return [name, mapping["majortype"][major_type], mapping["minortype"][minor_type]]
