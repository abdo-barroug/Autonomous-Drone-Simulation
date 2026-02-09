class Grille:
    def __init__(self, Longueur, Largeur, ZoneCount, Danger, ZoneOf):
        self.Longueur = Longueur # entier 
        self.Largeur = Largeur #entier
        self.Danger = Danger #c'est un ensemble de couple, chaque couple represente les coordonnes d'un obstacle
        self.ZoneCount = ZoneCount # entier, le nombre de zone dans la grille
        self.ZoneOf = ZoneOf # les apparetence aux ZONES

#je pense à consacrer cette classe pour faire un affichage de la grille  
