# Importation des modules 
from customtkinter import *
from CTkMessagebox import *
from PIL import Image
from tkinter import ttk 

# importation des style et des fonctions
import style as s
from fonctions import add_employee

""" Fonction qui verifie si les champs du formulaire sont vides ou pas, 
si oui elle affiche un message d'erreur et met en surbrillance les champs vides, 
sinon elle ajoute l'employé à la base de données et affiche un message de succès. """

def check_fields_impty():
    # Récupération des données du formulaire
    # si un champ est vide, afficher un message d'erreur et mettre en surbrillance les champs vides
    if id_entry.get() == "" or name_entry.get() == "" or prenom_entry.get() == "" or phone_entry.get() == "" or role_combx.get() == "" or genre_combx.get() == "" or salaire_entry.get() == "" :
        CTkMessagebox(title="Erreur", message="Veuillez remplir tous les champs", icon="cancel")
        # Mettre en surbrillance les champs vides
        id_entry.configure(border_color=s.COLORS["danger_light"])
        name_entry.configure(border_color=s.COLORS["danger_light"])
        prenom_entry.configure(border_color=s.COLORS["danger_light"]) 
        phone_entry.configure(border_color=s.COLORS["danger_light"])
        role_combx.configure(border_color=s.COLORS["danger_light"])
        genre_combx.configure(border_color=s.COLORS["danger_light"])
        salaire_entry.configure(border_color=s.COLORS["danger_light"])
        # Après 3 secondes, réinitialiser la couleur des bordures
        id_entry.after(3000, lambda: id_entry.configure(border_color=s.COLORS["bg"]))
        name_entry.after(3000, lambda: name_entry.configure(border_color=s.COLORS["bg"]))
        prenom_entry.after(3000, lambda: prenom_entry.configure(border_color=s.COLORS["bg"]))
        phone_entry.after(3000, lambda: phone_entry.configure(border_color=s.COLORS["bg"]))
        role_combx.after(3000, lambda: role_combx.configure(border_color=s.COLORS["bg"]))
        genre_combx.after(3000, lambda: genre_combx.configure(border_color=s.COLORS["bg"]))
        salaire_entry.after(3000, lambda: salaire_entry.configure(border_color=s.COLORS["bg"]))

    else:
        add_employee(id_entry.get(), name_entry.get(), prenom_entry.get(), phone_entry.get(), role_combx.get(), genre_combx.get(), salaire_entry.get())

# Création de la fenêtre principale
dash = CTk()

# Personnalisation de la fenêtre
dash.title("Se connecter")
dash.geometry("930x650+100+100")
dash.resizable(0, 0)
dash.configure(fg_color=s.COLORS["muted"])
image = CTkImage(Image.open("bg.jpg"), size=(930,158))
imagelabel = CTkLabel(dash, image=image)
imagelabel.grid(row=0, column=0, columnspan=2)

###################################################################################
# Frame principale

# left_frame
left_frame = CTkFrame(dash, 
                      fg_color=s.COLORS["muted"])
left_frame.grid(row=1, column=0, pady=10)

# right_frame
right_frame = CTkFrame(dash, 
                        fg_color=s.COLORS["surface"])
right_frame.grid(row=1, column=1, padx=(5, 20))

# Buttom frame
buttom_frame = CTkFrame(dash, fg_color=s.COLORS["muted"])
buttom_frame.grid(row=2, column=0, columnspan=2)

###################################################################################
# ID zone
id_lbl = CTkLabel(left_frame, text="id", 
                  font=s.FONTS["label"])
id_lbl.grid(row=0, column=0,  padx=10, pady=15, sticky="w")

id_entry = CTkEntry(left_frame, 
                         text_color="black",
                         fg_color="white",
                         border_width=2,
                         border_color=s.COLORS["bg"],
                         width=120
                         )
id_entry.grid(row=0, column=1)

# Name zone
name_lbl = CTkLabel(left_frame, text="Nom", 
                  font=s.FONTS["label"])
name_lbl.grid(row=1, column=0,  padx=10, pady=15, sticky="w")

name_entry = CTkEntry(left_frame, 
                         text_color="black",
                         fg_color="white",
                         border_width=2,
                         border_color=s.COLORS["bg"],
                         width=120
                         )
