# Importation des modules 
from customtkinter import *
from CTkMessagebox import *
from PIL import Image
from tkinter import ttk 

import style as s


def add_employee(id, name, prenom, phone, role, genre, salaire):
    """Fonction pour ajouter un employé"""
    # Récupération des données du formulaire
    if id == "" or name == "" or prenom == "" or phone == "" or role == "" or genre == "" or salaire == "" :
        CTkMessagebox(title="Erreur", message="Veuillez remplir tous les champs", icon="cancel")
        id.configure(border_color=s.COLORS["danger_light"])
        name.configure(border_color=s.COLORS["danger_light"])
        prenom.configure(border_color=s.COLORS["danger_light"]) 
        phone.configure(border_color=s.COLORS["danger_light"])
        role.configure(border_color=s.COLORS["danger_light"])
        genre.configure(border_color=s.COLORS["danger_light"])
        salaire.configure(border_color=s.COLORS["danger_light"])
        id.after(3000, lambda: id.configure(border_color=s.COLORS["bg"]))
        name.after(3000, lambda: name.configure(border_color=s.COLORS["bg"]))
        prenom.after(3000, lambda: prenom.configure(border_color=s.COLORS["bg"]))
        phone.after(3000, lambda: phone.configure(border_color=s.COLORS["bg"]))
        role.after(3000, lambda: role.configure(border_color=s.COLORS["bg"]))
        genre.after(3000, lambda: genre.configure(border_color=s.COLORS["bg"]))
        salaire.after(3000, lambda: salaire.configure(border_color=s.COLORS["bg"]))
    