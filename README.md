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

DAY : 04/02/2026

Améliorations de conformité avec la spécification :

- Correction des invariants :
    passage des print à des assert pour mieux vérifier la cohérence de l’état

- Correction de move_step :
    ajout d’un comportement non déterministe (choix aléatoire d’un voisin)

- Corrections mineures :
    correction de quelques messages d’erreur
    suppression de mises à jour inutiles de obstacle_distance

- Gestion du danger :
    ajout d’un crash automatique si le drone passe sur une zone dangereuse

- Amélioration de la cohérence :
    meilleure gestion des états (ex : airborne => docked = 0)


# Ce qui reste à faire :

Ce qu’il reste à faire :

- Implémenter le mode interactif
- Implémenter le mode automatique (séquence d’actions)
- Implémenter le mode exhaustif (exploration des états avec DFS)

- Rédiger les documents demandés :
    - manuel développeur
    - manuel utilisateur
    - rapport final