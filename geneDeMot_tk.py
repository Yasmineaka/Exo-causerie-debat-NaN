from tkinter import Tk,Label, Entry, Button, Scale, HORIZONTAL, Frame
from tkinter.ttk import Combobox
from funcs import gen_mdp_into

def cmd():
    gen_mdp_into(entre)

def positioning(m):
    print(m)



root = Tk()
root.geometry("1000x600")
root.config(bg="#061745")
root.title('Genérateur de mot de passe')
difficulty_box = Combobox(root, values=["Facile", "Difficile"])
frame = Frame(root, width=800, height=400,border="2" , bg="#0f3550")
nom= Label(root, text="Bienvenue sur notre generateur de mot de passe", font=("Inter", 30), bg="#061745", foreground="white")

label = Label(frame, text="Generateur de mot de passe", bg="#0F3550", foreground="white", font=("Inter", 25))
entre = Entry(frame, width=50)
bouton = Button(frame, text="Génerer", command=cmd)
mdp_lenght = Scale(frame, from_=20, to=50, orient=HORIZONTAL)




label.place(x=250, y=0)
entre.place(x=100, y=100)
# difficulty_box.pack()
# mdp_lenght.pack()
frame.place(x=100, y=100)
nom.pack()
bouton.place(x=600, y= 100)
root.mainloop()

