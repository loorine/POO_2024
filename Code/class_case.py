class Case:
    def __init__(self):
        self.bombe = False
        self.revelee = False
        self.drapeau = False
        self.nb_bombes_adjacentes = 0

    def placer_drapeau(self):
        self.drapeau = not self.drapeau

    def reveler_case(self):
        if not self.drapeau:
            self.revelee = True
            return self.bombe
        else:
            raise ValueError("Impossible de révéler la case, un drapeau est présent.")
