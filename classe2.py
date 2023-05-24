class animal:
    def __init__(self, race, milieu_vie, types, nbre_pattes, forme, couleur, cri, force ):
        self.race = race
        self.milieu_vie = milieu_vie
        self.types = types
        self.nbre_pattes = nbre_pattes
        self.forme = forme
        self.couleur = couleur
        self.cri = cri
        self.force = force
        
    def make_cri(self):
        print(self.cri)
    def attack(self, cible):

        print(self.force)
    def move(self):
        print("J'avance d'un pas")