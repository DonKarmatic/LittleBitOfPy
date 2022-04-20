import random

def game():
    while True:
        choice = int(input("Dare to wander, or shall you rest? Travel = 1, Rest = 2, Quit = 0: "))
        if choice == 1:
            print("Goodluck, traveller!")
            travel()
        elif choice == 2:
            print("Take your time, traveller. You've recovered a little bit. You know have full HP")
        elif choice == 0:
            break
        else:
            print("Woops, forgive me traveller, I don't know what that choice means.")

def enemy(area):

    forest = ["Giant Spider", "Skeleton Warrior", "Tusked Beast"]
    desert = ["Sand Worm", "Sand Scorpion", "Wind Spirit"]
    lake = ["Naiad", "Lake Serpent", "Water Spirit"]

    if area == "forest":
        return random.choice(forest)
    if area == "desert":
        return random.choice(desert)
    if area == "lake":
        return random.choice(lake)


def battle(location, enemy):

    monster = enemy
    print("You've encountered", monster, "! ")
    monsterHP = 20
    playerHP = 20

    while monsterHP > 0 and playerHP > 0:
        choice = int(input("Attack = 1, Run = 2: "))
        if choice == 1:
            monsterDefense = random.randint(1, 3)
            if monsterDefense == 1:
                print("You miss the attack!")
            else:
                damage = random.randint(2, 5)
                monsterHP -= damage
                print("Your attack landed! You did", damage, "damage! The monster has", monsterHP, "HP left!")
        elif choice == 2:
            print("You've decided to run!")
            break
        else:
            print("You've missed your turn!")

        defense = int(input("The monster is attacking! Block = 1, Dodge = 2: "))
        monsterAttack = random.randint(1, 2)
        if monsterAttack == 1:
            monsterDamage = random.randint(2, 4)
            if defense == 1:
                print("You've successfully blocked the attack!")
            else:
                playerHP -= monsterDamage
                print("You've taken", monsterDamage, "damage! You currently have", playerHP, "HP left!")

        if monsterAttack == 2:
            monsterDamage = random.randint(5, 7)
            if defense == 1:
                playerHP -= monsterDamage
                print("You've taken", monsterDamage, "damage! You currently have", playerHP, "HP left!")
            else:
                print("You've successfully dodged the attack!")

    if monsterHP <= 0:
        print("You've won the battle! Congratulations!")
        return True
    if playerHP <= 0:
        print("Oh no, you've lost the battle!")
        return False


def travel():

    World = ["forest", "desert", "lake"]
    location = random.choice(World)
    print("You've travelled to the", location + "! ")
    monster = enemy(location)
    isBattleWon = battle(location, monster)
    if isBattleWon == True:
        choice = int(input("Would you like to keep going? Continue = 1, Return = 2 "))
        if choice == 1:
            travel()
        elif choice == 2:
            print("Rest well traveller!")
        else:
            print("Odd response, you seem to need rest")
    else:
        print("Better luck next time, traveller!")

def main():
    print("Welcome to Little World! Hope you enjoy the game!")
    game()
    print("Thank you for playing, hope to you see soon!")


main()
