# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item
from colorama import Fore


class Room:
    def __init__(self, name, message, items=[]):
        self.name = name
        self.message = message
        self.items = items

    def __str__(self):
        room_string = Fore.BLUE + f"{self.name},\n" + Fore.LIGHTCYAN_EX + \
            f"{self.message}\n\n" + Fore.MAGENTA + \
            "Visible items:\n" + Fore.RESET

        i = 1
        for item in self.items:
            room_string += f"Item {i}: " + \
                Fore.YELLOW + f"{item}\n" + Fore.RESET
            i += 1

        return room_string

    def get_items(self):
        return self.items

    def add_item(self, item_number):
        grabbed_item = self[item_number]
        self.items.append(grabbed_item)
        return grabbed_item

    def remove_item(self, item_number):
        dropped_item = self.items[item_number]
        del self.items[item_number]
        return dropped_item
