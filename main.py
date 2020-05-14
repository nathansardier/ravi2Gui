import sys

from PyQt5.QtWidgets import QApplication

from gui import Gui

# auteur : Baudouin Dafflon 2
'''
Question 1: Changer le titre de la fenetre
Question 2: Changer la taille minimale de la fenetre (1280x720)
Question 3: ajouter un menu "fichier" avec 3 actions possible (ouvrir / enregistrer / quitter)
Question 4: Ajouter la description des action dans la "statue bar"

Question 5: ajouter un systeme d'onglet
Question 6: dans l'onglet 1, ajouter un bouton qui ouvre un "input file" pour demander le nom de l'utilisateur
Question 7: dans l'onglet 1, ajouter un label pour afficher le nom de l'utilisateur
Question 8: Changer l'arriere plan de l'onglet 1 avec une image de votre choix

Question 9: dans l'onglet 2, ajouter un tableau a deux colonnes pour enregistrer les carateristiques de l'utilisateur (nom, prenom, date de naissance, sexe, taille poid)
Question 10: dans l'onglet 2, ajouter un bouton "enregistrer" qui enregistre dans un fichier les carateristiques dans un fichier json  


'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Gui()
    sys.exit(app.exec_())