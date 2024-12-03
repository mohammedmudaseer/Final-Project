from Chapter_1 import chapter_one
from Chapter_2 import chapter_two
from Chapter_3 import chapter_three
from Chapter_4 import chapter_four
from Chapter_5 import chapter_five

def start_game():
    print("Welcome to the Adventure Game: Distress in Verenthia!")
    chapter_one()
    chapter_two()
    chapter_three()
    chapter_four()
    chapter_five()
    print("Thank you for playing!")

if __name__ == "__main__":
    start_game()