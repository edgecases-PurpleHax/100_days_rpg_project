from bin.game_packages.states import *
from bin.game_packages.factories import *


def test_character_stats():
    test_char = Character(name='Test Char', strength=100, health=100)
    assert test_char.name == 'Test Char'
    assert test_char.health == 100
    assert test_char.strength == 100
    assert test_char.alive == True


def test_char_functions():
    test_char = Character(name="Test Char", strength=100, health=100)
    test_char.take_damage(10)
    assert test_char.health == 90
    test_char.heal(20)
    assert test_char.health == 100
    assert test_char.heal(20) == "You are already at full health"
    assert test_char.check_alive() == True
    test_char.take_damage(100)
    assert test_char.alive == False


def test_char_outputs():
    test_char = Character(name="Test Char", strength=100, health=100)
    assert test_char.show_stats() == f"Name: {test_char.name}\r\nStrength: {test_char.strength}\r\nHealth: {test_char.health}"


def test_char_input():
    name = input("What is your name? \r\n")
    test_char = Character(name=name, strength=100, health=100)
    print(test_char.name)
    assert test_char.name == name


def test_player_stats():
    test_player = Player(name='Test Player', major_type="Soldier", minor_type="Charismatic")
    assert test_player.alive == True
    assert test_player.health == 100
    assert test_player.intelligence == 30
    assert test_player.stealth == 30
    assert test_player.strength == 50
    assert test_player.charisma == 50
    assert test_player.endurance == 30
    assert test_player.agility == 30


def test_player_functions():
    test_player = Player(name='Test Player', major_type="Soldier", minor_type="Charismatic")
    assert test_player.check_alive() == True
    test_player.take_damage(10)
    assert test_player.health == 90
    test_player.study(100)
    assert test_player.intelligence == 100
    test_player.study(-100)
    assert test_player.intelligence == 0


def test_player_output():
    test_player = Player(name='Test Player', major_type="Soldier", minor_type="Charismatic")
    assert test_player.show_stats() == f"Name: {test_player.name}\r\nStrength: {test_player.strength}\r\nHealth: {test_player.health}"
    assert test_player.display_character_stats() == f"Name: {test_player.name}\r\nStrength: {test_player.strength}\r\n" \
                                                    f"Health: {test_player.health}\r\n" \
                                                    f"Intelligence: {test_player.intelligence}\r\n" \
                                                    f"Stealth: {test_player.stealth}\r\n" \
                                                    f"Charisma: {test_player.charisma}"


def test_player_input():
    name = input("What is your name? \r\n")
    test_player = Player(name=name, major_type="Soldier", minor_type="Charismatic")
    print(test_player.name)
    assert test_player.name == name


def test_factory_name_factory():
    name = NameFactory('male')
    name2 = NameFactory('female')
    name3 = NameFactory('any')
    assert name.name != None
    assert name2.name != None
    assert name3.name != None
    assert type(name.name) == str
    assert type(name2.name) == str
    assert type(name3.name) == str


def test_game_creation():
    game = Game()
    assert game.player.name
    assert game.armorer
    assert game.librarian
    assert game.spellseller
    assert game.missionnpc1
    assert game.missionnpc2
    assert game.missionnpc3
    assert game.missionnpc4
    assert game.missionnpc5


def test_save_and_load():
    game_to_save = Game()
    print(f"Use {game_to_save.player.name}_save for test file to open")
    game_to_save.save_game()
    game_to_load = game_to_save.load_game()
    assert game_to_load.player.name == game_to_save.player.name
    assert game_to_load.player.health == game_to_save.player.health
    assert game_to_load.player.strength == game_to_save.player.strength
    assert game_to_load.player.stealth == game_to_save.player.stealth
    assert game_to_load.player.intelligence == game_to_save.player.intelligence
    assert game_to_load.player.charisma == game_to_save.player.charisma
    assert game_to_load.armorer.name == game_to_save.armorer.name
    assert game_to_load.librarian.name == game_to_save.librarian.name
    assert game_to_load.spellseller.name == game_to_save.spellseller.name
    assert game_to_load.missionnpc1.name == game_to_save.missionnpc1.name
    assert game_to_load.missionnpc2.name == game_to_save.missionnpc2.name
    assert game_to_load.missionnpc3.name == game_to_save.missionnpc3.name
    assert game_to_load.missionnpc4.name == game_to_save.missionnpc4.name
    assert game_to_load.missionnpc5.name == game_to_save.missionnpc5.name


def test_player_soldier_charismatic():
    test = Player(name=NameFactory('any'), major_type="Soldier", minor_type="Charismatic")
    assert test.strength == 50
    assert test.stealth == 30
    assert test.intelligence == 30
    assert test.charisma == 50
    assert test.agility == 30
    assert test.endurance == 30


def test_player_soldier_agile():
    test = Player(name=NameFactory('any'), major_type="Soldier", minor_type="Agile")
    assert test.strength == 50
    assert test.stealth == 30
    assert test.intelligence == 30
    assert test.charisma == 30
    assert test.agility == 50
    assert test.endurance == 30


def test_player_soldier_endurance():
    test = Player(name=NameFactory('any'), major_type="Soldier", minor_type="Endurance")
    assert test.strength == 50
    assert test.stealth == 30
    assert test.intelligence == 30
    assert test.charisma == 30
    assert test.agility == 30
    assert test.endurance == 50


def test_player_traveller_charismatic():
    test = Player(name=NameFactory('any'), major_type="Traveller", minor_type="Charismatic")
    assert test.strength == 30
    assert test.stealth == 30
    assert test.intelligence == 50
    assert test.charisma == 50
    assert test.agility == 30
    assert test.endurance == 30


def test_player_traveller_agile():
    test = Player(name=NameFactory('any'), major_type="Traveller", minor_type="Agile")
    assert test.strength == 30
    assert test.stealth == 30
    assert test.intelligence == 50
    assert test.charisma == 30
    assert test.agility == 50
    assert test.endurance == 30


def test_player_traverller_endurance():
    test = Player(name=NameFactory('any'), major_type="Traveller", minor_type="Endurance")
    assert test.strength == 30
    assert test.stealth == 30
    assert test.intelligence == 50
    assert test.charisma == 30
    assert test.agility == 30
    assert test.endurance == 50


def test_player_assassin_charismatic():
    test = Player(name=NameFactory('any'), major_type="Assassin", minor_type="Charismatic")
    assert test.strength == 30
    assert test.stealth == 50
    assert test.intelligence == 30
    assert test.charisma == 50
    assert test.agility == 30
    assert test.endurance == 30


def test_player_assassin_agile():
    test = Player(name=NameFactory('any'), major_type="Assassin", minor_type="Agile")
    assert test.strength == 30
    assert test.stealth == 50
    assert test.intelligence == 30
    assert test.charisma == 30
    assert test.agility == 50
    assert test.endurance == 30


def test_player_assassin_endurance():
    test = Player(name=NameFactory('any'), major_type="Assassin", minor_type="Endurance")
    assert test.strength == 30
    assert test.stealth == 50
    assert test.intelligence == 30
    assert test.charisma == 30
    assert test.agility == 30
    assert test.endurance == 50
