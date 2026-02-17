import random

class Athlete:
    """Athlete class, with only name attribute"""
    def __init__(self,name):
        """Custom factory function of class Athlete, receives name"""
        self.name = name
        self.number = random.randint (1,99) 
        # Assign a random number to the athlete 

    def __str__(self):
        """String representation of the Athlete object."""
        return F"Athlete name is {self.name}"
    
    def __repr__(self):
        return F"Athlete (name is {self.name}, Number: {self.number})"
    
    def set_number(self, number):
        """Set the athelete´s number."""
        self.number = number

    def to_json (self):
        """Generate json of Athlete"""
        return {
            "name":self.name, 
            "number":self.number
            }
    
if __name__=="__main__":
  Athlete1 = Athlete("Lionel Messi")
  Athlete1.set_number = 10
  print ( Athlete1)
  print(repr(Athlete1))
  