class Animal :
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return F"The name of animal is {self.name} "

    def __repr__(self):
        return F"Animal (name is: {self.name}, Class animal: {self.number})"