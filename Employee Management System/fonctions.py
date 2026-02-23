# Importation des modules 
from logging import root

from customtkinter import *
from CTkMessagebox import *
from PIL import Image
from tkinter import ttk 
import pymysql
import style as s


# def connect_data():
#     try:
#         con = pymysql.connect(host="localhost", user="root", password="")
#         mycursor = con.cursor()
#     except:
#         CTkMessagebox(title="Erreur", message="quelque chose est survenu.")
#         return

#     mycursor.execute("CREATE DATABASE IF NOT EXISTS employee_data")
#     mycursor.execute("USE employee_data")
#     mycursor.execute("CREATE TABLE IF NOT EXISTS data (okId VARCHAR(20), Nom VARCHAR(50), Prenom VARCHAR(20), Telephone VARCHAR(15), Role VARCHAR(50), Genre VARCHAR(20), Salaire(20)")




    # Si les informations sont correctes, ouvrir la page principale
    # Sinon, afficher un message d'erreur
def add_employee(id, name, prenom, phone, role, genre, salaire):
    """Fonction pour ajouter un employé"""
    # Ajouter l'employé à la base de données
    # Afficher un message de succès
    CTkMessagebox(title="Succés", message=f"Employé {name} ajouté avec succès", icon="info")


# connect_data()

