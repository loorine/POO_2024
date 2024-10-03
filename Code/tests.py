from class_plateau import Plateau  
from class_jeu import Jeu

  
    
    # # TEST PLATEAU 
    
    # # Créer un plateau de démineur de 10x10 avec 20 bombes
    # plateau = Plateau(10, 10)
    # plateau.placer_bombes(20)

    # # Simuler un clic sur la case (5, 5)
    # case = plateau.get_case(5, 5)
    # bomb_found = case.reveler_case()  # Révèle la case
    # if bomb_found:
    #     print("BOOM! Vous avez cliqué sur une bombe.")
    # else:
    #    print("La case est sans bombe.")
       
       
    # # TEST JEU 
    # jeu = Jeu(10, 10, 20)  # Créer une nouvelle partie avec un plateau 10x10 et 20 bombes
    # jeu.demarrer_partie()  # Démarrer la partie

    # # Simuler des clics sur des cases
    # jeu.cliquer_case(5, 5)
    # jeu.cliquer_case(2, 3)

    # # Placer un drapeau
    # jeu.placer_drapeau(2, 3)

    # # Continuer à jouer jusqu'à la victoire ou la défaite


1
def main():
    jeu = Jeu()
    jeu.demarrer_partie()  # Démarrer la partie avec la sélection de la difficulté

    while jeu.jeu_en_cours:
        action = input("Voulez-vous 'cliquer' sur une case ou 'placer' un drapeau ? (cliquer/placer) : ").strip().lower()
        
        if action == 'cliquer':
            x = int(input("Entrez la coordonnée x de la case à cliquer : "))
            y = int(input("Entrez la coordonnée y de la case à cliquer : "))
            jeu.cliquer_case(x, y)
        elif action == 'placer':
            x = int(input("Entrez la coordonnée x de la case pour placer un drapeau : "))
            y = int(input("Entrez la coordonnée y de la case pour placer un drapeau : "))
            jeu.placer_drapeau(x, y)
        else:
            print("Action non reconnue. Veuillez entrer 'cliquer' ou 'placer'.")

        # Ici, tu pourrais vérifier si le joueur a gagné ou perdu
        # par exemple :
        # if jeu.nb_bombes == 0:  # ou une autre condition de victoire
        #     jeu.victoire()
        # elif une_condition_de_defaite:
        #     jeu.defaite()

if __name__ == "__main__":
    main()
