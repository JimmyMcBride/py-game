class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}, Description: {self.description}"

    def get_item_name(self):
        return f"{self.name}"