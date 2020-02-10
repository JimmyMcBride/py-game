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
        player_string = Fore.GREEN + \
            f"Current Room: {self.current_room}\n\n" + \
            Fore.LIGHTRED_EX + "Held Items:\n" + Fore.RESET

        i = 1
        for item in self.items:
            player_string += f"Item {i}: " + \
                Fore.YELLOW + f"{item}\n" + Fore.RESET
            i += 1

        return player_string

    def get_current_room(self):
        return self.current_room

    def get_items(self):
        return self.items

    def move_n(self):
        if hasattr(self.current_room, 'n_to'):
            self.current_room = self.current_room.n_to
            return Fore.GREEN + f"Player has moved to the {self.current_room.name}"
        else:
            return Fore.RED + "You went nowhere dummy! 🤣"

    def move_s(self):
        if hasattr(self.current_room, 's_to'):
            self.current_room = self.current_room.s_to
            return Fore.GREEN + f"Player has moved to the {self.current_room.s_to.name}"
        else:
            return Fore.RED + "You went nowhere dummy! 🤣"

    def move_e(self):
        if hasattr(self.current_room, 'e_to'):
            self.current_room = self.current_room.e_to
            return Fore.GREEN + f"Player has moved to the {self.current_room.name}"
        else:
            return Fore.RED + "You went nowhere dummy! 🤣"

    def move_w(self):
        if hasattr(self.current_room, 'w_to'):
            self.current_room = self.current_room.w_to
            return Fore.GREEN + f"Player has moved to the {self.current_room.name}"
        else:
            return Fore.RED + "You went nowhere dummy! 🤣"

    def grab_item(self, item_number):
        grabbed_item = self.current_room.get_items()[item_number]
        self.items.append(grabbed_item)
        return grabbed_item

    def drop_item(self, item):
        self.items.remove(item)
        return item

    def found_treasure(self):
        return self.current_room.name == "Treasure Chamber"
