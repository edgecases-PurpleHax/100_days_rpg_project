import pytest
from characters.characters import *
from factories.factories import NameFactory


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
    name = input("What is your name")
    test_char = Character(name=name, strength=100, health=100)
    print(test_char.name)
    assert test_char.name == name


def test_player_stats():
    test_player = Player(name='Test Player', strength=100, intelligence=100, health=100, charisma=100, stealth=100)
    assert test_player.alive == True
    assert test_player.health == 100
    assert test_player.intelligence == 100
    assert test_player.stealth == 100
    assert test_player.strength == 100
    assert test_player.charisma == 100


def test_player_functions():
    test_player = Player(name='Test Player', strength=100, intelligence=100, health=100, charisma=100, stealth=100)
    assert test_player.check_alive() == True
    test_player.take_damage(10)
    assert test_player.health == 90
    test_player.study(100)
    assert test_player.intelligence == 100
    test_player.study(-100)
    assert test_player.intelligence == 0


def test_player_output():
    test_player = Player(name='Test Player', strength=100, intelligence=100, health=100, charisma=100, stealth=100)
    assert test_player.show_stats() == f"Name: {test_player.name}\r\nStrength: {test_player.strength}\r\nHealth: {test_player.health}"
    assert test_player.display_character_stats() == f"Name: {test_player.name}\r\nStrength: {test_player.strength}\r\n" \
                                                    f"Health: {test_player.health}\r\n" \
                                                    f"Intelligence: {test_player.intelligence}\r\n" \
                                                    f"Stealth: {test_player.stealth}\r\n" \
                                                    f"Charisma: {test_player.charisma}"


def test_player_input():
    name = input("What is your name")
    test_player = Player(name=name, strength=100, intelligence=100, health=100, charisma=100, stealth=100)
    print(test_player.name)
    assert test_player.name == name


def test_factory_NameFactory():
    name = NameFactory('male')
    name2 = NameFactory('female')
    name3 = NameFactory('any')
    assert name.name != None
    assert name2.name != None
    assert name3.name != None
    assert type(name.name) == str
    assert type(name2.name) == str
    assert type(name3.name) == str
