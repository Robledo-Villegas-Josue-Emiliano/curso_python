"""
Docstring for tictactoe.
game_logic.board
Author : Josué Emiliano Robledo Villegas

""""
def display board(dboard:dict) -> None:
    """ Display game board 
    of Tictactoe
    """"
    d = dboard
    print(f"{d[0]:2s}|{d[1]:2s}|{d[2]:2s}")
    print("-----|-----|-----")
    print(f"{d[3]:2s}|{d[4]:2s}|{d[5]:2s}")
    print("-----|-----|-----")
    print(f"{d[6]:2s}|{d[7]:2s}|{d[8]:2s}")



