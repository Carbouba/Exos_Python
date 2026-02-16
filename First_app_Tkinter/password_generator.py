from tkinter import *

# Création de la fenetre
window = Tk()
window.title("Générateur de mot de passe")
window.geometry("750x500")
window.minsize(500, 500)
#window.iconbitmap("Logo_patrio.ico")
window.config(background="#5371ad")

frame = Frame(window, bg="#5371ad")

# Crreation d'image
width = 300
height = 300
canvas = Canvas(window, width=width, height=height, bg="#5371ad")
canvas.create_image(width/2, height/2)

# Créer le titre
Label_title = Label(frame, text="Mot de passe", font=("Helvetica", 20), bg="#5371ad", foreground="#ffffff" )
Label_title.pack()

# Afficher la frame
frame.pack(expand=YES)

# Afficher la fenetre
window.mainloop()
