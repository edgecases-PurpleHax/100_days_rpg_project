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
    def __init__(self, name, major_type, minor_type):
        self.major_type = major_type
        self.minor_type = minor_type
        if self.major_type == "Soldier":
            self.health = 100
            self.strength = 50
            self.intelligence = 30
            self.stealth = 30
        elif self.major_type == "Assassin":
            self.health = 100
            self.strength = 30
            self.intelligence = 30
            self.stealth = 50
        elif self.major_type == "Traveller":
            self.health = 100
            self.strength = 30
            self.intelligence = 50
            self.stealth = 30
        if self.minor_type == "Charismatic":
            self.charisma = 50
            self.agility = 30
            self.endurance = 30
        elif self.minor_type == "Agile":
            self.charisma = 30
            self.agility = 50
            self.endurance = 30
        elif self.minor_type == "Endurance":
            self.charisma = 30
            self.agility = 30
            self.endurance = 50
        super().__init__(name, self.strength, self.health)

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

    def intelligence_attack(self):
        return self.strength * (self.intelligence / 100)

    def avoid_attack(self):
        chance = self.strength * (self.charisma/100)
        roll = random.random(1, 20)
        if chance > roll:
            return True
        if chance <= roll:
            return False

    def stealth_attack(self):
        return self.strength * (self.stealth / 100)

    def regular_attack(self, modifier):
        return self.strength


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
        self.menu = []


class MissionNpc(Npc):
    def __init__(self, name, mission_number):
        super().__init__(name=name)
        with open('missions.json', 'r') as f:
            self.mission_list = json.load(f)
        self.mission = self.mission_list[mission_number]


class Enemy(Character):
    def __init__(self, name, strength, level):
        super().__init__(name=name, strength=strength, health=100)
        self.level = level

    def attack(self, level):
        return self.strength * (self.level / 100)


class EnemyType1(Enemy):
    def __init__(self, name, strength, level):
        super().__init__(name=name, strength=strength, level=level)
        self.level = level


class EnemyType2(Enemy):
    def __init__(self, name, strength, level):
        super().__init__(name=name, strength=strength, level=level)


class EnemyType3(Enemy):
    def __init__(self, name, strength, level):
        super().__init__(name=name, strength=strength, level=level)


class EnemyType4(Enemy):
    def __init__(self, name, strength, level):
        super().__init__(name=name, strength=strength, level=level)


class EnemyType5(Enemy):
    def __init__(self, name, strength, level):
        super().__init__(name=name, strength=strength, level=level)