name_entry.grid(row=1, column=1)

# prenom zone
prenom_lbl = CTkLabel(left_frame, text="Prénom", 
                  font=s.FONTS["label"])
prenom_lbl.grid(row=2, column=0,  padx=10, pady=15, sticky="w")

prenom_entry = CTkEntry(left_frame, 
                         text_color="black",
                         fg_color="white",
                         border_width=2,
                         border_color=s.COLORS["bg"],
                         width=120
                         )
prenom_entry.grid(row=2, column=1)

# phone zone
phone_lbl = CTkLabel(left_frame, text="Téléphone", 
                  font=s.FONTS["label"])
phone_lbl.grid(row=3, column=0,  padx=10, pady=15, sticky="w")

phone_entry = CTkEntry(left_frame, 
                         text_color="black",
                         fg_color="white",
                         border_width=2,
                         border_color=s.COLORS["bg"],
                         width=120
                         )
phone_entry.grid(row=3, column=1)

# role zone
roles = ["Desigenr", "Developpeur", "Agent de terrain", "Superviseur"]
role_lbl = CTkLabel(left_frame, text="Rôle", 
                  font=s.FONTS["label"])
role_lbl.grid(row=4, column=0,  padx=10, pady=15, sticky="w")

role_combx = CTkComboBox(left_frame, 
                         values=roles, 
                         text_color="black",
                         fg_color="white",
                         border_width=2,
                         border_color=s.COLORS["bg"],
                         width=120,
                         state="readonly"
                         )
role_combx.grid(row=4, column=1)
role_combx.set("Selectionner")

# genre zone
genre = ["Homme", "Femme"]
genre_lbl = CTkLabel(left_frame, text="Sexe", 
                  font=s.FONTS["label"])
genre_lbl.grid(row=5, column=0,  padx=10, pady=15, sticky="w")

genre_combx = CTkComboBox(left_frame, 
                         values=genre, 
                         text_color="black",
                         fg_color="white",
                         border_width=2,
                         border_color=s.COLORS["bg"],
                         width=120,
                         state="readonly",
                         )
genre_combx.grid(row=5, column=1)
genre_combx.set("Homme")

# salaire zone
salaire_lbl = CTkLabel(left_frame, text="Salaire", 
                  font=s.FONTS["label"])
salaire_lbl.grid(row=6, column=0,  padx=10, pady=15, sticky="w")

salaire_entry = CTkEntry(left_frame, 
                         text_color="black",
                         fg_color="white",
                         border_width=2,
                         border_color=s.COLORS["bg"],
                         width=120
                         )
salaire_entry.grid(row=6, column=1)


###################################################################################

# Search by
searchby_option = ["id", "Nom", "Prénom", "Téléphone", "Genre", "Salaire"]
searchby_combx = CTkComboBox(right_frame, 
                         values=searchby_option, 
                         text_color="black",
                         fg_color="white",
                         border_width=2,
                         border_color=s.COLORS["muted"],
                         width=180,
                         state="readonly",
                         )
searchby_combx.grid(row=0, column=0)
searchby_combx.set("Rechercher selon")

# salaire zone
serach_entry = CTkEntry(right_frame, 
                         text_color="black",
                         fg_color="white",
                         border_width=2,
                         border_color=s.COLORS["muted"],
                         width=130
                         )
serach_entry.grid(row=0, column=1)

search_btn = CTkButton(right_frame, 
                       text="Rechercher",
                       font=s.FONTS["label"],
                       text_color="white", 
                       fg_color=s.COLORS["primary"],
                       hover_color=s.COLORS["primary_hover"],
                       corner_radius=5,
                       cursor="hand2",
                       width=130
                       )
search_btn.grid(row=0, column=2, pady=10)

showall_btn = CTkButton(right_frame, 
                       text="Afficher tout",
                       font=s.FONTS["label"],
                       text_color="white", 
                       fg_color=s.COLORS["primary"],
                       hover_color=s.COLORS["primary_hover"],
                       corner_radius=5,
                       cursor="hand2",
                       width=130
                       ) 
showall_btn.grid(row=0, column=3)

