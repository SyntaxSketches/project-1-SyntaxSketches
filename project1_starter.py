"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Kabijah Hill
Date: 10/28

"""

def create_character(name, character_class):
    """Create a new character dictionary with stats."""
    
    # Standardize the class name (e.g., handles "warrior" or "WARRIOR")
    standardized_class = character_class.title()
    
    stats = calculate_stats(standardized_class, 1)
    if stats is None:
        return None  # invalid class handled

    strength, magic, health = stats

    character = {
        "name": name,
        "class": standardized_class, # Use the standardized name for consistency
        "level": 1,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 100  # starting gold
    }

    return character


def calculate_stats(character_class, level):
    """Calculate character stats based on class and level."""
    
    # Standardize the class name to ensure consistent matching
    standardized_class = character_class.title()
    
    # Base stats per class and growth factor
    if standardized_class == "Warrior":
        strength = 15 + (level * 2)
        magic = 5 + (level * 1)
        health = 120 + (level * 5)
    elif standardized_class == "Mage":
        strength = 5 + (level * 1)
        magic = 18 + (level * 3)
        health = 90 + (level * 4)
    elif standardized_class == "Rogue":
        strength = 10 + (level * 2)
        magic = 10 + (level * 1)
        health = 80 + (level * 3)
    elif standardized_class == "Cleric":
        strength = 8 + (level * 2)
        magic = 15 + (level * 2)
        health = 110 + (level * 4)
    else:
        # Invalid class name provided
        return None  
    
    # Return the 3-part tuple (strength, magic, health)
    return (strength, magic, health)

def save_character(character, filename):
    """
    Save character info to a text file in required format.
    FIXED: Now explicitly returns a boolean (True/False) as required by tests.
    """
    try: 
        with open(filename, "w") as f:
            f.write(f"Character Name: {character['name']}\n")
            f.write(f"Class: {character['class']}\n")
            f.write(f"Level: {character['level']}\n")
            f.write(f"Strength: {character['strength']}\n")
            f.write(f"Magic: {character['magic']}\n")
            f.write(f"Health: {character['health']}\n")
            f.write(f"Gold: {character['gold']}\n")
        
        #FIX 1: Return True on successful save
        return True 
        
    except IOError as e:
        # Debugging print statement left in for local testing
        print(f"\nFATAL FILE ERROR: Could not save character to {filename}.")
        print(f"OS REASON: {e}")
        return False

def load_character(filename):
    """
    Load character from a text file into a dictionary.
    Includes robust handling for missing files, corrupted lines, and type conversion.
    """
    
    KEY_MAP = {
        "Character Name": "name",
        "Class": "class",
        "Level": "level",
        "Strength": "strength",
        "Magic": "magic",
        "Health": "health",
        "Gold": "gold",
    }

    try: 
        # Attempt to open and read the file
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        # If the file is missing, return None
        return None 
    except Exception as e:
        # Handle other read errors
        print(f"Error reading file {filename}: {e}")
        return None

    character = {}
    for line in lines:
        try: 
            # Split only on the first ": " to handle potential extra colons in data values
            key_str, value_str = line.strip().split(": ", 1) 
        except ValueError:
            # Skip lines that don't split correctly (malformed)
            continue 

        if key_str in KEY_MAP:
            value = value_str
            # Check if the value should be an integer
            if key_str in ["Level", "Strength", "Magic", "Health", "Gold"]:
                try:
                    value = int(value_str) 
                except ValueError:
                    # Abort load if a required integer is corrupted
                    print(f"Error: Invalid number format for {key_str} in file: {value_str}")
                    return None 
                    
            character[KEY_MAP[key_str]] = value

    # Check if all required keys were loaded successfully
    required_keys = set(KEY_MAP.values())
    if set(character.keys()) != required_keys:
        # Data is incomplete
        return None 
        
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
    """
    Increase level and recalculate stats.
    Correctly handles the 3-part tuple returned by calculate_stats.
    """
    character["level"] += 1
    
    # Ensure the class name is standardized for calculate_stats
    standardized_class = character["class"].title()
    stats = calculate_stats(standardized_class, character["level"])
    
    if stats:
        # FIX: Only unpack the three items returned by calculate_stats (no gold)
        strength, magic, health = stats
        
        # Update the character's stats
        character["strength"] = strength
        character["magic"] = magic
        character["health"] = health 
        # Gold is intentionally NOT updated here

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!\n")

    # The program should now execute past here without crashing.
    hero = create_character("Ariah", "Warrior")
    mage = create_character("Memphis", "Rogue")

    if hero:
        print("\nMain Character:")
        display_character(hero)
        save_character(hero, "ariah.txt")
        
        # Demonstrate level up and saving
        level_up(hero)
        print("\nMain Character (Level 2):")
        display_character(hero)
        save_character(hero, "ariah_L2.txt")
        
        # Demonstrate loading
        loaded_hero = load_character("ariah.txt")
        if loaded_hero:
             print("\nLoaded Ariah (Level 1):")
             display_character(loaded_hero)
        else:
             print("\nError loading Ariah.")

    else:
        print("Error: hero creation failed.\n")

    if mage:
        print("\nSide Character:")
        display_character(mage)
        save_character(mage, "memphis.txt")
    else:
        print("Error: mage creation failed.\n")
