import tkinter as tk

def decimal_hexa(decimal):
    hexa = hex(decimal).replace("0x", "")
    
    return hexa

def convetir():
    decimal = int(decima_entry.get())
    hexa = decimal_hexa(decimal)
    resulta.config(text=hexa.capitalize())

root = tk.Tk()
root.title("Convertisseur")
#root.geometry("500x400")

titre = tk.Label(root, text="Convertir Decimal vers Hexadecimal", font=("Arial", 15))
titre.pack()

main_fram = tk.Frame(root)
main_fram.pack()

decimal_label = tk.Label(main_fram, text="Nombre decimal :")
decimal_label.grid(row=0, column=0, padx=5, pady=5)

decima_entry = tk.Entry(main_fram)
decima_entry.grid(row=0, column=1, padx=5, pady=5)

convert_btn = tk.Button(root, text="Convertir", font=("Arial", 10), command=convetir)
convert_btn.pack(pady=10)

resulta = tk.Label(root, text="")
resulta.pack(pady=10)

root.mainloop()