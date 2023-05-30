from adventure_game_pkg.gladiator_attr import Villian, Human
from adventure_game_pkg.display_functions import display_options, display_magic_options, display_hero_options

while True:
    # displays the warrior, wizard and tank hero options
    display_hero_options()
    # HP, Magic, and Strength populate based on hero choice
    hero_choice = input("Choose your hero: ")
    if hero_choice == "1":
        print("You have chosen the Warrior")
        hero = Human("Warrior", 150, 55, 100)
        break
    elif hero_choice == "2":
        print("You have chosen the Wizard")
        hero = Human("Wizard", 150, 30, 160)
        break
    elif hero_choice == "3":
        print("You have chosen the Tank")
        hero = Human("Tank", 230, 30, 100)
        break
    else:
        print("Invalid Choice")
    print("")

# create dragon enemy with attributes
dragon = Villian("Dragon", 350, 60, 150)

print("A Dragon appraches....")
# Game runs unitl either dragon or hero is defeated
while (dragon.hp > 0) and (hero.hp > 0):
    # displays options Attack, Run, or Magic
    print("")
    hero.display_hp()
    hero.display_magic()
    print("")
    dragon.display_hp()
    dragon.display_magic()
    print("")
    display_options()
    # 1/10 chance of getting super attack
    super_attack_chance = hero.super_attack_chance()
    action = input("what is your choice?: ")
    if action == "1":
        # perform basic attack
        hero.basic_attack(dragon)
    elif action == "2":
        while True:
            # display magic options
            display_magic_options()
            magic_action = input("Choose a magic ability: ")
            if magic_action == "1":
                # increase hero hp
                hero.heal_hp()
                break
            elif magic_action == "2":
                # ice magic reduces enemies damange by half for 3 turns
                hero.ice_magic(dragon)
                break
            elif magic_action == "3":
                # decreases dragon hp
                hero.lightning_strke(dragon)
                break
            else:
                print("Invalid input")
    elif action == "3":
        # Damage reduced by 2/3 for 1 turn
        hero.defend()
    elif action == "4":
        # 1/ 4 chance from running away
        run_successful = hero.run_away()
        if run_successful == 1:
            break
    elif action == "5":
        hero.summon_upgrade()
    elif action == "6" and super_attack_chance == 1:
        hero.super_attack(dragon)
    else:
        print("Invalid Response")
    # dragon attacks after each turn
    if dragon.hp > 0:
        dragon.villian_action_iq(hero)
    # magic is increased by a small amount after each turn
    hero.replenish_magic()
    dragon.replenish_magic()
if dragon.hp <= 0:
    print(dragon.name, "is defeated!")
    print("You have won!")
if hero.hp <= 0:
    print(hero.name, "is defeated")
    print("You Lost: GAME OVER")
