from typing import Literal

class Card:
    # Constructeur
   # pv = point de vie
   # PA = point d'attaque
    def __init__(self, nom: str, tipe: Literal["epique", "legendaire", "rare"] , pV, pA) -> None:
        self.nom = nom
        self.tipe = tipe
        self.pV = pV
        self.pA = pA
        
    def se_presenter(self):
        raise NotImplementedError("Methode non implementer")
    
    def attaquer(self, advers_card: "Card"):

       #advers_card.pV -= self.pA








