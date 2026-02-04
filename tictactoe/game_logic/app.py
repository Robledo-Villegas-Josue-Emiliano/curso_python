"""
Author: Josué Emiliano
"""

from menu import display_menu
#from game_logic import game
from game_logic import play_game

def main():
    """Main function to run the Tic Tac Toer game
    """
    
    while True:
        choice = display_menu()
        if choice == 1:
            play_game()
        elif choice == 2:
            play_game()
        elif choice == 3:
            print("Exiting the game. Goodbye!")
            break

if __name__ == "__main__":
    main()