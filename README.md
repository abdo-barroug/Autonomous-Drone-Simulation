# Projet-MNAI
Ce dépôt Git est consacré au projet de MNAI visant à implémenter un environnement d’apprentissage par renforcement (RL) simulant le comportement d’un drone autonome de patrouille.


# Avancement sur le Projet
DAY : 2/9/2026
intialisation du projet, 1ere conception du projet, petite implementation de la classe Grille
=> pour tester la classe Grille il suffit de lancer la commande suivante sur le terminal : python .\Grille.py, oubliez pas de se placer dans le dossier MNAI
Autrement on peut utiliser l'icon "play" on the top right corner de VSCode

DAY : 03/23/2026
- Mise en place d’une architecture orientée objet :
    - EtatEnvironnement → état du drone
    - DroneAgent → actions du drone
    - Grille → environnement
- Implémentation des premières actions :
    décollage (takeoff_cmd)
    déplacement (move_step)
- Ajout des invariants pour vérifier la cohérence
- Création d’une simulation (main.py)
- Ajout d’un affichage de la grille avec le drone (D) qui se déplace

=> pour tester sur le terminal, "python3 main.py"
ou autrement on peut utiliser l'icon "play" on the top right corner de VSCode