# Importation des modules 
from customtkinter import *
from CTkMessagebox import *
from PIL import Image

import style as s

def sign_up_page():
    root.destroy()
    import sign_up_auth_page 

# Page de connexion
def login_infos_check():
    if user_name_entry.get() == "" or user_mdp_entry.get() == "":
        user_name_entry.configure(border_color=s.COLORS["danger_light"])
        user_mdp_entry.configure(border_color=s.COLORS["danger_light"])
        user_name_entry.after(3000, lambda:user_name_entry.configure(border_color="white"))
        user_mdp_entry.after(3000, lambda:user_mdp_entry.configure(border_color="white"))
        msg = CTkLabel(type_zone_frame, 
                 text="Veuillez remplir tous les champs", justify="center",
                 font=("Roboto", 13),
                 text_color=s.COLORS["danger_light"])
        msg.place(x=33, y=245)
        msg.after(3000, lambda: msg.destroy()) # Supprimer le message après 3 secondes
                    
    elif user_name_entry.get() == "adm" and user_mdp_entry.get() == "adm":
        root.destroy()
        import ems
    else:
        msg = CTkLabel(type_zone_frame, 
                 text="Nom d'utilisateur ou \n mot de passe incorrect", justify="center",
                 font=("Roboto", 13),
                 text_color=s.COLORS["danger_light"])
        msg.place(x=53, y=250)

        user_name_entry.delete(0, END)
        user_mdp_entry.delete(0, END)
        msg.after(3000, lambda: msg.destroy()) # Supprimer le message après 3 secondes

# Création de la fenêtre principale
root = CTk()

# Personnalisation de la fenêtre
root.title("Se connecter")
root.geometry("930x578")
root.resizable(0, 0)
root.configure(fg_color=s.COLORS["surface"])
image = CTkImage(Image.open("cover.jpg"), size=(930,500))
imagelabel = CTkLabel(root, image=image)
imagelabel.place(x=50 , y=0)

# Titre pricipal
titre = CTkLabel(root, 
                 text="Systéme de gestion\nd'employées",
                 justify="center", 
                 font=s.FONTS["title"],
                 text_color=s.COLORS["primary"],
                 bg_color=s.COLORS["surface"]
                 )
titre.place(x=65, y=90)

# Zone de saisie 
type_zone_frame = CTkFrame(root, 
                           fg_color=s.COLORS["bg"],
                           width=250, height=300,
                           corner_radius=10)
type_zone_frame.place(x=60, y= 160)

titre_label = CTkLabel(type_zone_frame, 
                       text="Se connecter",
                       text_color=s.COLORS["primary"],
                       font=("Helvetica", 18, "bold"),
                       
                       ).place(x=32, y=12)

sub_new_label = CTkLabel(type_zone_frame, 
                       text="Saisissez les identifiants de votre compte",
                       text_color=s.COLORS["muted"],   
                       font=("Roboto", 10)                    
                       ).place(x=32, y=30)

username_plas_label = CTkLabel(type_zone_frame, 
                       text="Nom d'utilisateur",
                       text_color=s.COLORS["muted"],   
                       font=("Roboto", 10)                    
                       ).place(x=34, y=53)

user_name_entry = CTkEntry(type_zone_frame, 
                         placeholder_text="",
                         text_color="black",
                         fg_color="white",
                         border_width=2,
                         border_color=s.COLORS["bg"],
                         width=190,
                         height=30,
                         corner_radius=5
                         )
user_name_entry.place(x=32, y=75)

mdp_plas_label = CTkLabel(type_zone_frame, 
                       text="Mot de passe",
                       text_color=s.COLORS["muted"],   
                       font=("Roboto", 10)                    
                       ).place(x=34, y=105)

user_mdp_entry = CTkEntry(type_zone_frame, 
                         placeholder_text="",
                         text_color="black",
                         fg_color="white",
                         border_width=2,
                         border_color=s.COLORS["bg"],
                         width=190,
                         height=30,
                         corner_radius=5,
                         show="*"
                         )
user_mdp_entry.place(x=32, y=125)

login_btn = CTkButton(type_zone_frame, 
                      text="Se connecter",
                      font=("Roboto", 15), 
                      text_color="white", 
                      fg_color=s.COLORS["primary"],
                      hover_color=s.COLORS["primary_hover"],
                      corner_radius=5,
                      cursor="hand2",
                      command=login_infos_check,
                      width=190
                      )
login_btn.place(x=32, y=175)

creat_new_label = CTkLabel(type_zone_frame, 
                       text="Vous n'avez pas encore de compte ?",
                       text_color=s.COLORS["muted"],   
                       font=("Roboto", 10)                    
                       ).place(x=43, y=205)

creat_new_link = CTkButton(type_zone_frame, 
                       text="Créer un compte",
                       text_color=s.COLORS["primary"],   
                       font=("Roboto", 13, "bold"),
                       fg_color=s.COLORS["bg"],
                       cursor="hand2",  
                       hover=False, 
                       height=20,
                       width=50,
                       command=sign_up_page
                       ).place(x=63, y=225)

# Lance l'application sur le menu principal puis démarre la boucle graphique.
root.mainloop()