from PyInquirer import prompt
from item import Item
from player import Player
from room import Room
from colorama import Fore
import os

# Declare all the rooms

'''
outside     : rock - (a large stone made from basalt),
              paper - (sheet of paper made of papyrus),
              scissors - (a marvelous new piece of technology)
foyer       : gold - (some money for your pocket),
              helmet - (Something to protect your head),
              shield - (Something to protect your body)
overlook    : skull - (Some dead guys skull),
              raw beef hide - (Hide from cow),
              bow - (A violin bow, probably not what you were thinking)
narrow      : sword - (A large iron sword),
              arrow - (This one looks as if it had been logged in the knee of an adventurer),
              leather pants - (Chapped, assless leather pants)
treasure    : goblet - (An empty goblit that smells like garlic)
'''


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [
                         Item("Rock", "A large stone made from basalt."),
                         Item("Paper", "A sheet of paper made of papyrus."),
                         Item("Scissors", "A marvelous new piece of technology.")]),

    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east.", [
        Item("Gold", "Some money for your pocket"),
        Item("Helmet", "Something to protect your head from further damage."),
        Item("Shield", "Something to protect your body.")]),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.", [
        Item("Skull", "Some deaf guy's skull."),
        Item("Hide", "Hide from a Cow."),
        Item("Bow", "A violin bow. Probably not what you were thinking")]),

    'narrow': Room("Narrow Passage",
                   "The narrow passage bends here from west to north. The smell of gold permeates the air.", [
                       Item("Sword", "A large iron sword."),
                       Item(
                           "Arrow", "This one looks as if it had been logged in the knee of an adventurer..."),
                       Item("Leather Pants", "Chapped, assless, leather pants.")]),
    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.", [Item("Goblet", "An empty goblet that smells like garlic.")]),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.  # Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


player = Player(room['outside'])
command = ""

# print(player.get_current_room())


def clear(): return os.system('clear')


clear()

print(player.get_current_room())

'''
    split the command
    see if it has 1 or 2 arguments
    if 1 it's a direction command
    if 2 it's a command to pick up items
'''

init_direction = [
    {
        "type": "list",
        "name": "direction",
        "message": "Which direction would you like to go?",
        "choices": ["Go north", "Go south", "Go east", "Go west", "Grab item", "Quit"]
    }
]

inv_direction = [
    {
        "type": "list",
        "name": "direction",
        "message": "Which direction would you like to go?",
        "choices": ["Go north", "Go south", "Go east", "Go west", "Grab item", "Drop item", "Quit"]
    }
]

while not command == "Quit":

    if not player.get_items():
        command = prompt(init_direction)
    else:
        command = prompt(inv_direction)

    if command["direction"] == "Go north":
        player.move_n()
        print(player)

    elif command["direction"] == "Go south":
        player.move_s()
        print(player)

    elif command["direction"] == "Go east":
        player.move_e()
        print(player)

    elif command["direction"] == "Go west":
        player.move_w()
        print(player)

    elif command["direction"] == "Quit":
        print("Thanks for playing! 🎮")
        command = "Quit"

    elif command["direction"] == "Grab item":
        room_items = player.get_current_room().get_items()

        choice_arr = []

        for i in range(len(room_items)):
            choice_arr.append({"name": f"{room_items[i].name}"})

        picked_up = prompt({
            "type": "checkbox",
            "name": "item",
            "message": "Which item(s) would you like to pick up?",
            "choices": choice_arr
        })['item']

        player_inv = []

        for i, item in enumerate(room_items):
            for inv in picked_up:
                if item.name == inv:
                    grabbed_item = player.grab_item(i)
                    player_inv.append(grabbed_item.name)

                    print(Fore.LIGHTGREEN_EX +
                          f"Player grabbed the {grabbed_item.name}.")

        t = 0
        for item in player.get_items():
            gone = player.get_current_room().remove_item(item)
            print(
                Fore.RED + f"The {gone.name} was removed from the room.")

    elif command["direction"] == "Drop item":
        room_items = player.get_items()

        choice_arr = []

        for i in range(len(room_items)):
            choice_arr.append({"name": f"{room_items[i].name}"})

        dropped_items = prompt({
            "type": "checkbox",
            "name": "item",
            "message": "Which item(s) would you like to pick up?",
            "choices": choice_arr
        })['item']

        for index, item in enumerate(room_items):
            for inv in dropped_items:
                if item.name == inv:
                    dropped_item = player.drop_item(index)
                    print(
                        Fore.RED + f"Player dropped the {dropped_item.name}.")

    elif command["direction"] == "Quit":
        print("Thanks for playing! 🎮")
        command = "Quit"

    else:
        print(command)
        print("Not a valid command. 🤷‍")
