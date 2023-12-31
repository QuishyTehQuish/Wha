import random
import equip
import text_adventure.spells_list as spells_list

def gen_chest():
    num_items = random.randint(1, 2)
    chest = {
        "items": [random.choice(equip.Equipment.equipment_list) for _ in range(num_items)]
    }
    return chest

def gen_magic():
    num_items = random.randint(1, 2)
    chest = {
        "spells": [random.choice(spells_list.spell_book.spells) for _ in range(num_items)]
    }
    return chest

def choice():
    player_choice = input("You find a chest! Do you want to open it? (yes/no): ")
    if player_choice.lower() == "yes":
        chest = gen_chest()
        print("You opened the chest and found the following items:")
        for item in chest["items"]:
            print(item["name"], "-", item["description"])


