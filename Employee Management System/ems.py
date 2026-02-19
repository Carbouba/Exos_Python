# Importation des modules 
from customtkinter import *
from CTkMessagebox import *
from PIL import Image

import style as s

# Création de la fenêtre principale
dash = CTk()

# Frame principale

# left_frame
left_frame = CTkFrame(dash, 
                      fg_color=s.COLORS["muted"])
left_frame.grid(row=1, column=0, pady=10)

# right_frame
right_frame = CTkFrame(dash, 
                        fg_color=s.COLORS["muted"])
right_frame.grid(row=1, column=1, sticky="w")

# ID zone
id_lbl = CTkLabel(left_frame, text="id", 
                  font=s.FONTS["subtitle"])
id_lbl.grid(row=0, column=0,  padx=(20))

id_entry = CTkEntry(left_frame, 
                         text_color="black",
                         fg_color="white",
                         border_width=2,
                         border_color=s.COLORS["bg"],
                         width=180
                         )
id_entry.grid(row=0, column=1)

# Name zone
name_lbl = CTkLabel(left_frame, text="Nom", 
                  font=s.FONTS["subtitle"])
name_lbl.grid(row=1, column=0,  padx=(20))

name_entry = CTkEntry(left_frame, 
                         text_color="black",
                         fg_color="white",
                         border_width=2,
                         border_color=s.COLORS["bg"],
                         width=180
                         )
name_entry.grid(row=1, column=1)

# prenom zone
prenom_lbl = CTkLabel(left_frame, text="Prénom", 
                  font=s.FONTS["subtitle"])
prenom_lbl.grid(row=2, column=0,  padx=(20))

prenom_entry = CTkEntry(left_frame, 
                         text_color="black",
                         fg_color="white",
                         border_width=2,
                         border_color=s.COLORS["bg"],
                         width=180
                         )
prenom_entry.grid(row=2, column=1)

# phonr zone
phone_lbl = CTkLabel(left_frame, text="Téléphone", 
                  font=s.FONTS["subtitle"])
phone_lbl.grid(row=3, column=0,  padx=(20))

phone_entry = CTkEntry(left_frame, 
                         text_color="black",
                         fg_color="white",
                         border_width=2,
                         border_color=s.COLORS["bg"],
                         width=180
                         )
phone_entry.grid(row=3, column=1)




# Personnalisation de la fenêtre
dash.title("Se connecter")
dash.geometry("930x578")
dash.resizable(0, 0)
dash.configure(fg_color=s.COLORS["bg"])
image = CTkImage(Image.open("bg.jpg"), size=(930,158))
imagelabel = CTkLabel(dash, image=image)
imagelabel.grid(row=0, column=0, columnspan=2)



# Démarrage
# Lance l'application sur le menu principal puis démarre la boucle graphique.
dash.mainloop()