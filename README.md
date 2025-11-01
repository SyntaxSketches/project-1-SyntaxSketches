Game Concept: The World of Chrysalis

The world of Chrysalis is a world full of shimmering magic and ancient legends, where the rise of powerful, predominantly female heroes is chronicled for posterity. You get to choose from four core archetypes: the tough Warrior (Ariah), the elusive Rogue (Lyra), the supportive Cleric (Elara), and the powerful Mage (Memphis). This little system tracks their growth and gear reliably as they begin their journey!

Design Choices: Stat Formulas

I wanted the stats to be easy to understand but still make each class feel completely unique. My formula for calculating stats is straightforward and applies to every stat:

                                       BASE STAT + (LEVEL X GROWTH RATE)

Warrior (Ariah): They're built as the main tank. They have high starting Health (120) and massive HP Growth (+5), making them super durable. Their high Strength (15) ensures they hit hard right away.

Mage (Memphis): They're the glass cannons. They have the highest starting Magic (18) and the best Magic Growth (+3) for rapid spell power scaling. Their low starting Strength is the necessary tradeoff!

Rogue (Lyra): They're agile and balanced. Their base stats are pretty even, and their low starting Health means they have to rely on their quick Strength (10) and speed rather than endurance.

Cleric (Elara): They're durable support. They have strong Magic (15) for healing and casting, plus great Health (110), making them tough, versatile healers.

BONUS Creative Feature: Starting Equipment based on Class

I added Starting Equipment based on Class! 
Warrior: Gets heavy defense items like the Lionheart Chestplate and Guardian's Aegis to protect that huge Health pool, plus the powerful Aetherium Greatsword for damage.

Mage: Gets powerful, mystic items like the Prism Staff of Mana and the Ancient Rune Scroll to channel their high Magic stat.

Rogue: Gets gear for stealth and skill, including the Twin Shadow Blades and the essential Master's Lockpick Set.

Cleric: Gets mystical support gear like the Scepter of Divine Power and Sacred Mantle, aligning their divine gear with their high Magic and Health.

The code handles this by pulling the corresponding equipment string from a dictionary and saving it directly into the character's file when created!

                                                      AI Code Stuff
I used AI heavily to ensure the code was bug-free and compliant. AI helped me implement the sophisticated error handling in the file I/O functions and fixed several tricky logical errors,

                                                    How to run my code
To run and verify my project, follow the steps below:

Navigate to the Project Directory

Open the terminal and move into the folder containing project1_starter.py.
cd project-1-SyntaxSketches

Run the Program

Execute the main Python file to generate and display all test characters.
This will also create text files for each character in the same directory. python project1_starter.py

Run the Automated Tests

Use the  command (pytest) to verify that all functions and file operations pass the automated test suite:
If everything is working correctly, you should see all tests pass with green checkmarks in the terminal output
