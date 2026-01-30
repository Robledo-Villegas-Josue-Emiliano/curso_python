"""
Author: Josué Emiliano
"""

from menu import display_menu
from game_logic import game
from game_logic import two_players

def main():
    """Main function to run the Tic Tac Toer game
    """
    
    while True:
        choice = display_menu()
        if choice == 1:
            print("One Player Game is not implemented yet.")
            # Here you would call the one player game function when
            # implmented
        elif choice == 2:
            two_players()
        elif choice == 3:
            print("Exiting the game. Goodbye!")
            break

if __name__ == "__main__":
    main()