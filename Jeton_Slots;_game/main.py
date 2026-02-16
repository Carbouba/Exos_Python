# Importer le module random
import random
from tkinter import * 

# Fonction pour affichier si identifiants correctes
def affiche_messa():
    print(f"\nBienvenue {email}\n")


# Affichage du message 
print("Bienvenue sur la machine à sous GraveFruitiiii!")

# Création de la fenetre
window = Tk()
window.title("Machine à sous")
window.geometry("750x500")
window.config(background="#3A8096")

# Ajout de la frame
frame = Frame(window, background="#3A8096")

# Ajout d'un prremier texte
text1 = Label(frame, text="Bienvenue !", font=("Helvetica", 40), bg="#3A8096", foreground="#ffffff")
text1.pack()

# MAessage saisie de nom
text2 = Label(frame, text="Entrez votre email", font=("Helvetica", 10), bg="#3A8096", foreground="#000000")
text2.pack(padx=0)
email = Entry(frame)
email.pack(padx=0)

text3 = Label(frame, text="Entrez votre mot de passe", font=("Helvetica", 10), bg="#3A8096", foreground="#000000")
text3.pack(padx=0)
nom = Entry(frame)
nom.pack(padx=0)

# Ajout d'un bouton
boutton1 = Button(frame, text="Connexion", font=("Helvetica", 10), bg="#ffffff", foreground="#3A8096")
boutton1.pack(pady=10)



# # Liste stockant le nom de chaque fruit
# fruit = ["ananas", "cerise", "orange", "pasteque", "pomme_dore"]

# # Afficher un fruit aleatoirement
# fruit_hasard = random.choices(fruit, k=3)

# print(f"{fruit_hasard}\n")

# Affichage de la frame
frame.pack(expand=YES)

#  Affichage de la fenetre
window.mainloop()