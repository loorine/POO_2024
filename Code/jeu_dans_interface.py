import sys
from PyQt5.QtWidgets import QApplication
from class_jeu import Jeu
from class_interface import Interface

if __name__ == "__main__" :
    
    app = QApplication(sys.argv)
    jeu = Jeu()  
    interface = Interface(jeu)
    interface.show()
    sys.exit(app.exec_())
