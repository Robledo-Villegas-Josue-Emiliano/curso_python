"""Docstring for game_tournament.py"""
import random
from Team import Team
from Game  import Game

class Group:

    def __init__ (self, name):
        self.name = name
        self.teams = []
        self.games = []
    
    def add_team (self,team):
        if isinstance (team, Team):
            self.teams.append(team)
        else:
            raise ValueError ("Only team objects can be added as a team.")
        
    def add_games(self):
        """ Add games for the group """
        for i in range (len(self.teams)):
            for j in range (i + 1, len(self.teams)):
                games = Game (self.teams[i], self.teams[j])
                self.games.append(games)

    def __repr__(self):
        """ String representation of the Group class. """
        return f"Group(name={self.name}, teams={repr(self.teams)})"
    
    def to_json(self):      
        """ Convert the Group object to a JSON string. """
        return {
            "name": self.name,
            "teams": [team.to_json() for team in self.teams]
        }
    
    def display_group(self):
        """ Display the group. """
        print(f"Group: {self.name}")
        for team in self.teams:
            print(f"  {team}")

    def display_group_games(self):
        """ Display the group games. """
        print(f"Group: {self.name}")
        for game in self.games:
            print(f"  {game}")
    
    def display_play_game (self):
        for game in self.games:
            game.play()

    def play_group_games (self):
        for game in self