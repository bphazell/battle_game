import random
import time

# Gladiator class contains the functions and attributes that both Human and Villian subclasses can use


class Gladiator:
    def __init__(self, name, hp, strength, magic):
        self.name = name
        self.max_hp = hp
        self.max_magic = magic
        self.magic = magic
        self.hp = hp
        self.strength = strength
        self.delay = 1
        self.shield = 0
        self.iced_count = 0
        self.elder_wand = 0

    def display_hp(self):
        time.sleep(self.delay)
        print(self.name, "HP is", self.hp)

    def display_magic(self):
        print(self.name, "Magic is", self.magic)

    # Damage is random between a range determined by hero's strength
    def basic_attack(self, opponent):
        time.sleep(self.delay)
        # Checks for if hero is "iced" which decreases damaage by half
        # decrements Ice_count after each turn
        damage = random.randint(self.strength - 10, self.strength + 10)
        if self.iced_count > 0:
            damage = round(damage / 2)
            print(self.name, "is Iced. Damage is reduced by half")
            self.iced_count -= 1
        if opponent.shield == 1:
            damage = round(damage * 0.3)
            print(
                opponent.name, "defends against the upcoming attack")
            opponent.shield -= 1
        print("The", self.name, "attacks")
        time.sleep(self.delay)
        print("The", self.name, "attack did", damage, "damage")
        opponent.hp -= damage
        time.sleep(self.delay)
        print("The", opponent.name, "now has", opponent.hp, "HP")

    # increases hero's hp but only up to the orginal max hp value
    def heal_hp(self):
        if self.magic > 25:
            print(self.name, "cast a healing spell")
            if self.hp + 100 <= self.max_hp:
                self.hp += 100
                time.sleep(self.delay)
                print(self.name, "health increased by 100")
                time.sleep(self.delay)

            else:
                heal = self.max_hp - self.hp
                self.hp += heal
                time.sleep(self.delay)
                print(self.name, "health increased by", heal)
            self.magic -= 30
        else:
            print(self.name, "doesn't have enough magic")

    # Reduce incoming attack by 2/3
    def defend(self):
        time.sleep(self.delay)
        print("The", self.name,
              "takes a defensive position")
        self.shield = 1

    # Restores 5 magic after each turn
    def replenish_magic(self):
        time.sleep(self.delay)
        print("")
        if self.magic < self.max_magic:
            if self.elder_wand == 0:
                self.magic += 5
                print(self.name, "Magic replenished by 5")
            else:
                self.magic += 10
                print(self.name, "Magic replenished by 10")
        else:
            print(self.name, "Magic is full")


class Human(Gladiator):
    def __init__(self, name, hp, strength, magic):
        super().__init__(name, hp, strength, magic)

    # 1/4 chance of running away. Game ends but player doesn't lose or win
    def run_away(self):
        time.sleep(self.delay)
        print(self.name, "attempt to run away...")
        time.sleep(self.delay)
        run_success = random.randint(1, 4)
        if run_success == 1:
            print(self.name, "successfully ran away")
            return 1
        elif run_success != 1:
            print(self.name, "Failed to Escape")
            return 0

    # Reduces basic attack damage by half for 3 turns
    def ice_magic(self, opponent):
        if self.magic > 25:
            time.sleep(self.delay)
            print("The", opponent.name,
                  "has been Iced, it's basic attack is reduced")
            opponent.iced_count += 3
            self.magic -= 25
        else:
            print(self.name, "doesn't have enough magic")

    # performs a high damage attack that can't be guarded
    def lightning_strke(self, opponent):
        if self.magic > 25:
            time.sleep(self.delay)
            damage = random.randint(75, 120)
            print(self.name, "cast lightening which takes", damage, "damage")
            opponent.hp -= damage
            time.sleep(self.delay)
            print(opponent.name, "HP is now", opponent.hp)
            self.magic -= 25
        else:
            print(self.name, "doesn't have enough magic")

    # 1 / 10 chance of getting a super attack
    def super_attack_chance(self):
        random_limit = random.randint(1, 10)
        if random_limit == 1:
            print("6) Super Attack")
            return 1
        else:
            return 0

    # High damage attack between 100 and 200
    def super_attack(self, opponent):
        time.sleep(self.delay)
        print(self.name, "charges up their attack...")
        time.sleep(self.delay)
        print(self.name, "strikes!")
        damage = random.randint(100, 200)
        print("The attack takes", damage, "damage!!")
        opponent.hp -= damage
        time.sleep(self.delay)
        print("The", opponent.name, "now has", opponent.hp, "HP")

    # Randomly generates an updgrade
    def summon_upgrade(self):
        item = random.randint(1, 10)
        time.sleep(self.delay)
        print(self.name, "summons an upgrade...")
        time.sleep(self.delay)
        print("...")
        time.sleep(self.delay)
        print(".....")
        time.sleep(self.delay)
        if item == 1:
            print("You have summoned the Master Sword!")
            time.sleep(self.delay)
            print("Your attack power has increased by 45")
            self.strength += 45
        elif item == 2:
            print("You have summoned the Beskar Armor!")
            time.sleep(self.delay)
            print("Your HP is restored and capacity is increased by 100")
            self.max_hp += 100
            self.hp = self.max_hp
        elif item == 3:
            print("You have summoned the Elder Wand!")
            time.sleep(self.delay)
            print("Your Magic is increased by 100!")
            self.max_magic += 100
            self.magic = self.max_magic
            print("Your magic replenishment is now doubled after each turn")
            self.elder_wand = 1
        elif item == 4 or item == 5:
            print("You have summoned a healing potion")
            if self.hp + 75 <= self.max_hp:
                self.hp += 75
                time.sleep(self.delay)
                print(self.name, "health increased by 75")
                time.sleep(self.delay)
            else:
                heal = self.max_hp - self.hp
                self.hp += heal
                time.sleep(self.delay)
                print(self.name, "health increased by", heal)
        elif item == 6 or item == 7:
            print("You have summoned a magic potion")
            if self.hp + 50 <= self.max_magic:
                self.max_magic += 50
                time.sleep(self.delay)
                print(self.name, "Magic increased by 50")
                time.sleep(self.delay)
            else:
                magic_add = self.max_magic - self.magic
                self.magic += magic_add
                time.sleep(self.delay)
                print(self.name, "Magic increased by", magic_add)
        elif item == 8:
            print("Oh No! You have summoned an evil spirt!")
            time.sleep(self.delay)
            print("It attacks you and takes 50 damage")
            self.hp -= 50
        else:
            print("Nothing is returned.....")


# Sets the Villians attributes
# Currently does not use magic field. This will be incorporated into a later version of the game


class Villian(Gladiator):
    def __init__(self, name, hp, strength, magic):
        super().__init__(name, hp, strength, magic)

    # performs a high damage attack that can't be defended or iced
    def fire_attack(self, opponent):
        if self.magic > 25:
            time.sleep(self.delay)
            damage = random.randint(50, 80)
            print(self.name, "breathes fire which takes", damage, "damage")
            if opponent.shield == 1:
                print("Magic attacks can't be guarded")
            opponent.hp -= damage
            time.sleep(self.delay)
            print(opponent.name, "HP is now", opponent.hp)
            self.magic -= 25
        else:
            print(self.name, "doesn't have enough magic")

    # Randomily determines villian's action
    def villian_action_iq(self, opponent):
        choice = random.randint(1, 6)
        if choice <= 3:
            self.basic_attack(opponent)
        elif choice == 4:
            self.heal_hp()
        elif choice == 5:
            self.defend()
        else:
            self.fire_attack(opponent)
