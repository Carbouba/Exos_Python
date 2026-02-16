# Depuis le module Ttkinter, import ttous les elements avec (*)
from tkinter import *
import webbrowser

def ouvrir_page_web():
    webbrowser.open_new("https://aistudio.google.com/prompts/1_pICrB9soFYiFi35GdVyCiOIX3RSDoXW")

# Premier fenetre
root = Tk()

# Personnaliser la fenetre
root.title("My first app")
root.geometry("750x500")
root.minsize(500, 500)
#root.iconbitmap("Logo_patrio.ico")
root.config(background='#5371ad')

# Ajouter une frame
frame = Frame(root, bg="#5371ad")

# Ajouter du texte
label_title = Label(frame, text="Bienvenue sur mon app", font=("Montsserat", 40), bg=("#5371ad"), foreground=("#FFFFFF"))
label_title.pack()

# Ajouter d'un second texte
label_subtitle = Label(frame, text="Ceci est ma premiere application avec interface en Python", font=("Helvetica", 20), bg=("#5371ad"), foreground=("#000000"))
label_subtitle.pack()

# Ajouter un bouton
button = Button(frame, text="Clique", font=("Montsserat", 20), bg=("#FFFFFF"), foreground=("#000000"), command=ouvrir_page_web)
button.pack(pady=25, padx=25)

# Ajouter la frame
frame.pack(expand=YES)

# Aficher la fenetre
root.mainloop()