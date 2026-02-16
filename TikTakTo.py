import tkinter

def check_win(click_row, click_col):
    # Detecter lz victoir verticale
    coutn = 0
    for i in range(3):
        current_buton = boutons[i][click_col]
        if current_buton["text"] == "X":
            coutn += 1
    if coutn == 3:
        print("Gagné verticalement")

    # Detecter lz victoir horizontal
    coutn = 0
    for i in range(3):
        current_buton = boutons[i][click_row]
        if current_buton["text"] == "X":
            coutn += 1
    if coutn == 3:
        print("Gagné horizontalement")


    # Detecter lz victoir horizontal
    coutn = 0
    for i in range(3):
        current_buton = boutons[i][i]
        if current_buton["text"] == "X":
            coutn += 1
    if coutn == 3:
        print("Gagné diagonalement")



def place_symbole(row, column):
    print(f"{row} {column}")
    
    clickerd_button = boutons[row][column]
    clickerd_button.config(text="X")

    check_win(row, column)

def draw_grid():
    for row in range(3):
        button_in_cals = []
        for column in range(3):
            button = tkinter.Button(
                windoww,font=("Arial", 25),
                width=5, height=3,
                command=lambda r = row, c = column :place_symbole(r, c)
                )
            button.grid(row=row, column=column)
            button_in_cals.append(button)
        boutons.append(button_in_cals)

    

# Stockage des positions boutons
boutons = []

# Créartionde la fenetre principale
windoww = tkinter.Tk()

# Personnalisation de la fenetre
windoww.title("TicTacToe Game")
windoww.geometry("500x500")

# Appele de la fonction boutton
draw_grid()

# Affichage de la fenetre
windoww.mainloop()