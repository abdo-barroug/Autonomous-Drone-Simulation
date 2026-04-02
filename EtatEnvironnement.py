

class EtatEnvironnement :

    def __init__(self, Grille):
     
        self.baseX = 0
        self.baseY = 0
        
        self.grille = Grille
        self.maxX = Grille.MaxX
        self.maxY = Grille.MaxY
        
        # variables representant la position courante du drone dans la grille
        self.posX = self.baseX # = 0
        self.posY = self.baseY # = 0
        
        # niveau de batterie du drone entre 0 et 100
        self.battery = 100
        
        # represente la distance entre le drone et l'obstacle a chaque position
        self.obstacle_distance = 2
        
        #etat operationnel du drone 1 = True, 0 = False
        self.docked = 0 
        self.airborne = 0
        self.crashed = 0

        # ensemble de zone visite
        self.visZones = {self.grille.ZoneOf(self.posX,self.posY)}
        
        self.check_invariant()
        
    # methode pour verifier les invariants apres chaque mouvement du drone, incluant l'etat initial
    def check_invariant(self):

        assert 0 <= self.posX <= self.maxX, "posX hors limites"
        assert 0 <= self.posY <= self.maxY, "posY hors limites"

        assert 0 <= self.battery <= 100, "battery hors limites"

        assert self.docked in (0,1), "docked invalide"
        assert self.airborne in (0,1), "airborne invalide"
        assert self.crashed in (0,1), "crashed invalide"

        for z in self.visZones:
            assert 1 <= z <= self.grille.ZoneCount, "visZones hors limites"

        # contraintes logiques
        if self.docked == 1:
            assert self.airborne == 0, "docked=1 => airborne=0"
            assert self.posX == self.baseX and self.posY == self.baseY, "docked => position base"

        if self.crashed == 1:
            assert self.airborne == 0, "crashed=1 => airborne=0"
    
    def update_obstacle_distance(self):
        if (self.posX, self.posY) in self.grille.Danger:
            self.obstacle_distance = 0
            self.crashed = 1
            self.airborne = 0
        else:
            self.obstacle_distance = 2
        
    def get_zone(self, x, y):
        return self.grille.ZoneOf(x, y)
    
    def afficher(self):
        self.grille.afficher(self.posX, self.posY)