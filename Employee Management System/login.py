# Importation du module CustomTkinter
from customtkinter import *
from CTkMessagebox import *

from PIL import Image

# Thème visuel global
COLORS = {
    "bg": "#F4F7FB",
    "surface": "#FFFFFF",
    "primary": "#2563EB",
    "primary_hover": "#1D4ED8",
    "success": "#059669",
    "success_hover": "#047857",
    "danger": "#DC2626",
    "danger_hover": "#B91C1C",
    "text": "#0F172A",
    "muted": "#475569",
    "border": "#D9E2EC",
    "btn_texte_color":"#E7E7E7"
}

FONTS = {
    "title": ("Helvetica", 24, "bold"),
    "subtitle": ("Helvetica", 14),
    "button": ("Helvetica", 16, "bold"),
    "body": ("Helvetica", 13),
}


# Création de la fenêtre principale
root = CTk()

# Frame principale
# main_frame = ctk.CTkFrame(root, fg_color=COLORS["bg"])
# main_frame.pack(expand=True, fill="both")


# Personnalisation de la fenêtre
root.title("Se connecter")
root.geometry("930x478")
root.resizable(0, 0)
root.configure(fg_color=COLORS["bg"])
image = CTkImage(Image.open("cover.jpg"), size=(930,478))
imagelabel = CTkLabel(root, image=image)
imagelabel.place(x=50 , y=0)

# Titre pricipal
titre = CTkLabel(root, 
                 text="Systéme de gestion d'employer", 
                 font=FONTS["title"],
                 text_color=COLORS["primary"],
                 fg_color=COLORS["bg"]
                 
                 )
titre.place(x=20, y=100)



# Démarrage
# Lance l'application sur le menu principal puis démarre la boucle graphique.
root.mainloop()
