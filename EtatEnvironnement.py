class EtatEnvironnement :

    # ils ne vont pas changé lors de l'execution donc on les gardes commes des attributs de classe
    baseX = 6 
    baseY = 6 

    def __init__(self, Longueur, Largeur, ZoneCount, Danger, ZoneOf):
    #les champs
    posX, posY, battery, obstacle_distance, docked, airborne,crashed, visZones

