import numpy as np
from class_case import Case 


class Plateau:
    
    
    def __init__(self, taille_x: int, taille_y: int, nb_bombes: int):
        
        """ Constructeur de la classe. 6 attributs.
            2 entiers pour donner la taille du plateau de jeu.
            1 autre entier qui rpz le nombre de bombes sur le plateau.
            1 tableau numpy qui rpz le plateau (qui donne x*y cases).
            2 autres tableaux numpy, un avec la solution et un qui rpz l'avancement de la partie.
        """
        
        # la taille et le nb de bombes vont dépendre du niveau de jeu choisi
        self.taille_x = taille_x
        self.taille_y = taille_y
        self.nb_bombes = nb_bombes
        
        # création du plateau via utilisation de la classe Case :
        self.grille = np.array([[Case() for _ in range(taille_y)] for _ in range(taille_x)])  
        
        # tableau des réponses et tableau de l'avancement de la partie
        self.tableau_reponses = np.empty((self.taille_x, self.taille_y), dtype=object)
        self.tableau_jeu = np.full((self.taille_x, self.taille_y),'-', dtype=object)



    def placer_bombes(self):
        """ Méthode pour placer des bombes de manière aléatoire sur le plateau de jeu. """
        # Une amélioration pourrait être de changer le code de cette fonction pour que le premier clic soit forcément un zéro.
        bombes_placees = set()
        while len(bombes_placees) < self.nb_bombes:
            x, y = np.random.randint(0, self.taille_x), np.random.randint(0, self.taille_y)
            bombes_placees.add((x, y))
        
        for x, y in bombes_placees:
            # l'attribut 'bombe' des cases concernées bascule en True :
            self.grille[x, y].bombe = True 



    def get_case(self, x: int, y: int) -> Case:
        """ Méthode pour accéder à une case via ses coordonées sur le plateau.
            Paramètres : x et y, 2 entiers
        """
        if 0 <= x < self.taille_x and 0 <= y < self.taille_y:
            return self.grille[x, y]
        else:
            raise ValueError("Coordonnées hors du plateau")
            

                    
    def compter_bombe_adjacentes(self, x: int, y: int) -> int:
        """ Méthode qui compte et retourne le nombre de bombes adjacentes pour la case donnée. """
        count = 0
        for i in range(max(0, x - 1), min(self.taille_x, x + 2)):
            for j in range(max(0, y - 1), min(self.taille_y, y + 2)):
                if self.grille[i, j].bombe and (i != x or j != y):
                    count += 1
        # enregistre ce nombre dans la case pour d'autres utilisations
        self.grille[x, y].nb_bombes_adjacentes = count
        return count
        
    

    def afficher_tout(self) -> np.ndarray:
        """ Méthode qui affiche les réponses, càd les bombes et les nombres de bombes adjacentes.
            En gros ça met à jour l'attribut self.tableau_reponses.
            Cette méthode est principalement là pour que ce soit plus facile de faire des tests. 
        """    
        for x in range(self.taille_x):
            for y in range(self.taille_y):
                case = self.grille[x, y]
                if case.bombe:
                    self.tableau_reponses[x, y] = '💣'  
                else:
                    self.tableau_reponses[x, y] = self.compter_bombe_adjacentes(x, y)
        return self.tableau_reponses