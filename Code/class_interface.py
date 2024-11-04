from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QInputDialog, QMessageBox, QGridLayout
from class_jeu import Jeu


class Interface(QWidget):
    
    
    def __init__(self, game: Jeu):
        
        """ Initialisation de l'interface graphique. 
            Pleins d'attributs pour que ça ressemble à qqch.
            Prend également en paramètre 'game' de la classe jeu, pour faire la jonction avec le jeu justement.
        """
        
        super().__init__()
        
        # référence à l'instance de Jeu
        self.game = game  
        
        # titre, taille et couleur        
        self.setWindowTitle("DEMINEUR")
        self.resize(400, 400)
        self.setStyleSheet("background-color: lightgray;")
      
        # layout principal
        self.layout_principal = QVBoxLayout()
        
        # label du titre
        self.label = QLabel("DEMINEUR", self)
        self.label.setStyleSheet("color: black; font-size: 32px; font-weight: bold;")
        self.label.setAlignment(Qt.AlignCenter)
        self.layout_principal.addWidget(self.label)

        # bouton pour démarrer une nouvelle partie
        self.bouton_demarrer = QPushButton("Démarrer une nouvelle partie", self)
        self.bouton_demarrer.setStyleSheet("font-size: 18px; padding: 10px;")
        self.bouton_demarrer.clicked.connect(self.lancer_partie)
        self.layout_principal.addWidget(self.bouton_demarrer)

        # layout pour la grille
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(0)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.layout_principal.addLayout(self.grid_layout)

        # appliquer le layout principal à la fenêtre
        self.setLayout(self.layout_principal)      



    def lancer_partie(self):
        """ Méthode pour démarrer la partie. 
            Menu déroulant pour choisir le niveau de difficulté.
        """
        choix, ok = QInputDialog.getItem(
            self, 
            "Choix du niveau","Sélectionnez un niveau de difficulté :",
            ["Facile (10x8, 10 bombes)", "Moyen (18x14, 40 bombes)", "Difficile (24x20, 99 bombes)"], 
            0, False)
        if ok:
            niveau = {'Facile (10x8, 10 bombes)': '1',
                      'Moyen (18x14, 40 bombes)': '2',
                      'Difficile (24x20, 99 bombes)': '3'}.get(choix)
            if niveau:
                self.game.demarrer_partie(niveau)
                reponses = self.game.plateau.afficher_tout()
                self.creer_grille()
                QMessageBox.information(self, "Partie démarrée", "Bonne chance!")
            else:
                print("Choix invalide. La partie ne peut pas commencer.")



    def creer_grille(self):
        """ Méthode qui crée la grille du jeu. """
        # efface les anciens boutons s'il y en a
        for i in reversed(range(self.grid_layout.count())):
            widget = self.grid_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        taille_x = self.game.plateau.taille_x
        taille_y = self.game.plateau.taille_y

        # crée les boutons pour chaque case
        self.boutons_cases = {}
        for x in range(taille_x):
            for y in range(taille_y):
                bouton_case = QPushButton("", self)
                bouton_case.setFixedSize(40, 40)
                bouton_case.setStyleSheet("border: 1px solid black;")
                bouton_case.clicked.connect(lambda checked, bx=x, by=y: self.handle_click(bx, by))
                bouton_case.setContextMenuPolicy(Qt.CustomContextMenu)
                bouton_case.customContextMenuRequested.connect(lambda pos, bx=x, by=y: self.handle_right_click(bx, by))

                self.grid_layout.addWidget(bouton_case, x, y)
                self.boutons_cases[(x, y)] = bouton_case
 
        
 
    def handle_click(self, x, y):
        """ Méthode qui gère les clics sur les cases. """
        if self.game.jeu_en_cours:
            # clic gauche pour révéler
            self.game.clic_gauche(x, y)
            
            # vérifie si la case révélée est une bombe
            case = self.game.plateau.get_case(x, y)
            if case.revelee and case.bombe:
                # affiche une bombe sur le bouton
                self.boutons_cases[(x, y)].setText("💣")  
                self.boutons_cases[(x, y)].setStyleSheet("background-color: red;")
                QMessageBox.warning(self, "Perdu!", "Vous avez touché une bombe!")
                self.game.jeu_en_cours = False  # fin du jeu
            else:
                # vérifie la victoire après le clic gauche
                if self.game.verifier_victoire():
                    QMessageBox.information(self, "Gagné!", "Félicitations, vous avez gagné!")
                    self.game.jeu_en_cours = False  # fin du jeu
            # mise à jour de la grille après le clic
            self.mettre_a_jour_grille()



    def handle_right_click(self, x, y):
        """ Méthode qui gère le clic droit pour placer ou enlever un drapeau."""
        if self.game.jeu_en_cours:
            self.game.clic_droit(x, y)
            self.mettre_a_jour_grille()



    def mettre_a_jour_grille(self):
        """ Méthode qui met à jour l'affichage de la grille en fonction de l'état du jeu.
            Met des couleurs.
        """
        ma_partie = self.game.plateau.tableau_jeu  
        print(ma_partie) # vérification dans la console mais c'est pas obligé
        
        for (x, y), bouton in self.boutons_cases.items():
            case = self.game.plateau.get_case(x, y)
            if case.revelee :
                bouton.setText(str(ma_partie[x][y]))  
                if not case.bombe :
                    bouton.setStyleSheet("background-color: lightyellow;")
            
            elif case.drapeau:
                bouton.setText("🚩")
                bouton.setStyleSheet("background-color: orange;")
            else:
                bouton.setText("")  