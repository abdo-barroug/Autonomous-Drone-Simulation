import random as r

class DroneAgent:
    
    def __init__(self, EtatEnvironnement):
        self.env = EtatEnvironnement
    
    def takeoff_cmd(self):
        
        e = self.env
        
        #precondition
        if not(e.crashed == 0):
            print("Impossible takeoff: le drone est crashed ")
            return
            
        if not(e.airborne == 0):
            print("Impossible takeoff: le drone est deja airborne")
            return
        
        if not(e.docked == 0):
            print("Impossible takeoff: le drone est docked")
            return
        
        if not(e.battery > 0):
            print("Impossible takeoff: Batterie faible")
            return
        
        # si toute est bien passee
        e.airborne = 1
        
        e.docked = 0
        
        e.update_obstacle_distance()
              
        e.check_invariant()
              
    def move_step(self):
        
        e = self.env
        
        # precondition
        if not(e.crashed == 0):
            print("Impossible move_step: le drone est crashed ")
            return
            
        if not(e.airborne == 1):
            print("Impossible move_step: le drone n'est pas airborne")
            return
        
        if not(e.docked == 0):
            print("Impossible move_step: le drone est docked")
            return
        
        if not(e.battery > 0):
            print("Impossible move_step: Batterie faible")
            return
    
        # calcul voisins valides
        voisins = []

        if e.posY < e.maxY:
            voisins.append((e.posX, e.posY + 1))
        if e.posY > 0:
            voisins.append((e.posX, e.posY - 1))
        if e.posX < e.maxX:
            voisins.append((e.posX + 1, e.posY))
        if e.posX > 0:
            voisins.append((e.posX - 1, e.posY))

        # choix NON déterministe
        nextX, nextY = r.choice(voisins)

        # mise a jour
        e.posX = nextX
        e.posY = nextY
        e.battery -= 1

        e.visZones.add(e.get_zone(nextX, nextY))

        e.update_obstacle_distance()

        e.check_invariant()
        
    # se deplacer en evitant le danger si possible
    # et c'est different de move_step car dans move step on choisit ou aller
    # par contre ici le drone choisit intelligemment
    def avoid_maneuver(self):
        
        e = self.env
        
        # precondition
        if not(e.crashed == 0):
            print("Impossible avoid_maneuver: le drone est crashed ")
            return
            
        if not(e.airborne == 1):
            print("Impossible avoid_maneuver: le drone n'est pas airborne")
            return
        
        if not(e.docked == 0):
            print("Impossible avoid_maneuver: le drone est docked")
            return
        
        if not(e.battery > 1):
            print("Impossible avoid_maneuver : Batterie faible")
            return
        
        # les 4 positions autour du Drone, faut rester dans la grille
        voisins = []
        
        if e.posY < e.maxY: #Haut
            voisins.append((e.posX, e.posY + 1))

        if e.posY > 0: #Bas
            voisins.append((e.posX, e.posY - 1))

        if e.posX < e.maxX: #Droite
            voisins.append((e.posX + 1, e.posY))

        if e.posX > 0: #Gauche
            voisins.append((e.posX - 1, e.posY))
        
        # Trouver les voisins safe
        voisins_surs = []

        for (x, y) in voisins:
            if (x, y) not in e.grille.Danger:
                voisins_surs.append((x, y))
                
                
        # sil existe un voisin safe 
        if voisins_surs :  
            (nextX, nextY) = r.choice(voisins_surs)
            obstacle = 2 #yaura un deplacement
            
        else : #aucun voisin sur
            (nextX, nextY) = r.choice(voisins)
            
            if (nextX, nextY) in e.grille.Danger:
                obstacle = 0
            else:
                obstacle = 2
        
        #update de l'etat
        e.posX = nextX
        e.posY = nextY
        
        e.battery -= 2

        # ajout de la zone visitee
        e.visZones.add(e.get_zone(nextX, nextY))
        
        #Vérification de cohérence
        e.update_obstacle_distance()
        
        e.check_invariant()
        
    def return_home(self):
        e = self.env
        
        #precondition
        if not(e.crashed == 0):
            print("Impossible return_home: le drone est crashed ")
            return
            
        if not(e.airborne == 1):
            print("Impossible return_home: le drone n'est pas airborne")
            return
        
        if not(e.docked == 0):
            print("Impossible return_home: le drone est docked")
            return
        
        if not(e.battery > 0):
            print("Impossible return_home: Batterie faible")
            return
        
        # calcul prochain nextX et nextY
        if e.posX < e.baseX:
            nextX = e.posX + 1
        elif e.posX > e.baseX:
            nextX = e.posX - 1
        else:
            nextX = e.posX

        if e.posY < e.baseY:
            nextY = e.posY + 1
        elif e.posY > e.baseY:
            nextY = e.posY - 1
        else:
            nextY = e.posY
        #alors
        e.posX = nextX
        e.posY = nextY
        e.battery -= 1

        e.visZones.add(e.get_zone(nextX, nextY))
        
        if (nextX,nextY) in e.grille.Danger:
            e.obstacle_distance = 0
        else:
            e.obstacle_distance = 2
            
        #Vérification de cohérence
        e.update_obstacle_distance()
        e.check_invariant()
        
    def dock_cmd(self):
        
        e = self.env
        
        #precondition
        if not(e.crashed == 0):
            print("Impossible dock_cmd: le drone est crashed ")
            return
            
        if not(e.airborne == 1):
            print("Impossible dock_cmd: le drone n'est pas airborne")
            return
        
        if not(e.docked == 0):
            print("Impossible dock_cmd: le drone est deja docked")
            return
        
        if not(e.posX == e.baseX and  e.posY == e.baseY):
            print("Impossible dock_cmd: Pas à la base")
            return
        
        
        # effet
        e.docked = 1
        e.airborne = 0

        e.check_invariant()
    
    def undock_cmd(self):
        e = self.env
        
        #precondition
        if not(e.crashed == 0):
            print("Impossible undock_cmd: le drone est crashed ")
            return
            
        if not(e.docked == 1):
            print("Impossible undock_cmd: le drone n'est pas docked")
            return
        
        if not(e.battery>0):
            print("Impossible undock_cmd: batterie insuffisante")
            return
        
        e.docked = 0
        e.airborne = 1
        
        # ajouter la base aux zones visitees
        e.visZones.add(e.get_zone(e.posX, e.posY))
        
        e.check_invariant()
        
    def charge_step(self):
        
        e = self.env
        #precondition
        
        if(not(e.crashed == 0)):
            print("Impossible charge_step: le drone est crashed ")
            return
        if(not(e.docked == 1)):
            print("Impossible charge_step: le drone n'est pas docked  ")
            return
        #alors
        
        if(e.battery <= 95):
            e.battery += 5
        else:
            e.battery = 100
        
        e.check_invariant()   
        
    def emergency_stop(self):
        e = self.env
        e.crashed = 1
        e.airborne = 0
        e.docked = 0
        e.obstacle_distance = 0
        e.check_invariant()
        
    
