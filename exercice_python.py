class Player:
    def __init__(self, nom, point_de_vie, point_d_attaque, arme):
        if type (nom) is not str: 
            raise TypeError
        if type (point_de_vie) is not int:
            raise TypeError
        if type (point_d_attaque) is not int:
            raise TypeError
        if type (arme) is not str: 
            raise TypeError
        self.nom = nom
        self.point_de_vie = point_de_vie
        self.point_d_attaque = point_d_attaque
        self.arme = arme

    def __repr__(self):
        print(f"le score après attaque est \n nom:{self.nom} \n point_de_vie:{self.point_de_vie} \n point_d_attaque:{self.point_d_attaque} ")

    #def SePresenter(self):
        #print(f"le score après attaque est \n nom:{self.nom} \n point_de_vie:{self.point_de_vie} \n point_d_attaque:{self.point_d_attaque} ")
       # print("nom: " + str(self.nom)+ "\n") 
        #print("votre point de vie avant attaque est " + str(self.point_de_vie) +"\n")
        #print("votre score après attaque est " + str(self.point_d_attaque)+"\n")
       # print("votre arme est " + str(self.arme) + "\n")

    def FaceToface(self, Player2):
        Player2.point_de_vie -= 1
        return(f"Votre point d'Attaquer est {Player2.point_de_vie}")
    def Attaquer(self, player3): 
       if(self.type_arme == rapprocher):
           self.FaceToface



joueur1 = Player("yasmine", 7, 3, "fusil")
joueur2 = Player("aka", 17, 7, "fusil")


print(joueur1.__repr__())
print(joueur2.__repr__())
print(joueur1.FaceToface(joueur2))
 




class Weapon:
    def __init__(self, nom,degat, typ):
        self.nom = nom
        self.degat = degat
        self.typ = typ
    def PresenterArme(self):
        print("nom" + self.nom)
        print("degat" + self.degat)
joueur3 = Player("amenan", 3, 3, "fusil")
   




        
      
    









