from tkinter import *
from PIL import Image, ImageTk
from datetime import *
import time
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np


class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard")
        self.root.geometry("1366x768")
        self.root.config(bg="#eff5f6" )

        # Icon de la fenetre
        icon = PhotoImage(file="/home/boubacar/Mes_projets_code/Exos_Python/Tableau de bord/icons/sales_sale_supermarket_stock_market_icon_153077.png")
        self.root.iconphoto(True, icon)

        # Entete
        self.entete = Frame(self.root, bg="#009df4")
        self.entete.place(x=300, y=0, width=1070, height=60)

        # Bouton de deconnexion
        self.deconect = Button(self.entete, text="Se deconnecter", font=("Helvetica", 13, "bold"), 
                               bd=0, bg="#32cf8e", fg="white", 
                               cursor="hand2", activebackground="#32cf8e")
        self.deconect.place(x=950, y=15)

        # Menu frame
        self.menu_frame  =Frame(self.root, bg="white")
        self.menu_frame.place(x=0, y=0, width=300, height=750)

        # Logo
        self.logo = Image.open(r"/home/boubacar/Mes_projets_code/Exos_Python/Tableau de bord/icons/round-account-button-with-user-inside_icon-icons.com_72596.png")
        photo = ImageTk.PhotoImage(self.logo)
        self.logo = Label(self.menu_frame, image=photo, bg="white")
        self.logo.image = photo
        self.logo.place(x=100, y=50)

        # Nom de l'utilsateur
        self.nom = Label(self.menu_frame, text="Boubacar", font=("Helvetica", 13, "bold"), bg="white")
        self.nom.place(x=100, y=200)

if __name__=="__main__":
    root = Tk()
    Dashboard(root)
    root.mainloop()
