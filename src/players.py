import random
import time

"""Contains information on player attributes."""

class Player:
    """Describes a basic player."""
    def __init__(self, name, level, health, will, strength):
        """Initializes stats"""
        self.name = name
        self.level = level
        self.health = health
        self.full_health = health
        self.will = will
        self.full_will = will
        self.strength = strength

    def default_attack(self, enemy):
        """Normal attack that damages enemy target."""
        damage = 0
        if random.randint(1, 100) <= 95:
            damage = (self.level * 2)
            critical_hit = random.randint(1,10)
            if critical_hit == 1:
                damage += int(self.level)
                print("Critical hit!")
        enemy.health -= damage
        print("The enemy took " + str(damage) + " damage.")

class MainPlayer(Player):
    """The user's avatar."""
    def __init__(self, name, level, health, will, strength):
        Player.__init__(self, name, level, health, will, strength)
        self.wealth = 100
        self.inventory = []
        self.status = []

    def use_item(self, item):
        if item not in self.inventory:
            print(f"{item} is not in your inventory!")
            return
        self.inventory.remove(item)

    def snipe(self, enemy):
        """Deals damage based on strength, 20% chance of missing."""
        if self.will >= 4:
            self.will -= 4
            probability = random.randint(1, 100)
            if probability <= 20:
                print("You missed!")
                damage = 0
            else:
                damage = self.strength * 1.5
            enemy.health -= damage
            print("The enemy took " + str(damage) + " damage.")
        else:
            print("Not enough will!")



class Enemy:
    """Describes common enemy."""
    def __init__(self, level, health, magic):
        """Initializes stats"""
        self.level = level
        self.health = health
        self.full_health = health
        self.magic = magic
        self.full_magic = magic

    def default_attack(self, player):
        """Normal attack that damages protagonist target."""
        chance_to_hit = random.randint(1,100)
        damage = 0
        if chance_to_hit <= 90:
            damage = (self.level * 2)
            if chance_to_hit <= 10:
                damage += int(self.level * 0.5)
        player.health -= damage
        print(player.name + " took " + str(damage) + " damage.")

# Spawn enemies
def spawn_enemy(level):
    if level == "easy":
        level = random.randint(1,5)
        health = int(level * 5)
        magic = int(level * 2)
        enemy = {"level": level,"health": health,"magic": magic}
        return enemy
    elif level == "medium":
        level = random.randint(6, 10)
        health = int(level * 5)
        magic = int(level * 2)
        enemy = {"level": level,"health": health,"magic": magic}
        return enemy
    elif level == "hard":
        level = random.randint(11, 15)
        health = int(level * 5)
        magic = int(level * 2)
        enemy = {"level": level,"health": health,"magic": magic}
        return enemy

def start_battle(team, protag_moves, sidekick_moves, string_to_instance):
    chance = random.randint(1,3)
    if chance > 1:
        time.sleep(1)
        Protagonist = team[0]
        Sidekick = team[1]
        print("Encountered an enemy!\n")
        enemy = spawn_enemy("easy")
        minion = Enemy(**enemy)
        print("The enemy level is " + str(minion.level) + ".")
        while Protagonist.health > 0 and minion.health > 0:
            print("The enemy has " + str(minion.health) + " HP left.")
            print(Protagonist.name + " has " + str(Protagonist.health) + " HP left.")
            print(Protagonist.name + " has " + str(Protagonist.will) + " will left.")
            print(Sidekick.name + " has " + str(Sidekick.health) + " HP left.")
            print(Sidekick.name + " has " + str(Sidekick.will) + " will left.\n")
            print()
            time.sleep(1)
            print("What will " + Protagonist.name + " do?")
            print()
            for action in protag_moves:
                print(action)
            print()
            decision = input("You will... ").lower().strip()
            if decision == "attack":
                Protagonist.default_attack(minion)
            elif decision == "snipe":
                Protagonist.snipe(minion)
            elif decision == "heal all":
                Protagonist.healall(team)
            print()
            time.sleep(1)

            if Protagonist.health > 0 and minion.health > 0:
                print("What will " + Sidekick.name + " do?")
                print()
                for action in sidekick_moves:
                    print(action)
                print()
                decision = input(Sidekick.name + " will... ").lower().strip()
                if decision == "attack":
                    Sidekick.default_attack(minion)
                elif decision == "heal":
                    for i in team:
                        print(i.name)
                    heal = input("Heal who? ")
                    Sidekick.heal(heal, string_to_instance)
                print()
                time.sleep(1)

            if Protagonist.health > 0 and minion.health > 0:
                print("The enemy attacks!")
                chance = random.randint(1,2)
                if chance == 1:
                    person = Sidekick
                elif chance == 2:
                    person = Protagonist
                minion.default_attack(person)
                print()
                time.sleep(1)

        else:
            print("Enemy defeated!")
            print()


    else:
        print("You didn't encounter any enemies.")
