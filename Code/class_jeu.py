from class_plateau import Plateau

class Jeu:
    
    def __init__(self):
        self.plateau = None
        self.nb_bombes = 0
        self.jeu_en_cours = False

    def demarrer_partie(self):
       print("Choisissez un niveau de difficulté :")
       print("1. Facile (10x8, 10 bombes)")
       print("2. Moyen (18x14, 40 bombes)")
       print("3. Difficile (24x20, 99 bombes)")
        
       choix = input("Entrez votre choix (1/2/3) : ")
        
       if choix == '1':
           self.plateau = Plateau(10, 8)
           self.nb_bombes = 10
       elif choix == '2':
            self.plateau = Plateau(18, 14)
            self.nb_bombes = 40
       elif choix == '3':
            self.plateau = Plateau(24, 20)
            self.nb_bombes = 99
       else:
            print("Choix invalide. La partie ne peut pas commencer.")
            return

       self.plateau.placer_bombes(self.nb_bombes)
       self.jeu_en_cours = True
       print("La partie a commencé! Bonne chance!")
        
        
    def cliquer_case(self, x: int, y: int):
        if not self.jeu_en_cours:
            print("La partie est déjà terminée.")
            return
        
        case = self.plateau.get_case(x, y)
        if case.revelee:
            print("Cette case a déjà été révélée.")
            return
        
        if case.reveler_case():  # Si une bombe est révélée
            self.defaite()
        else:
            bombes_adjacentes = self.plateau.compter_bombe_adjacentes(x, y)
            case.nb_bombes_adjacentes = bombes_adjacentes
            print(f"La case révélée contient {bombes_adjacentes} bombes adjacentes.")
            # Ici, tu pourrais ajouter de la logique pour révéler des cases adjacentes si besoin

    def placer_drapeau(self, x: int, y: int):
        case = self.plateau.get_case(x, y)
        case.placer_drapeau()
        drapeau_status = "placé" if case.drapeau else "retiré"
        print(f"Drapeau {drapeau_status} sur la case ({x}, {y}).")

    def victoire(self):
        self.jeu_en_cours = False
        print("Félicitations! Vous avez gagné!")

    def defaite(self):
        self.jeu_en_cours = False
        print("Dommage! Vous avez perdu. Une bombe a été déclenchée.")
