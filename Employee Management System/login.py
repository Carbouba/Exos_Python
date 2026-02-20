# Importation des modules 
from customtkinter import *
from CTkMessagebox import *
from PIL import Image

import style as s

# Page de connexion
def login_page():
    if user_name_entry.get() == "" or user_mdp_entry.get() == "":
        #CTkMessagebox(title="Erreur", message="Tous les champs doivent etre remplis", icon="cancel")
        user_name_entry.configure(border_color=s.COLORS["danger_light"])
        user_mdp_entry.configure(border_color=s.COLORS["danger_light"])
        user_name_entry.after(3000, lambda:user_name_entry.configure(border_color="white"))
        user_mdp_entry.after(3000, lambda:user_mdp_entry.configure(border_color="white"))
        msg = CTkLabel(type_zone_frame, 
                 text="Veuillez remplir \ntous les champs", justify="center",
                 font=("Montserrat", 12, "bold"),
                 text_color=s.COLORS["danger"])
        msg.place(x=45, y=180)
        msg.after(3000, lambda: msg.destroy()) # Supprimer le message après 3 secondes
                    
    elif user_name_entry.get() == "adm" and user_mdp_entry.get() == "adm":
        #CTkMessagebox(title="Succés", message=f"Connecter entant que {user_name_entry}", icon="info")
        root.destroy()
        import ems
    else:
        msg = CTkLabel(type_zone_frame, 
                 text="Nom d'utilisateur ou \n mot de passe incorrect", justify="center",
                 font=("Montserrat", 12, "bold"), 
                 text_color=s.COLORS["danger"])
        msg.place(x=33, y=180)
        user_name_entry.delete(0, END)
        user_mdp_entry.delete(0, END)
        msg.after(3000, lambda: msg.destroy()) # Supprimer le message après 3 secondes
        #CTkMessagebox(title="Erreur", message="Nom d'utilisateur ou mot de passe incorrect", icon="cancel")
    
        
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
                         )
user_name_entry.place(x=32, y=50)

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
                      font=s.FONTS["button"],
                      text_color="white", 
                      fg_color=s.COLORS["primary"],
                      hover_color=s.COLORS["primary_hover"],
                      corner_radius=5,
                      cursor="hand2",
                      command=login_page
                      )
login_btn.place(x=32, y=140)

# Démarrage
# Lance l'application sur le menu principal puis démarre la boucle graphique.
root.mainloop()
