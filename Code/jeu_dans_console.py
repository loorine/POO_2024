### DEROULEMENT D'UNE PARTIE DANS LA CONSOLE ###

from class_jeu import Jeu 


if __name__ == "__main__" :
        
    # instanciation de la classe jeu    
    jeu = Jeu()
    
    # choix de la difficulté 
    choix = input("Choisissez une difficulté (1: Facile, 2: Moyen, 3: Difficile): ")
    
    # démarrage de la partie
    jeu.demarrer_partie(choix)
    
    # création du tableau de réponses et du tableau de la partie
    reponses = jeu.plateau.afficher_tout()
    ma_partie = jeu.plateau.tableau_jeu
    
    
    # déroulement du jeu
    while jeu.jeu_en_cours :
        
        # affichage de l'avancement de la partie
        for ligne in ma_partie:
            print(" | ".join(f"{val:>3}" for val in ligne))
        
        # choix de la case
        choix_x = int(input("coordonnée x ?"))
        choix_y = int(input("coordonnée y ?"))
    
        # choix de l'action à effectuer
        choix2 = input("reveler / drapeau ? (1: reveler, 2 : drapeau) ")
    
        # appel aux méthodes de jeu
        if choix2== '1' :
            jeu.clic_gauche(choix_x, choix_y)
        if choix2 == '2' :
            jeu.clic_droit(choix_x, choix_y)
            
    # boucle jusqu'à ce que le joueur ait perdu ou gagné !
        
