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
                game = Game (self.teams[i], self.teams[j])
                self.games.append(games)

    def __str__(self):
        """String representation of the group class."""
        return f"Group: {self.name}, Teams: {self-self.teams}"
    
    def __repr__(self):
        