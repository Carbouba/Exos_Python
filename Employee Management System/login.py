# Importation des modules 
from customtkinter import *
from CTkMessagebox import *
from PIL import Image

import style as s


# Création de la fenêtre principale
root = CTk()

# Frame principale
# main_frame = ctk.CTkFrame(root, fg_color=COLORS["bg"])
# main_frame.pack(expand=True, fill="both")


# Personnalisation de la fenêtre
root.title("Se connecter")
root.geometry("930x478")
root.resizable(0, 0)
root.configure(fg_color=s.COLORS["surface"])
image = CTkImage(Image.open("cover.jpg"), size=(930,478))
imagelabel = CTkLabel(root, image=image)
imagelabel.place(x=50 , y=0)

# Titre pricipal
titre = CTkLabel(root, 
                 text="Systéme de gestion\nd'employer",
                 justify="center", 
                 font=s.FONTS["title"],
                 text_color=s.COLORS["primary"],
                 bg_color=s.COLORS["surface"]
                 )
titre.place(x=55, y=100)


# Zone de saisie 
type_zone_frame = CTkFrame(root, 
                           fg_color=s.COLORS["bg"],
                           width=200, height=230,
                           corner_radius=10)
type_zone_frame.place(x=60, y= 180)

titre_label = CTkLabel(type_zone_frame, 
                       text="Connexion",
                       text_color=s.COLORS["primary"],
                       font=s.FONTS["title"],
                       
                       ).place(x=35, y=8)

user_name_entry = CTkEntry(type_zone_frame, 
                         placeholder_text="Nom d'utilisateur",
                         text_color="black",
                         fg_color="white",
                         border_width=2,
                         border_color=s.COLORS["bg"],
                         ).place(x=32, y=50)

user_mdp_entry = CTkEntry(type_zone_frame, 
                         placeholder_text="mot de passe", show="*",
                         text_color="black",
                         fg_color="white",
                         border_width=2,
                         border_color=s.COLORS["bg"],
                         )
user_mdp_entry.place(x=32, y=90)

login_btn = CTkButton(type_zone_frame, 
                      text="Se connecter",
                      text_color="white", 
                      fg_color=s.COLORS["primary"],
                      hover_color=s.COLORS["primary_hover"],
                      corner_radius=5,
                      cursor="hand2"
                      )
login_btn.place(x=32, y=140)

# Démarrage
# Lance l'application sur le menu principal puis démarre la boucle graphique.
root.mainloop()
