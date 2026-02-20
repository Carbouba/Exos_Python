# Importation des modules 
from customtkinter import *
from CTkMessagebox import *
from PIL import Image
from tkinter import ttk 

import style as s


def add_employee(id, name, prenom, phone, role, genre, salaire):
    """Fonction pour ajouter un employé"""
    # Ajouter l'employé à la base de données
    # Afficher un message de succès
    CTkMessagebox(title="Succés", message=f"Employé {name} ajouté avec succès", icon="info")

    