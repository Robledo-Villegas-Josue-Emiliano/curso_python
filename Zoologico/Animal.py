class Animal :
    def __init__(self,name, id_clase, caracteristica):
        self.name = name
        self.id_clase = id_clase
        self.caracteristica = caracteristica

    def __str__(self):
        return F"El nombre del animal es {self.name} "

    def __repr__(self):
        return F"Animal (name is: {self.name}, Class animal: {self.id_clase})"