"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Your Name Here]
Date: [Date]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""

def create_character(name, character_class):
    """Create a new character dictionary with stats."""
    stats = calculate_stats(character_class, 1)
    if stats is None:
        return None

    strength, magic, health, gold = stats

    character = {
        "name": name,
        "class": character_class,
        "level": 1,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }
    return character


def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    if character_class == "Warrior":
        strength = 10 + level * 3
        magic = 3 + level * 1
        health = 100 + level * 5
    elif character_class == "Mage":
        strength = 4 + level * 1
        magic = 12 + level * 4
        health = 80 + level * 3
    elif character_class == "Rogue":
        strength = 7 + level * 2
        magic = 6 + level * 2
        health = 90 + level * 4
    elif character_class == "Cleric":
        strength = 6 + level * 1
        magic = 10 + level * 3
        health = 110 + level * 5
    else:
        # Return default stats even for invalid classes
        strength = 5 + level * 1
        magic = 5 + level * 1
        health = 100 + level * 3
    return (strength, magic, health)  # always return a tuple

def save_character(character, filename):
    """Save character info to a text file in required format."""
    with open(filename, "w") as f:
        f.write(f"Character Name: {character['name']}\n")
        f.write(f"Class: {character['class']}\n")
        f.write(f"Level: {character['level']}\n")
        f.write(f"Strength: {character['strength']}\n")
        f.write(f"Magic: {character['magic']}\n")
        f.write(f"Health: {character['health']}\n")
        f.write(f"Gold: {character['gold']}\n")

def load_character(filename):
    """Load character from a text file into a dictionary."""
    with open(filename, "r") as f:
        lines = f.readlines()

    character = {}
    for line in lines:
        key, value = line.strip().split(": ")
        if key in ["Level", "Strength", "Magic", "Health", "Gold"]:
            value = int(value)
        character[key.replace("Character Name", "name").lower()] = value

    return character

def display_character(character):
    """Display character info neatly."""
    print(f"Character Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")

def level_up(character):
    """Increase level and recalculate stats."""
    character["level"] += 1
    stats = calculate_stats(character["class"], character["level"])
    if stats:
        strength, magic, health, gold = stats
        character["strength"] = strength
        character["magic"] = magic
        character["health"] = health
        character["gold"] = gold

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    ariah = create_character("Ariah", "Mage")
    memphis = create_character("Memphis", "Rogue")
    locus = create_character("Locus", "Warrior")

    # Display them
    display_character(ariah)
    print()
    display_character(memphis)
    print()
    display_character(locus)

    # Save to files
    save_character(ariah, "ariah.txt")
    save_character(memphis, "memphis.txt")
    save_character(locus, "locus.txt")

    print("\nCharacters saved successfully!")
