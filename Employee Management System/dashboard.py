# Importation des modules 
from customtkinter import *
from CTkMessagebox import *
from PIL import Image

import style as s

# Création de la fenêtre principale
root = CTk()

# Personnalisation de la fenêtre
root.title("Gestionnaire de stock")
root.geometry("1800x900")
root.resizable(0, 0)
root.configure(fg_color=s.COLORS["bg2"])
# image = CTkImage(Image.open("cover.jpg"), size=(930,500))
# imagelabel = CTkLabel(root, image=image)
# imagelabel.place(x=50 , y=0)

# Titre pricipal
title_frame = CTkFrame(root,
                 fg_color=s.COLORS["blue"],
                 width=1800, height=150,
                 corner_radius=25)
title_frame.place(x=0, y= -25)

titre = CTkLabel(title_frame, 
                 text="Gestionnaire de stock",
                 justify="center", 
                 font=s.FONTS["h1"],
                 text_color=s.COLORS["bg2"], 
                 
                 )
titre.place(x=700, y=75)

# Zone de saisie 
type_zone_frame = CTkFrame(root, 
                           fg_color=s.COLORS["bg"],
                           width=250, height=300,
                           corner_radius=10)
type_zone_frame.place(x=60, y= 160)




# Lance l'application sur le menu principal puis démarre la boucle graphique.
root.mainloop()
