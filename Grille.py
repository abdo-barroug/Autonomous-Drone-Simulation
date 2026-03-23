class Grille:
    def __init__(self, Longueur, Largeur):
        self.MaxY = Longueur  # entier c'est le maxY
        self.MaxX = Largeur   # entier c'est le maxX
        self.Danger = {(3,3), (4,5), (5,4)}  # ensemble de couples obstacles
        self.ZoneCount = 4  # nombre de zones dans la grille

    # méthode pour déterminer la zone d'une cellule
    def ZoneOf(self, x, y):
        if x <= 2 and y <= 2:
            return 1
        if x <= 2 and y > 2:
            return 2
        if x > 2 and y <= 2:
            return 3
        if x > 2 and y > 2:
            return 4
        return -1

    # méthode pour afficher la grille
    def afficher(self, droneX=None, droneY=None):
        for y in range(0, self.MaxY + 1):
            for x in range(0, self.MaxX + 1):

                if (x, y) == (droneX, droneY):
                    print("D", end=" ")

                elif (x, y) in self.Danger:
                    print("X", end=" ")

                else:
                    print(".", end=" ")
            print()
