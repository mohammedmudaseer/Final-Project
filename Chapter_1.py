# Module for Chapter 1: Receiving and Analyzing the Distress Signal
def chapter_one():
    print("Chapter 1: The Distress Signal")
    print("Aiden picks up a distress signal from Verenthia.")
    
    # Action 1: Analyze the signal
    signal_data = analyze_signal()
    print("Signal analyzed:", signal_data)
    
    # Action 2: Prepare the ship
    gather_supplies()
    
    # Transition to Chapter 2
    print("Course set for Verenthia. Proceeding to Chapter 2.")
    
    from Chapter_2 import chapter_two  # Lazy import
    chapter_two()

def analyze_signal():
    print("Analyzing signal...")
    return {"origin": "Verenthia", "message": "SOS"}

def gather_supplies():
    print("Gathering supplies for the journey...")
    print("Supplies loaded successfully.")