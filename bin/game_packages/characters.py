import json
import random


class Character:
    def __init__(self, name, strength, health):
        self.name = name
        self.strength = strength
        self.health = health
        self.alive = True

    def show_stats(self):
        return f'Name: {self.name}\r\nStrength: {self.strength}\r\nHealth: {self.health}'

    def take_damage(self, damage):
        if self.health - damage > 0:
            self.health = self.health - damage
        else:
            self.health = 0
            self.alive = False
        self.check_alive()

    def heal(self, healing_amount):
        if self.health == 100:
            return "You are already at full health"
        elif self.health + healing_amount >= 100:
            self.health = 100
        else:
            self.health = self.health + healing_amount

    def check_alive(self):
        if not self.alive:
            return f"{self.name} has died"
        else:
            return True


class Player(Character):
    def __init__(self, name, strength, health, intelligence, stealth, charisma):
        super().__init__(name, strength, health)
        self.stealth = stealth
        self.intelligence = intelligence
        self.charisma = charisma

    def study(self, intelligence_gain):
        if self.intelligence + intelligence_gain >= 100:
            self.intelligence = 100
        else:
            self.intelligence = self.intelligence + intelligence_gain

    def display_character_stats(self):
        main_stats = self.show_stats()
        additional_stats = main_stats + f'\r\nIntelligence: {self.intelligence}\r\n' \
                                        f'Stealth: {self.stealth}\r\n' \
                                        f'Charisma: {self.charisma}'
        return additional_stats


class Npc(Character):
    def __init__(self, name):
        super().__init__(name=name, strength=0, health=100)

    def speech(self, npctype, selection):
        with open('dialog.json', 'r') as f:
            dialoge = json.load(f)
        return dialoge[npctype][selection]


class Armorer(Npc):
    def __init__(self, name):
        super().__init__(name=name)
        self.menu = []


class SpellSeller(Npc):
    def __init__(self, name):
        super().__init__(name=name)
        self.menu = []


class Librarian(Npc):
    def __init__(self, name):
        super().__init__(name=name)


class MissionNpc(Npc):
    def __init__(self, name, mission_number):
        super().__init__(name=name)
        with open('missions.json', 'r') as f:
            self.mission_list = json.load(f)
        self.mission = self.mission_list[mission_number]