""" triple vue elle affiche les données de la base de données dans une table avec des colonnes id, nom, prenom, téléphone, genre et salaire.
Elle est configurée pour n'afficher que les en-têtes de colonnes et pas les données, 
et elle a une barre de défilement verticale pour permettre à l'utilisateur de faire défiler les données 
si elles dépassent la hauteur de la table. Les colonnes sont centrées et ont une largeur spécifique pour améliorer la lisibilité des données affichées. """
triple_vue = ttk.Treeview(right_frame, height=10)
triple_vue.grid(row=1, columnspan=4)
triple_vue["columns"] = ["id", "Nom", "Prénom", "Téléphone", "Genre", "Salaire"]

# Configuration des en-têtes de colonnes et des propriétés de la table
triple_vue.heading("id", text="id")
triple_vue.heading("Nom", text="Nom")
triple_vue.heading("Prénom", text="Prénom")
triple_vue.heading("Téléphone", text="Téléphone")
triple_vue.heading("Genre", text="Genre")
triple_vue.heading("Salaire", text="Salaire")

# Affichage des en-têtes de colonnes uniquement, sans les données
triple_vue.config(show="headings")

# Configuration de la barre de défilement verticale pour la table
style = ttk.Style()

# Configuration du thème pour la table
style.theme_use("clam")
style.configure("triple-vue", font=s.FONTS["label"])

# Configuration de la barre de défilement verticale pour la table
scroll_bar = ttk.Scrollbar(right_frame, orient=VERTICAL)
scroll_bar.grid(row=1, column=4, sticky="ns")

triple_vue.column("id", anchor=CENTER, width=100)
triple_vue.column("Nom", anchor=CENTER, width=120)
triple_vue.column("Prénom", anchor=CENTER, width=100)
triple_vue.column("Téléphone", anchor=CENTER, width=150)
triple_vue.column("Genre", anchor=CENTER, width=100)
triple_vue.column("Salaire", anchor=CENTER, width=120)

######################################################################################
new_btn = CTkButton(buttom_frame, 
                       text="Nouveau employer",
                       font=s.FONTS["label"],
                       text_color="white", 
                       fg_color=s.COLORS["primary"],
                       hover_color=s.COLORS["primary_hover"],
                       corner_radius=5,
                       cursor="hand2",
                       width=130
                       ) 
new_btn.grid(row=0, column=0, padx=10, pady=5)

add_btn = CTkButton(buttom_frame, 
                       text="Ajouter un employer",
                       font=s.FONTS["label"],
                       text_color="white", 
                       fg_color=s.COLORS["primary"],
                       hover_color=s.COLORS["primary_hover"],
                       corner_radius=5,
                       cursor="hand2",
                       width=130,
                       command=check_fields_impty
                       ) 
add_btn.grid(row=0, column=1, padx=10, pady=5)

updt_btn = CTkButton(buttom_frame, 
                       text="Mettre à jour",
                       font=s.FONTS["label"],
                       text_color="white", 
                       fg_color=s.COLORS["primary"],
                       hover_color=s.COLORS["primary_hover"],
                       corner_radius=5,
                       cursor="hand2",
                       width=130
                       ) 
updt_btn.grid(row=0, column=2, padx=10, pady=5)

del_btn = CTkButton(buttom_frame, 
                       text="Supprimer un emplyer",
                       font=s.FONTS["label"],
                       text_color="white", 
                       fg_color=s.COLORS["primary"],
                       hover_color=s.COLORS["primary_hover"],
                       corner_radius=5,
                       cursor="hand2",
                       width=130
                       ) 
del_btn.grid(row=0, column=3, padx=10, pady=5)

del_all_btn = CTkButton(buttom_frame, 
                       text="Supprimer tous",
                       font=s.FONTS["label"],
                       text_color="white", 
                       fg_color=s.COLORS["primary"],
                       hover_color=s.COLORS["primary_hover"],
                       corner_radius=5,
                       cursor="hand2",
                       width=130
                       ) 
del_all_btn.grid(row=0, column=4, padx=10, pady=5)


# Démarrage
# Lance l'application sur le menu principal puis démarre la boucle graphique.
dash.mainloop()