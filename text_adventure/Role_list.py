roles = {
    "1": {
        "name": "Assassin",
        "skill": ["Assassinate"],
        "attributes": {
            "maxhp": 11,
            "attack": 11,
            "defence": 11,
            "speed": 11
        }
    },
    "2": {
        "name": "Rogue",
        "skill": ["Sneak"],
        "attributes": {
            "maxhp": 7,
            "attack": 5,
            "defence": 1,
            "speed": 5
        }
    },
    "3": {
        "name": "Ninja",
        "skill": ["Smoke_Screen"],
        "attributes": {
            "maxhp": 10,
            "attack": 10,
            "defence": 10,
            "speed": 5
        }
    },
    "4": {
        "name": "Thief",
        "skill": ["Steal"],
        "attributes": {
            "maxhp": 7,
            "attack": 5,
            "defence": 1,
            "speed": 5
        }
    },
    "5": {
        "name": "Worlds weakest God",
        "skill": ["Thoughts & Prayers"],
        "attributes": {
            "maxhp": 3,
            "attack": 1,
            "defence": 1,
            "speed": 1
        }
    }
}

def use_skill(skill_name):
    if skill_name == "Assassinate":
        # Define the effect of the Assassinate skill
        print("You use Assassinate skill! It's a critical hit!")
    elif skill_name == "Sneak":
        # Define the effect of the Sneak skill
        print("You activate Sneak skill and become invisible.")
    elif skill_name == "Smoke_Screen":
        # Define the effect of the Smoke Screen skill
        print("You deploy a Smoke Screen and obscure the battlefield.")
    elif skill_name == "steal":
        #Define the effect of steal
        print("You steal from the target! Do we even have items?")

def player_choice():
    role = input("Choose a class (1: Assassin, 2: Rogue, 3: Ninja, 4:thief): ")
    if role in roles:
        role_data = roles[role]
        print(f"You've selected {role_data['name']}")
        print(role_data)
        return role
    else:
        print("Do it right, retard!")
        player_choice()

#player_choice()