from Athlete import Athlete
from Sport import Sport

class Team:
    def __init__(self, name, sport:Sport):
        self.name = name
        self.sport = sport
        self.athletes = []

    def add_athlete(self,athlete):
        """Add an athlete to the team"""
        if isinstance(athlete, Athlete):
            self.athletes.append(athlete)
        else:
            raise ValueError("Only Athlete objects can be added to the team")
        
    def set_sport (self,sport):
        "Select  the sport"
        if isinstance(sport,Sport):
            self.sport = Sport
        else:
            raise ValueError("Only Sports objects can be added to the team")

    def __str__(self):
        return f"{self.name} - {self.sport.name} ({len (self.athletes)} athletes)"
    
    def __repr__(self):
        """String representation of the Team class."""
        return f"Team(name ={self.name}, sport={repr(self.sport)}"

    def to_json(self):
        """Convert the Team object to a JSON string."""
        return {
            "name": self.name,
            "sport": self.sport.to_json(),
            "athletes": [athlete.to_json() for athlete in self.athletes]
        }
        
        
if __name__ == "__main__":
    a = Athlete("Chicharito")
    b = Athlete("Memo Ochoa")    
    s = Sport("Futbol",11,"FIFA")
    mexico = Team("Mexico",s) 
    mexico.add_athlete(a)
    mexico.add_athlete(b)
    print (mexico)
    print (repr(mexico))
    print (mexico.to_json())
