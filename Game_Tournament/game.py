""" 
Docstring for game_tournament.Game Game class represents a game in the tournament, It has a name, a sport, and a list of teams
"""
from Athlete import Athlete
from Sport import Sport
from Team import Team
import random

class Game: 
    """Gameclass represents a game in the tournament, It has two teams and a score"""

    def __init__ (self, A:Team  , B:Team):
        """Custom constructor for game class."""
        self.set_team(A, "local")
        self.set_team(B, "visitor")
        self.score = {
            A.name: 0, B.name: 0
        }

    def set_team(self, team, role):
        """ Set a team for the game"""
        if role == "local":
            self.team_a = team
        elif role == "visitor":
            self.team_b = team
        else:
            raise ValueError ("Role must be 'local or 'visitor'.")
        
    def play (self):
        """Simulate playing the game by randomly assigning  scores  ot each team. """
        self.score[self.team_a.name] = random.randint(0, Sport.max_score[self.team_a.sport.name])
        self.score[self.team_b.name] = random.randint(0, Sport.max_score[self.team_b.sport.name])

    def __str__(self):
        """String representation of the Game class."""
        return f"{self.team_a.name} vs  {self.team_b.name} - Score: {self.score[self.team_a.name]} : {self.score[self.team_b.name]}"
        
        
if __name__ == "__main__":
    a = Athlete("Chicharito")
    b = Athlete("Memo Ochoa")    
    s = Sport("Futbol",11,"FIFA")
    mexico = Team("Mexico",s) 
    mexico.add_athlete(a)
    mexico.add_athlete(b)
    brazil = Team("Brazil",s)
    brazil.add_athlete(Athlete("Pelé"))
    brazil.add_athlete(Athlete("Zico"))
    game = Game(mexico,brazil)
    game.play()
    print(game)