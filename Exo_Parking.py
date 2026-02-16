""" # Afficher un message de bienvenue
def afficher_bonjour():
    print("Bienvenue au niveau -1,que souhaitez vous faire ?")


afficher_bonjour()



# Récupéré l'emplacement N°3 du parking
print(parking[2])

# Verification de l'emplacement
emplacements = parking[2]
if emplacements == "D":
    print("\nDisponible")
else:
    print("\nNon disponible")

print(f"{parking}\n")

parking[0] = "V"
parking[1] = "H"




print(f"{parking}\n")


# Parcourir chaque emplacement pour afficher sa disponiblité

for i, emplacement in enumerate(parking):
    if emplacement == "D":
        print(f"Emplacement {i} : disponible")
    elif emplacement == "H":
        print(f"Emplacement {i} à Personnalité mobilité")
    else:
        print(f"Emplacement {i} : indisponible")

    resultat = ("Occupé", "Libre")[emplacement == "D"]
    print(resultat)
 """


def afficher_parking():
    for num_eta, etage in enumerate(parking, start=1):
        print(f"Etage {num_eta}")
        for num_pla, place in enumerate(etage, start=1):
            print(f"Emplacement {num_pla}. {place}")

# Liste de parking
emplacements = 27
etage = 3

parking = [['D'] * emplacements] * etage

parking[1][1] = 'V'

afficher_parking()

choix_etage = int(input("\nChoisissez un etage : ")) - 1
if len(parking) > choix_etage and choix_etage >= 0: 

    print("\n1. Garer une voiture\n2. Récupérer une voiture")
    choix = int(input("Votre choix : "))


    if choix == 1:
        choix_empl = int(input(f"\nVous avez choisit de garer une voiture a l'etage {choix_etage + 1}. à quel emplacement souhaitez vous la garé ? : ")) - 1
        if len(parking[choix_etage]) > choix_empl and choix_empl >= 0:
            if parking[choix_etage][choix_empl] == 'D':
                print(f"\nVous avez choisit l'emplacement N°{choix_empl + 1}, vous pouvez garé")
                parking[choix_etage][choix_empl] = 'V'
                afficher_parking()
            else:
                print(f"\nL'emplacement {choix_empl+ 1} est indisponible")
        else:
            print("\nVous devez entrez un chiffre correct et entre 1 et 27")


    elif choix == 2:
        choix_empl = int(input("\nVous avez choisit de récupérer une voiture. à quel emplacement se trouve la voiture ? : ")) - 1
        if len(parking[choix_etage]) > choix_empl and choix_empl >= 0:
            if parking[choix_etage][choix_empl] == 'V':
                print(f"\nVous avez choisit l'emplacement N°{choix_empl + 1}, vous pouvez récupérer votre voiture")
                parking[choix_etage][choix_empl] = 'D'
                afficher_parking()
            else:
                print(f"Il n'y a aucune voiture a cet emplacement")
    else:
        print("Veuillez choisir en 1 et 2")




""" # Parcourir chaque emplacement pour afficher sa disponiblité

for i, emplacement in enumerate(parking):
    if emplacement == "D":
        print(f"la place  {i} est disponible")
        break
    elif emplacement == "H":
        print(f"Emplacement {i} à Personnalité mobilité")
    else:
        print(f"Emplacement {i} : indisponible")

    resultat = ("Occupé", "Libre")[emplacement == "D"]
    print(resultat)
  """