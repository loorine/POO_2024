import numpy as np
from class_case import Case  # Import de la classe Case

class Plateau:
    def __init__(self, taille_x: int, taille_y: int):
        self.taille_x = taille_x
        self.taille_y = taille_y
        self.grille = np.array([[Case() for _ in range(taille_y)] for _ in range(taille_x)])  # Utilisation de Case

    def placer_bombes(self, nb_bombes: int):
        bombes_placees = 0
        while bombes_placees < nb_bombes:
            x = np.random.randint(0, self.taille_x)
            y = np.random.randint(0, self.taille_y)
            if not self.grille[x, y].bombe:
                self.grille[x, y].bombe = True
                bombes_placees += 1

    def get_case(self, x: int, y: int) -> Case:
        if 0 <= x < self.taille_x and 0 <= y < self.taille_y:
            return self.grille[x, y]
        else:
            raise ValueError("Coordonnées hors du plateau")

    def compter_bombe_adjacentes(self, x: int, y: int) -> int:
        bombes_adjacentes = 0
        for i in range(max(0, x - 1), min(self.taille_x, x + 2)):
            for j in range(max(0, y - 1), min(self.taille_y, y + 2)):
                if self.grille[i, j].bombe and (i != x or j != y):
                    bombes_adjacentes += 1
        return bombes_adjacentes
