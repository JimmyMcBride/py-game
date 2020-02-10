class Character:
    def __init__(self, name, max_health, current_health, attack, defence):
        self.name = name
        self.max_health = max_health
        self.current_health = current_health
        self.attack = attack
        self.defence = defence

    def take_damage(self, damage):
        final_damage = damage - self.defence
        self.current_health = self.current_health - final_damage
        return f"The player took {final_damage} points of damage and is at {self.current_health} hp."

    def heal(self, hp_points):
        healed = self.current_health + hp_points
        if healed > self.max_health:
            self.current_health = self.max_health
        else:
            self.current_health = healed
        return f"Player healed for {hp_points} points and is at {self.current_health} hp."


hero = Character('Hero', 200, 200, 30, 10)

attack = hero.take_damage(30)
potion = hero.heal(18)

# print(f'{hero.current_health}')
print(f'{attack}')
print(f'{potion}')
