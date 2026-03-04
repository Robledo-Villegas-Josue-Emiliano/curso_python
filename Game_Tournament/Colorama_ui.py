import os 
import colorama
from Tournament import Tournament
from colorama import  Fore, Back, Style, init
init(autoreset=True)

class coloramaUI:
    def __init__ (self):
        self.tournament = None
        self.current_file = None

    def current_file (self, file_path: str):
        self.current_file = file_path

    def run (self):
        """Run the coloramaUI"""
        # coloramaUI.init(autoreset=True)
        # self.show_menu()
        self.display_menu()
    
    def show_menu (self):
        """Show the menu"""
        while True : 
            print ("\n Tournament")
            print ("1. Load tournament")
            print ("2.Display tournament")
            print ("3.Exit")
            choice = input ("Enter your choice: ")
            if choice == "1":
                file_path = input ("Enter the path to the JSON file")
                self.set_current_file(file_path)
                self.open.tournament(file_path)
            elif choice == "2":
                self.display_tournament()
            elif choice =="3":
                self.exit_app()
            else:
                print ("Invalid choice. please try again.")

    def open_tournament (self, file_Path: str):
        """open tournament from the JSON file"""
        self.tournament = Tournament("Tournament")
        self.tournament .load_json(file_Path)

    def display_tournament (self):
        """Display tournament """
        #Clear screen
        os.system ("cls" if os.name == "nt" else "clear")
        #set background color to gray and texy color to white 
        print( Back.LIGHTBLACK_EX + Fore.WHITE + str(self.tournament))
        for group in self.tournament.groups:
            print(group)
        for game in self.tournament.games:
            print(game)
        else:
            print("No tournament loaded.")

    def exit_app(self):
        """Exit the application""" 
        print("Exiting application...")
        exit()

    def get_tournament_json (self):
        """ Get the tournament"""
        file_path = input ("Enter the path to the JSON file: ")
        self.set_current_file (file_path)
        self.open_tournament(file_path)
    
    def display_menu (self):
        """ Show the menu """
        dictionary_menu = {
            "1": "Load tournament",
            "2": "Display tournament",
            "3": "Exit"
        }
        action_dictionary = {
            "1": self.get_tournament_json,
            "2": self.display_tournament,
            "3": self.exit_app
        }
        while True:
            print("\nTournament")
            for key in sorted (dictionary_menu.keys()):
                print(f"{key}. {dictionary_menu[key]}")
            choice = input ("Enter your choice: ")
            if choice in action_dictionary:
                action_dictionary[choice]()
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    ui  = coloramaUI()
    ui.set_current_file("tournament.json")
    ui.open_tournament()
    ui.run()       

