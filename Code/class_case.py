class Case:
    
    def __init__(self):
        """ Conctructeur de la classe. 4 attributs.
            3 booléens pour connaitre l'état de la case
            1 entier qui rpz l'état des cases adjacentes
        """
        self.bombe = False
        self.revelee = False
        self.drapeau = False
        self.nb_bombes_adjacentes = 0

    def placer_drapeau(self):
        """ Méthode pour placer/déplacer un drapeau. """
        self.drapeau = not self.drapeau
    
    def reveler_case(self):
        """ Méthode pour révéler une case. """
        self.revelee = True
        return self.bombe  # Retourne True si c’est une bombe, sinon False