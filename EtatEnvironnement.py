class EtatEnvironnement :

    # ils ne vont pas changé lors de l'execution donc on les gardes commes des attributs de classe
    # baseX et baseY representent la position depuis laquelle le drone a decolle / peut se recharger
    baseX = 0 
    baseY = 0 

    def __init__(self, maxX, maxY, ZoneCount, Danger, ZoneOf):
        
        self.maxX = maxX
        self.maxY = maxY
        self.zoneOf = ZoneOf
        
        # variables representant la position courante du drone dans la grille
        self.posX = self.baseX
        self.posY = self.baseY 
        
        # niveau de batterie du drone entre 0 et 100
        self.battery = 100
        
        # represente la distance entre le drone et l'obstacle a chaque position
        self.obstacle_distance = 0
        
        #etat operationnel du drone 1 = True, 0 = False
        self.docked = 1 
        self.airborne = 0
        self.crashed = 0

        # ensemble de zone visite
        self.visZones = {ZoneOf(self.posX,self.posY)}
        
        self.check_invariant()
        
    # methode pour verifier les invariants apres chaque mouvement du drone, incluant l'etat initial
    def check_invariant(self):
        if not(0 <= self.posX <= self.maxX):
            print("posX hors limites")
            
        if not(0 <= self.posY <= self.maxY):
            print("posY hors limites")
        
        if not(0 <= self.battery <= 100):
            print("battery hors limites")
        
        if not((self.docked in (0,1)) & (self.airborne in (0,1)) & (self.crashed in (0,1))):
            print("etat invalide")
        
        if not all(self.visZone in self.ZoneCount):
            print("visZone hors limites")
            
        if (self.docked == 1):
            if (self.airborne != 0):
                print("docked = 1 => airborne = 0")
            if (self.posX != self.baseX or self.posY != self.baseY):
                print("docked = 1 ⇒ posX = baseX ∧ posY = baseY")
                
            
        
        

             



