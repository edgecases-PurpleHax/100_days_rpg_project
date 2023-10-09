# restart project
from bin.game_packages.inventory_items import Weapon
class Character:

    def take_damage(self, health, damage):
        return health - damage


class Player(Character):
    def __init__(self):
        self.player_name = input("Please enter your name: \r\n")
        self.player_health = 100
        self.player_armor = 0
        self.player_inventory = [Weapon(100, "hands", 5)]

    def gain_inventory(self, item):
        self.player_inventory.append(item)

    def equip_weapon(self, item):
        if item in self.player_inventory:
            self.player_inventory.remove(item)
        self.player_inventory[0] = item

    def combat(self, enemy):
        while self.player_health > 0:
            if enemy.health < 0:
                enemy.health = 0
            if enemy.health > 0:
                self.player_health = self.take_damage(health=self.player_health, damage=enemy.damage - self.player_armor * enemy.damage)
                enemy.health = enemy.take_damage(health=enemy.health, damage=self.player_inventory[0].damage)
            else:
                return "You killed the enemy."
        return "You have died"


class NPC(Character):

    def __init__(self):
        pass


class Enemy(Character):

    def __init__(self, health, name, damage):
        self.health = health
        self.name = name
        self.damage = damage
