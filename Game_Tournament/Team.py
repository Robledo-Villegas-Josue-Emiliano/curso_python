import Athlete
import Sport

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
        
if __name__ == "__main__":
    team = Team("Dodgers","Baseball")
    
