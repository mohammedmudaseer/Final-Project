from Chapter_3 import chapter_three  # Import the chapter_three function

def chapter_two():
    print("Chapter 2: Exploring Verenthia")
    print("Aiden lands on the planet, greeted by strange ruins and vegetation.")
    
    # Action 1: Explore ruins
    explore_ruins()
    
    # Action 2: Interact with a holographic message
    holographic_message()
    
    # Action 3: Search for clues
    if search_clues():
        print("Clues found! Unlocking paths to deeper exploration.")
        chapter_three()  # Call the imported chapter_three function
    else:
        print("No clues found. Revisiting exploration...")
        chapter_two()

def explore_ruins():
    print("Exploring the mysterious ruins...")
    # Simulated action
    print("Ruins reveal advanced technology and hints of the lost crew.")

def holographic_message():
    print("Interacting with a holographic message...")
    print('"This is the lost crew. Beware of Verenthia’s guardians."')

def search_clues():
    print("Searching for clues...")
    # Simulated search success/failure
    return True  # Change to False to test re-exploration