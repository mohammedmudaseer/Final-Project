# Module for Chapter 5: Escape Sequence
def chapter_five():
    print("Chapter 5: The Escape")
    print("The chamber begins collapsing. Time is running out!")
    
    # Action 1: Escape paths
    escape_path = input("Choose escape method (run/technology): ").lower()
    if escape_path == "run":
        dash_through()
    elif escape_path == "technology":
        carve_route()
    
    print("Returning to the ship with newfound knowledge. Game complete!")

def dash_through():
    print("Running through collapsing paths...")
    print("You narrowly escape entrapment!")

def carve_route():
    print("Using advanced technology to carve a safe path...")
    print("You create an efficient escape route!")