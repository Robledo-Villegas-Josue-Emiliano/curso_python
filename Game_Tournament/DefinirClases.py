class Athlete:
    """Athlete class, with only name attribute"""
    def __init__(self,name):
        """Custom factory function of class Athlete, receives name"""
        self.name = name

    def __str__(self):
        """String representation of the Athlete object."""
        return F"Athlete name is {self.name}"
    
    def __repr__(self):
        return F"Athlete name is {self.name}, Number: {self.number}"

if __name__=="__main__":
  Athlete1 = Athlete("Lionel Messi")
  Athlete1.number = 10
  print ( Athlete1)
  print(repr(Athlete1))