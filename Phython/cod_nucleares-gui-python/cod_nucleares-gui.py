from tkinter import *
import random

#5c739c para el fg de texto
#36435a para el bg de botones
#7c9dd8 bg para boton activo
#1c2431 par el bg de la ventana y texto

root = Tk()
# ventana config
root.title("Generador de codigos nucleares")
root.geometry("600x500")
root.iconbitmap("gui python\icon.ico")
root.resizable(0, 0)
root.config(bg= "#1c2431")

# variables
option = StringVar()

# funciones
def clear():
    question = HIDDEN
    boton_no = HIDDEN
    boton_si = HIDDEN

# widgets
question = Label(root, 
    text="Quieres codigos nucleares?", 
    fg= "white", 
    bg= "#1c2431", 
    font= "Arial 20")
question.place(x= 150, y= 10)

boton_si = Button(root, 
    text="Si",
    command= clear, 
    fg= "white", 
    bg= "#36435a", 
    bd= 3,  
    activebackground= "#7c9dd8", 
    font= "Arial")
boton_si.place(x= 200, y= 400)

boton_no = Button(root, 
    text="No", 
    command= clear,
    fg= "white", 
    bg= "#36435a", 
    bd= 3, 
    activebackground= "#7c9dd8", 
    font= "Arial")
boton_no.place(x= 350, y= 400)

root.mainloop()