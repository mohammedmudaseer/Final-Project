# Module for Chapter 3: Combat or Stealth
from Chapter_2 import chapter_two
import Chapter_4


def chapter_three():
    print("Chapter 3: Confronting Robotic Sentinels")
    
    # Action 1: Choose combat or stealth
    choice = input("Choose your approach (combat/stealth): ").lower()
    if choice == "combat":
        if engage_combat():
            print("Combat successful! Acquired advanced weaponry.")
        else:
            print("Defeated! Returning to Chapter 2 to gather resources.")
            chapter_two()
    elif choice == "stealth":
        if evade_sentinals():
            print("Stealth successful! Uncovered hidden treasures.")
        else:
            print("Detected! Returning to Chapter 2.")
            chapter_two()
    
    # Progress to Chapter 4
    Chapter_4()

def engage_combat():
    print("Engaging in combat...")
    # Simulated success/failure
    return True  # Change to False for testing

def evade_sentinals():
    print("Attempting to evade sentinels...")
    # Simulated success/failure
    return True