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
        
        e.update_obstacle_distance()
              
        e.check_invariant()
              
    def move_step(self, nextX, nextY):
        
        e = self.env
        
        # precondition
        if not(e.crashed == 0):
            print("Impossible move_step: le drone est crashed ")
            return
            
        if not(e.airborne == 1):
            print("Impossible move_step: le drone est deja airborne")
            return
        
        if not(e.docked == 0):
            print("Impossible move_step: le drone est docked")
            return
        
        if not(e.battery > 0):
            print("Impossible move_step: Batterie faible")
            return
            
        # verification de nextX et nextY
        if not(0<= nextX <= e.maxX):
            print("Impossible move_step: nextX argument invalide")
            return
            
        if not(0<= nextY <= e.maxY):
            print("Impossible move_step: nextY argument invalide")
            return
            
        if not((nextX == e.posX and nextY == e.posY + 1 and e.posY < e.maxY)
           or (nextX ==e.posX and nextY == e.posY - 1 and e.posY > 0)
           or (nextX ==e.posX + 1 and nextY == e.posY and e.posX < e.maxX)
           or (nextX == e.posX - 1 and nextY == e.posY and e.posX > 0)):    
                print("Impossible move_step: nextY ou NextX arguments invalides")
                return
        
        #si tt passe bien
        e.posX = nextX
        e.posY = nextY
        e.battery = e.battery - 1
        e.visZones.add(e.get_zone(nextX, nextY))
        
        e.update_obstacle_distance()
            
        e.check_invariant()
   
    def avoid_maneuver(self):
        pass
        
        
        
        
    def return_home(self):
        pass
    def dock_cmd(self):
        pass
    def undock_cmd(self):
        pass
    def charge_step(self):
        pass
    def emergency_stop(self):
        pass
    
