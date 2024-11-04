from class_plateau import Plateau


class Jeu:
    
    
    def __init__(self):
        """ Constructeur de la classe. 2 attributs.
            1 plateau
            1 booléen pour savoir si le jeu est en cours ou non
        """
        self.plateau = None
        self.jeu_en_cours = False
     
        

    def demarrer_partie(self, choix):
        """ Lance une nouvelle partie en fonction du niveau de difficulté choisi.
            Le niveau de difficulté définit la taille du plateau et le nombre de bombes.
            Créé également le tableau avec les réponses / la solution du jeu.
        """
        if choix == '1':
            self.plateau = Plateau(10, 8, 10)
            
        elif choix == '2':
            self.plateau = Plateau(18, 14, 40)
            
        elif choix == '3':
            self.plateau = Plateau(24, 20,99)
            
        else:
            print("Choix invalide. La partie ne peut pas commencer.")
            return

        self.plateau.placer_bombes()
        self.jeu_en_cours = True
        print("La partie a commencé! Bonne chance!")
       
        self.verifier_victoire()
        
   
        
    def clic_gauche(self, x: int, y: int):
        
        """ Méthode qui permet de cliquer sur une case pour la révéler.
            Impossible si : la partie est terminée, la case est déjà révélée ou la case possède un drapeau.
            Sinon la case est révélée et si elle n'a pas de bombes adjacentes, cela  déclenche la propagation.
            Si la case révélée est une bombe, ça enclenche la défaite.
        """
           
        if not self.jeu_en_cours:
            print("La partie est déjà terminée.")
            return
        
        case = self.plateau.get_case(x, y)
        
        if case.revelee:
            print("Cette case a déjà été révélée.")
            return
        
        if case.drapeau:
            print("Cette case ne peut pas être révélée car elle porte un drapeau.")
            return
        
        if case.bombe :
            self.plateau.tableau_jeu[x, y] = '💣'
        # si la case cliquée est une bombe, le joueur perd
        if case.reveler_case():
            self.defaite()
        else:
            self.propagation_zero(x, y)  
            
        self.verifier_victoire() 
            


    def propagation_zero(self, x: int, y: int):
        """ Méthode qui affiche les bombes adjacentes pour la case cliquée et propage si aucune bombe n'est adjacente."""
        # marque la case comme révélée 
        self.plateau.tableau_jeu[x, y] = self.plateau.tableau_reponses[x, y]
        case = self.plateau.get_case(x, y)
        case.revelee = True  
    
        # si aucune bombe adjacente, on déclenche la propagation
        if self.plateau.tableau_jeu[x, y] == 0:
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if not (0 <= i < self.plateau.taille_x and 0 <= j < self.plateau.taille_y):
                        continue  # ignore les cases hors du plateau
                    
                    if i == x and j == y:
                        continue  # ignore la case centrale
    
                    case_adj = self.plateau.get_case(i, j)
                    if not case_adj.bombe and not case_adj.drapeau and not case_adj.revelee:
                        self.propagation_zero(i, j)


            
    def clic_droit(self, x: int, y: int):
        
        """ Méthode qui permet de cliquer sur une case pour placer/déplacer un drapeau.
            Impossible si : la partie est terminée, la case est déjà révélée.
            S'il n'y a pas de drapeau, alors ça en place un.
            S'il y a déjà un drapeau, ça l'enlève.
        """
        
        if not self.jeu_en_cours:
            print("La partie est déjà terminée.")
            return
        
        case = self.plateau.get_case(x, y)
        
        if case.revelee:
            print("Cette case est déjà révélée. Impossible de poser un drapeau")
            return
        
        else : 
            case.placer_drapeau()
            
            if case.drapeau :
                self.plateau.tableau_jeu[x, y] = '🚩'
            else :
                self.plateau.tableau_jeu[x, y] = '-'
       
        self.verifier_victoire()                  
             
        
         
    def verifier_victoire(self):
        """ Méthode qui vérifie si le joueur a gagné ou non."""
        for x in range(self.plateau.taille_x):
            for y in range(self.plateau.taille_y):
                case = self.plateau.get_case(x, y)
                if not case.bombe and not case.revelee:
                    return False
        self.victoire()
        return True
    
    

    ### 2 petites méthodes qui permettent d'afficher des messages en cas de victoire/ défaite. Et qui met l'état du jeu en non en cours.
    
    def victoire(self):
        self.jeu_en_cours = False
        print("Félicitations! Vous avez gagné!")


    def defaite(self):
        self.jeu_en_cours = False
        print("Dommage! Vous avez perdu. Une bombe a été déclenchée.")