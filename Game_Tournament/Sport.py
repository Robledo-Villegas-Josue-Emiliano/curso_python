"""Sport class rpresents a sport in the tournament, It has a name and a league."""
class Sport:
    """Sport class represents a asport in the tournament. It has a name and a league"""
    max_score = {
         "Futbol" : 7,
         "Baseball" : 20,
         "Basketball" : 130,
         "Futbol Americano" : 60,
         "Hockey" : 10
    }
    def __init__(self, name, num_players, league):
        """Custom constructor for sport class."""
        self.name = name
        self.league = league
        self.num_players = num_players

    def add_name (self, name):
        """"Add name to the sport"""
        if name in self.max_score:
            self.name = name
        else:
            raise ValueError(f"Sport name must ve one of the following {', '.join(self.max_score.keys())}")
         
    def __str__(self):
        "String representation of the Sport Class. "
        return f"{self.name} ({self.league}) - {self.num_players} players"
    def __repr__(self):
        "String representation of the Sport Class. "
        return f"Sport=(name={self.name}, league={self.league}), players={self.num_players}"
    def to_json(self):
        """Convert the Sport object to a JSON string."""
        return{
            "name":self.name,
            "league":self.league,
            "num_players":self.num_players
        }
    
if __name__=="__main__":
        """Test sport class."""
        sport = Sport("Baseball",22,"MLB")
        print(sport)
        print(sport.to_json())
        print(repr(sport))