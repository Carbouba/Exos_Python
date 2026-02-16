# Importation des modules necessaire
from tkinter import *
from tkcalendar import *
import pymysql
from tkinter import ttk, messagebox

class FromMysql:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulaire Mysql")
        self.root.geometry("1920x1080+0+0")

        # Frame pricipale (Conteneur)
        main_frame = Frame(self.root, bg="grey")
        main_frame.place(x=500, y=200, width=700, height=500)

        # les champs de saisies
        title = Label(main_frame, text="Formulaire", font=("Helvetica", 25, "bold"), bg="grey", fg="white").place(x=50, y=30)

        # Prenom
        txt_prenom = Label(main_frame, text="Prenom", font=("Helvetica", 15), bg="grey", fg="black").place(x=50, y=100)
        self.ecr_prenom = Entry(main_frame, font=("Helvetica", 20), bg="lightgrey")
        self.ecr_prenom.place(x=50, y=130, width=250)

        # nom
        txt_nom = Label(main_frame, text="nom", font=("Helvetica", 15), bg="grey", fg="black").place(x=370, y=100)
        self.ecr_nom = Entry(main_frame, font=("Helvetica", 20), bg="lightgrey")
        self.ecr_nom.place(x=370, y=130, width=250)

        # Téléphone
        txt_tel = Label(main_frame, text="Téléphone", font=("Helvetica", 15), bg="grey", fg="black").place(x=370, y=180)
        self.ecr_tel = Entry(main_frame, font=("Helvetica", 20), bg="lightgrey")
        self.ecr_tel.place(x=370, y=210, width=250)

        # mail
        txt_mail = Label(main_frame, text="Adresse email", font=("Helvetica", 15), bg="grey", fg="black").place(x=50, y=180)
        self.ecr_mail = Entry(main_frame, font=("Helvetica", 20), bg="lightgrey")
        self.ecr_mail.place(x=50, y=210, width=250)

         # Nationalité
        txt_nat = Label(main_frame, text="Nationalité", font=("Helvetica", 15), bg="grey", fg="black").place(x=370, y=260)
        self.ecr_nat = Entry(main_frame, font=("Helvetica", 20), bg="lightgrey")
        self.ecr_nat.place(x=370, y=290, width=250)

        # Sexe
        txt_sexe = Label(main_frame, text="Sexe", font=("Helvetica", 15), bg="grey", fg="black").place(x=50, y=260)
        self.ecr_sexe = ttk.Combobox(main_frame, font=("Helvetica", 12), state="readonly")
        self.ecr_sexe["values"] = ("Homme", "Femme")
        self.ecr_sexe.current(0)
        self.ecr_sexe.place(x=50, y=290, width=250)

        # Date de naissance
        txt_date = Label(main_frame, text="Date de naissance", font=("Helvetica", 15), bg="grey", fg="black").place(x=50, y=340)
        self.ecr_date = DateEntry(main_frame, font=("Helvetica", 12), bg="lightgrey", date_pattern="dd/mm/yy", state="readonly")
        self.ecr_date.place(x=50, y=370)

        # Bouton de soumission
        self.submit_btn = Button(main_frame, text="Soumettre", font=("Helvetica", 12), bg="lightblue")
        self.submit_btn.place(x=50, y=440)
    
    def formulaire_bdd(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="formulaire")
            cur = con.cursor()
            cur.execute("select * frome details where email=%s", self.ecr_mail.get())
            row = cur.fetchone()

            if row != None:
                messagebox.showerror("Erreur", "Cet email existe deja, reessayer un autre", parent=self.root)
            else:
                pass


        except Exception as es:
            messagebox.showerror("Erreur", f"Erreur de connection : {str(es)}", parent=self.root)
        
# Création de la fenetre principale
root = Tk()
obj = FromMysql(root)




# Demarrage 
root.mainloop()