# # Import du module CTK
# import customtkinter as ctk

# # Création et personnalisation de la fentre 
# root = ctk.CTk()
# root.title("CTK-Hub") 
# root.geometry("300x500")

# def switch_option(switch_to):

#     if switch_to == "login":
#         login_page_option.configure(text_color="black", border_color="black")

#     else:
#         signup_page_option.configure(text_color="white", border_color="white")

# # Bouton login
# login_page_option = ctk.CTkButton(master=root, text="Login", 
#                                   font=("Arial", "bold", 20), text_color="white", 
#                                   width=120, height=20,
#                                   corner_radius=10, 
#                                   border_width=2, border_color="white", hover=False, command=lambda: switch_option("login"))

# # Bouton signup
# signup_page_option = ctk.CTkButton(master=root, text="Signup", 
#                                   font=("bold", 20), text_color="black", fg_color="white",
#                                   width=120, height=20,
#                                   corner_radius=10, 
#                                   border_width=2, border_color="white", hover=False, command=lambda: switch_option("signup"))

# # Placement des widgets
# login_page_option.place(x=20, y=40)
# signup_page_option.place(x=155, y=40)

# # page frame
# page_frame = ctk.CTkFrame(root, width=250, height=370, corner_radius=10)
# page_frame.place(x=25, y=110)

# # Demarrage
# root.mainloop()



# import tkinter as tk

# def switch_indice(indice):

#     home_pg_indice.config(bg=menu_bar_bg)
#     service_pg_indice.config(bg=menu_bar_bg)
#     cta_pg_indice.config(bg=menu_bar_bg)
#     updt_pg_indice.config(bg=menu_bar_bg)

#     indice.config(bg="white")
    



# # # Création et personnalisation de la fentre 
# root = tk.Tk()
# root.title("TK-Hub") 
# root.geometry("400x600")

# menu_bar_bg = "#383838"
# menu_bar_frame = tk.Frame(root, bg=menu_bar_bg)
# menu_bar_frame.pack(side=tk.LEFT, fill="y", padx=3, pady=4)
# menu_bar_frame.pack_propagate(flag=False)
# menu_bar_frame.configure(width=60)


# #toggle_icon = tk.PhotoImage(file="icons/user-svgrepo-")

# toggle_btn = tk.Button(menu_bar_frame, text="SDB", font=("Arial", 10), 
#                        bg=menu_bar_bg, fg="white", 
#                        width=2, bd=0, activebackground=menu_bar_bg)
# toggle_btn.place(x=9, y=10)

# #
# home_pg = tk.Button(menu_bar_frame, text="H_pg", font=("Arial", 10), 
#                        bg=menu_bar_bg, fg="white", 
#                        width=2, bd=0, activebackground=menu_bar_bg, command=lambda:switch_indice(home_pg_indice))
# home_pg.place(x=9, y=138)
# home_pg_indice = tk.Label(menu_bar_frame, bg=menu_bar_bg)
# home_pg_indice.place(x=2, y=134, width=2, height=35)

# #
# service_pg = tk.Button(menu_bar_frame, text="S_pg", font=("Arial", 10), 
#                        bg=menu_bar_bg, fg="white", 
#                        width=2, bd=0, activebackground=menu_bar_bg, command=lambda:switch_indice(service_pg_indice))
# service_pg.place(x=9, y=198)
# service_pg_indice = tk.Label(menu_bar_frame, bg=menu_bar_bg)
# service_pg_indice.place(x=2, y=194, width=2, height=35)

# #
# updt_pg = tk.Button(menu_bar_frame, text="U_pg", font=("Arial", 10), 
#                        bg=menu_bar_bg, fg="white", 
#                        width=2, bd=0, activebackground=menu_bar_bg, command=lambda:switch_indice(updt_pg_indice))
# updt_pg.place(x=9, y=258)
# updt_pg_indice = tk.Label(menu_bar_frame, bg=menu_bar_bg)
# updt_pg_indice.place(x=2, y=254, width=2, height=35)

# #
# cta_pg = tk.Button(menu_bar_frame, text="CTA", font=("Arial", 10), 
#                        bg=menu_bar_bg, fg="white", 
#                        width=2, bd=0, activebackground=menu_bar_bg, command=lambda:switch_indice(cta_pg_indice))
# cta_pg.place(x=9, y=318)
# cta_pg_indice = tk.Label(menu_bar_frame, bg=menu_bar_bg)
# cta_pg_indice.place(x=2, y=314, width=2, height=35)

# root.mainloop()



import tkinter as tk


def switch_incdice(btn, indice):
    
    acceuil_indice.config(bg=frames_bg)
    stock_indice.config(bg=frames_bg)
    btn_acceuil.config(bg=frames_bg, fg="white")
    btn_stock.config(bg=frames_bg, fg="white")

    indice.config(bg="white")
    btn.config(bg="white", fg="black")

# # Création et personnalisation de la fentre 
root = tk.Tk()
root.title("Gestion Stock") 
root.geometry("1920x1080")

frames_bg = "#383838"

main_frame = tk.Frame(root, bg=frames_bg)
main_frame.pack(expand=True, padx=20, pady=20)


top_frame = tk.Frame(root, bg=frames_bg)
top_frame.place(x=10, y=10)

login_btn = tk.Button(top_frame, )



titre = tk.Label(top_frame, text="GESTION STOCK V0.1", font=("Montserrat", 30, "bold"), background=frames_bg, fg="white")
titre.pack(padx=5, pady=5)

center_frame = tk.Frame(root, bg=frames_bg, width=1600, height=750)
center_frame.place(x=200, y=150)

left_fram = tk.Frame(root, bg=frames_bg, width=150, height=750)
left_fram.place(x=10, y=150)

btn_acceuil = tk.Button(left_fram, text="Acceuil", font=("Montserrat", 15, "bold"), 
                        background=frames_bg, fg="white", command=lambda: switch_incdice(btn_acceuil, acceuil_indice))
btn_acceuil.place(x=30, y=90, width=100)
acceuil_indice = tk.Label(left_fram, bg=frames_bg)
acceuil_indice.place(x=10, y=100,)


btn_stock = tk.Button(left_fram, text="Stock", font=("Montserrat", 15, "bold"), 
                        background=frames_bg, fg="white", command=lambda: switch_incdice(btn_stock, stock_indice))
btn_stock.place(x=30, y=190, width=100)
stock_indice = tk.Label(left_fram, bg=frames_bg)
stock_indice.place(x=10, y=200,)





root.mainloop()