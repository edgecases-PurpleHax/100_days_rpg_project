# restart project
import sys
from bin.game_packages.characters import Character, Player, NPC, Enemy
from bin.game_packages.inventory_items import Weapon


if __name__ == "__main__":
    print("Some story here, some story there. Now create a character.")
    player = Player()
    print(f"Time to talk to the player. Your name is {player.player_name}")
    print('Lets test out some weapon adding')
    first_weapon = Weapon(health=100, name="basic dagger", damage=3)
    player.gain_inventory(first_weapon)
    print(player.player_inventory)
    player.equip_weapon(first_weapon)
    print("Oh shit. You are getting attacked")
    print(player.player_inventory)
    first_enemy = Enemy(health=100, name="Test Dummy", damage=2)
    result = player.combat(enemy=first_enemy)
    if result == "You have died":
        print(result)
        print("Game Over")
        sys.exit()
    else:
        print(result)
    print("And the game continues. ")