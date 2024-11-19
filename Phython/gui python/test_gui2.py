from tkinter import *
#5c739c para el fg de texto
#36435a para el bg de botones
#7c9dd8 bg para boton activo
#1c2431 par el bg de la ventana y texto
#0d1120 bordes #445aa8


root = Tk()
# ventana config
root.title("Generador de codigos nucleares")
root.geometry("600x500")
root.iconbitmap("gui python\icon.ico")
root.resizable(0, 0)
root.config(bg= "#1c2431")

# variables
nombre = StringVar()
apellido = StringVar()

# funciones
def saludar():
    delete = Label(root, text= "---------------------------------------", fg= "#1c2431", bg= "#1c2431", bd= 3, font= "Sans 12")
    delete.place(x= 400, y= 50)
    saludo = Label(root, text= f"Hola {nombre.get()} {apellido.get()}", fg= "white", bg= "#1c2431", bd= 3, font= "Sans 12")
    saludo.place(x= 400, y= 50)
    # print(f"Hola {nombre.get()} {apellido.get()}")

# widgets
etiqueta1 = Label(root, text="Nombre: ", fg= "white", bg= "#1c2431", bd= 3, font= "Sans 12")
etiqueta1.place(x= 50, y= 20)
entry1 = Entry(root, textvariable= nombre, fg= "white", bg= "#1c2431", bd= 3, font= "Sans 12")
entry1.place(x= 150, y= 20)

etiqueta2 = Label(root, text="Apellido: ", fg= "white", bg= "#1c2431", bd= 3, font= "Sans 12")
etiqueta2.place(x= 50, y= 60)
entry2 = Entry(root, textvariable= apellido, fg= "white", bg= "#1c2431", bd= 3, font= "Sans 12", )
entry2.place(x= 150, y= 60)

boton = Button(root, text= "Saludar", command= saludar, fg= "white", bg= "#1c2431", activebackground= "#7c9dd8", bd= 3, font= "Sans 12")
boton.place(x= 75, y= 100)
root.mainloop()