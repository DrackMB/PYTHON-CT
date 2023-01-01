class Animal():
    nom=""
    age=0
    def __init__(self,nom,age):
        self.nom = nom
        self.age=age
    
    def cri(self):
        print("je suis dans animal")

class Chat(Animal):
    def __init__(self,nom,age):
        super().__init__(nom,age)
    def cri(self):
        print("Miaou")
   
class Chien(Animal):
    def __init__(self,nom,age):
        super().__init__(nom,age)
    def cri(self):
        print("Ouaf")    
        
class Ferme():
    def __init__(self,animaux=[]):
        self.animaux=animaux
        
    def ajouter_animal(self,animal):
        self.animaux.append(animal)
         
    def crier(self):
        if len(self.animaux)==0:
            return print ("Ma ferme a",len(self.animaux),"animaux")
        else: 
            for animal in self.animaux:
                animal.cri()  