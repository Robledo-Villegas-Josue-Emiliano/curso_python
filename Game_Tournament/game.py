""" 
Docstring for game_tournament.Game Game class represents a game in the tournament, It has a name, a sport, and a list of teams
"""
from Athlete import Athlete
from Sport import Sport
from Team import Team
import random
import json

class Game: 
    """Gameclass represents a game in the tournament, It has two teams and a score"""

    def __init__(self, A:Team  , B:Team):
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
        
    def play(self):
        """Simulate playing the game by randomly assigning  scores  ot each team. """
        self.score[self.team_a.name] = random.randint(0, Sport.max_score[self.team_a.sport.name])
        self.score[self.team_b.name] = random.randint(0, Sport.max_score[self.team_b.sport.name])

    def __str__(self):
        """String representation of the Game class."""
        return f"{self.team_a.name} vs  {self.team_b.name} - Score: {self.score[self.team_a.name]} : {self.score[self.team_b.name]}"
    
    def __repr__(self):
        """String representation of the game class"""
        return f"Game(team_a={repr(self.team_a)}, team_b={repr(self.team_b)}, score={self.score})"
    
    def to_json(self):
        """String representation of the game class."""
        """Convert the Game to a JSON string"""
        return {
            "team_a" : self.team_a.to_json(),
            "team_b" : self.team_b.to_json(),
            "Score"  : self.score
        }

    def a_game():
        """Example usage of the game class."""
        players_mex = ['Chicharito','Piojo','Guardado','Hector Moreno','Memo Ochoa','Gil Mora','Giovanni Dos Santos','Salcido','Hugo Sanches','Cuauthémoc Blanco','Jorge Campos']
        players_brz = ['Ronaldinho','Neymar','Ronaldo Nazario','Alisson','Pelé','Marquinhos','Hulk','David Luis','Rapinha','Casemiro','Zico']
        Sport = Sport("Futbol",11,"FIFA")
        team_mx = Team("México",sport)
        team_brz = Team("Brazil", sport)
        for player in players_mex:
            team_mx.add_athlete(Athlete(player))
        for player in players_brz:
            team_brz.add_athlete(Athlete(player))
        game = Game(team_mx,team_brz)
        game_string = game.to_json()
        return game_string

    def save_game_to_json(game, filename):
        """Save the game object to a JSON file"""
        with open(filename, 'w' , encodign='urf-8') as f:json.dump(game.to_json(), f, indent=4)
        
if __name__ == "__main__":
    string_game = a_game()
    save_game_to_json(string_game, "game.json")
