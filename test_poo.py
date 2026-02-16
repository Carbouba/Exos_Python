class Article():
    def __init__(self, nom, quantite, prix, categorie):
        self.nom = nom
        self.quantite = quantite 
        self.prix = prix
        self.categorie = categorie

    """ def ajout_article(self):
        
        self.nom = input("Entrez le nom : ")
        self.quantite = input("Entrez la quantité : ")
        self.prix = int(input("Entrez le prix : "))
        self.categorie = input("Entrez la categorie : ")
        print(f"L'article {self.nom} a été ajouté !")
 """

    def afficher_article(self):
        print(f"Nom :  {self.nom}")
        print(f"Quantité :  {self.quantite}")
        print(f"Prix :  {self.prix}")
        print(f"Categorie :  {self.categorie}")
    

        #print(f"\nNom : {self.nom}\nQuantité : {self.quantite}\nPrix : {self.prix}\nCategorie : {self.categorie}")




a1 = Article("Pomme", 23, 100, "Fruit")
#a1.ajout_article()
a1.afficher_article()


""" 
a1 = Article()
print(f"\nNom : {a1.nom}\nQuantité : {a1.quantite}\nPrix : {a1.prix}\nCategorie : {a1.categorie}") """




""" a2 = Article(nom, quantite, prix, cat)

print(f"\nNom : {a2.nom}\nQuantité : {a2.quantite}\nPrix : {a2.prix}\nCategorie : {a2.categorie}") """