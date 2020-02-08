# Write a class to hold player information, e.g. what room they are in
# currently in

from room import Room
from item import Item
from colorama import Fore

class Player:
    def __init__(self, current_room, items=[]):
        self.current_room = current_room
        self.items = items

    def __str__(self):
        player_string = Fore.RED + f"Current Room: {self.current_room}\n\n" + Fore.LIGHTRED_EX + "Held Items:\n" + Fore.RESET

        i = 1
        for item in self.items:
            player_string += f"Item {i}: {item}\n"
            i += 1

        return player_string

    def get_current_room(self):
        return self.current_room

    def get_items(self):
        return self.items

    def move_n(self):
        if hasattr(self.current_room, 'n_to'):
            self.current_room = self.current_room.n_to
        else:
            print("You went nowhere, dummy.\n")

    def move_s(self):
        if hasattr(self.current_room, 's_to'):
            self.current_room = self.current_room.s_to
        else:
            print("You went nowhere, dummy.\n")

    def move_e(self):
        if hasattr(self.current_room, 'e_to'):
            self.current_room = self.current_room.e_to
        else:
            print("You went nowhere, dummy.\n")

    def move_w(self):
        if hasattr(self.current_room, 'w_to'):
            self.current_room = self.current_room.w_to
        else:
            print("You went nowhere, dummy.\n")

    def grab_item(self, item_number):
        grabbed_item = self.current_room.get_items()[item_number - 1]
        self.items.append(grabbed_item)
        return grabbed_item

    def drop_item(self, item_number):
        dropped_item = self.items[item_number - 1]
        del self.items[item_number - 1]
        return dropped_item

    def found_treasure(self):
        return self.current_room.name == "Treasure Chamber"
