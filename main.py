from EtatEnvironnement import EtatEnvironnement
from DroneAgent import DroneAgent
from Grille import Grille

def main():
    g = Grille(5, 5)
    env = EtatEnvironnement(g)
    agent = DroneAgent(env)

    print("=== ETAT INITIAL ===")
    env.afficher()

    print("\n=== DECOLLAGE ===")
    agent.takeoff_cmd()
    env.afficher()

    print("\n=== MOVE DROITE ===")
    agent.move_step(env.posX + 1, env.posY)
    env.afficher()

    print("\n=== MOVE DROITE ===")
    agent.move_step(env.posX + 1, env.posY)
    env.afficher()

    print("\n=== MOVE HAUT ===")
    agent.move_step(env.posX, env.posY + 1)
    env.afficher()

    print("\n=== ETAT FINAL ===")
    print("Position :", env.posX, env.posY)
    print("Zones visitées :", env.visZones)
    print("Obstacle distance :", env.obstacle_distance)
    print("Crash :", env.crashed)


if __name__ == "__main__":
    main()