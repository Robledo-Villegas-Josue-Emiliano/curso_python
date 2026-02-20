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

def save_game_to_json(game_data, filename):
        """Save the game object to a JSON file"""
        with open(filename, 'w' , encoding='utf-8') as f:
            json.dump(game_data, f, indent=4)

def a_tournament():
        """Example usage of the game class."""
        players_mexico = ['Chicharito','Piojo','Guardado','Hector Moreno','Memo Ochoa','Gil Mora','Giovanni Dos Santos','Salcido','Hugo Sanches','Cuauthémoc Blanco','Jorge Campos']
        players_brazil = ['Ronaldinho','Neymar','Ronaldo Nazario','Alisson','Pelé','Marquinhos','Hulk','David Luis','Rapinha','Casemiro','Zico']
        players_france = ['Mbappé','Griezmann','Pogba','Lloris','Kanté','Benzema','Varane','Coman','Rabiot','Giroud','Matuidi']
        players_spain = ['Sergio Ramos','Iniesta','Xavi','Casillas','Puyol','David Villa','Busquets','Silva','Morata','Isco','Alba']
        players_japan = ['Kagawa','Honda','Okazaki','Nagatomo','Yoshida','Hasebe','Kawashima','Inui','Shibasaki','Muto','Sakai']
        players_germany = ['Müller','Kroos','Neuer','Hummels','Reus','Götze','Khedira','Draxler','Schweinsteiger','Boateng','Özil']
        players_italy = ['Buffon','Chiellini','Pirlo','Balotelli','Marchisio','De Rossi','Insigne','Barzagli','Bonucci','Verratti','El Shaarawy']
        players_netherlands = ['Van Dijk','Depay','Robben','Sneijder','Van Persie','De Jong','Blind','Wijnaldum','Cillessen','Babel','Kuyt']
        sport = Sport("Futbol",11,"FIFA")
        team_mexico = Team("México",sport)
        team_brazil = Team("Brazil", sport)
        team_france = Team("France", sport)
        team_spain = Team("Spain", sport)
        team_japan = Team("Japan", sport)
        team_germany = Team("Germany", sport)
        team_italy = Team("Italy", sport)
        team_netherlands = Team("Netherlands", sport)
        for player in players_mexico:
            team_mexico.add_athlete(Athlete(player))
        for player in players_brazil:
            team_brazil.add_athlete(Athlete(player))
        for player in players_france:
            team_france.add_athlete(Athlete(player))
        for player in players_spain:
            team_spain.add_athlete(Athlete(player))
        for player in players_japan:    
            team_japan.add_athlete(Athlete(player))
        for player in players_germany:
            team_germany.add_athlete(Athlete(player))
        for player in players_italy:
            team_italy.add_athlete(Athlete(player)) 
        for player in players_netherlands:
            team_netherlands.add_athlete(Athlete(player))   
        tournament_list = [team_mexico,team_brazil,team_france, team_germany,team_italy,team_japan,team_spain,team_netherlands]
        return [team.to_json() for team in tournament_list]
        
        
if __name__ == "__main__":
    string_game = a_tournament()
    save_game_to_json(string_game, "tournament.json")
    print(string_game)
