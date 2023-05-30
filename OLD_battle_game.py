
# Set up your game variables: the game characters and their stats.
import random
import time

org_hero_hp = 200
hero_hp = 200
hero_mana = 100

dragon_hp = 400
iced_count = 0

delay = 1


def basic_attack():
    time.sleep(delay)
    return random.randint(15, 25)


def limit_break_attack():
    time.sleep(delay)
    return random.randint(100, 200)


def dragon_attack():
    time.sleep(delay)
    global iced_count
    if iced_count == 0:
        return random.randint(25, 45)
    else:
        time.sleep(delay)
        iced_count = iced_count - 1
        time.sleep(delay)
        print("The Dragon is impacted by ice for",
              str(iced_count), "more turns")
        return int((random.randint(25, 45))/2)


def lightning_strke(dragon_hp):
    time.sleep(delay)
    print("Lightning strikes the dragon dealing 100 damage!")
    time.sleep(delay)
    print("The Dragons HP is now", dragon_hp)
    return dragon_hp - 100


def limit_break():
    random_limit = random.randint(1, 10)
    if random_limit == 1:
        print("4) LIMIT BREAK")
        return 1
    else:
        return 0


def heal_hp(hero_hp):
    if hero_hp + 50 <= org_hero_hp:
        hero_hp = hero_hp + 50
        time.sleep(delay)
        print("Your health increased by 50 pts")
        return hero_hp
    else:
        heal = org_hero_hp - hero_hp
        time.sleep(delay)
        print("Your health increased by", str(heal))
        hero_hp = 200
        return hero_hp


def ice_magic():
    time.sleep(delay)
    print("The Dragon has been Iced, all of it's attacks are reduced")
    global iced_count
    iced_count = 3


def run_away():
    time.sleep(delay)
    print("You attempt to run away...")
    time.sleep(delay)
    run_success = random.randint(1, 4)
    if run_success == 1:
        print("You successfully ran away")
        return 1
    elif run_success != 1:
        print("The Dragon Caught You")
        return 0


# # Prompt the player to choose from a list of options.

# # Gameplay function
print("a dragon appraches!")
while dragon_hp >= 0:
    time.sleep(delay)
    print("          ======          ")
    print("it's your move:")
    print("1) Attack")
    print("2) Magic")
    print("3) Run")
    limit_break_chance = limit_break()
    print("          ======          ")
    # prompt use to choose action
    action = input("what is your choice?")
    if action == "1":
        attack = basic_attack()
        time.sleep(delay)
        print("you attack and do", attack, "damage")
        dragon_hp = dragon_hp - attack
        time.sleep(delay)
        print("the dragon now has", dragon_hp, "health")
        if dragon_hp <= 0:
            time.sleep(delay)
            print("the Dragon has lost the battle")
            break
    elif action == "2":
        while True:
            time.sleep(delay)
            print("")
            print("Your Mana Remaining:", hero_mana)
            print("1) Heal 50 Points - 25 mana")
            print("2) Ice - Reduce Dragon Damage for 3 turns - 25 mana ")
            print("3) Lightening - 100 pt. Damage - 25 mana")
            print("")
            magic_choice = input("What do you choose")
            if magic_choice == "1" and hero_mana > 25:
                hero_hp = heal_hp(hero_hp)
                hero_mana = hero_mana - 25
                time.sleep(delay)
                print("You health is now", hero_hp)
                time.sleep(delay)
                print("You mana is now", hero_mana)
                break
            elif magic_choice == "2" and hero_mana > 25:
                ice_magic()
                hero_mana = hero_mana - 25
                time.sleep(delay)
                print("You mana is now", hero_mana)
                break
            elif magic_choice == "3":
                dragon_hp = lightning_strke(dragon_hp)
                hero_mana = hero_mana - 25
                if dragon_hp <= 0:
                    time.sleep(delay)
                    print("the Dragon has lost the battle")
                break
            else:
                time.sleep(delay)
                print("invalid choice")

    elif action == "3":
        run = run_away()
        if run == 1:
            break
        elif run == 0:
            attack = dragon_attack()
            time.sleep(delay)
            print("The dragon attacks you from behind and takes",
                  attack, "damage")
            hero_hp = hero_hp - attack
            time.sleep(delay)
            print("Your health is now", hero_hp)
            if hero_hp <= 0:
                time.sleep(delay)
                print("You have lost the battle")
                break
    elif action == "4" and limit_break_chance == 1:
        attack = limit_break_attack()
        time.sleep(delay)
        print("you attack and do", attack, "damage!")
        dragon_hp = dragon_hp - attack
        time.sleep(delay)
        print("the dragon now has", dragon_hp, "health")
        if dragon_hp <= 0:
            time.sleep(delay)
            print("the Dragon has lost the battle")
            break
    else:
        print("invalid response")
    attack = dragon_attack()
    time.sleep(delay)
    print("The dragon attacks and takes",
          attack, "damage")
    hero_hp = hero_hp - attack
    time.sleep(delay)
    print("Your health is now", hero_hp)
    if hero_hp <= 0:
        time.sleep(delay)
        print("You have lost the battle")
        break
