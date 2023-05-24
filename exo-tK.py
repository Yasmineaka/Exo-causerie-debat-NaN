from tkinter import Tk,Label, Entry, Button, Scale, HORIZONTAL, Frame
from tkinter.ttk import Combobox
from funcs import gen_mdp_into

def cmd():
    gen_mdp_into(entre)



root = Tk()
root.geometry("500x500")
root.title('Genérateur de mot de passe')
difficulty_box = Combobox(root, values=["Facile", "Difficile"])
frame = Frame(root, background="RED")


label = Label(root, text="Bienvenu sur notre générateur")
entre = Entry(root, width=50)
bouton = Button(root, text="Génerer", command=cmd)
mdp_lenght = Scale(frame, from_=20, to=50, orient=HORIZONTAL)




label.pack()
entre.pack()
difficulty_box.pack()
mdp_lenght.pack()
frame.pack()
bouton.pack()
root.mainloop()

