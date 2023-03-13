from tkinter import *
from tkinter import ttk
import tkinter as tk 
from Clase import *

ventana = Tk()
ventana.title("Cajero")
seccion2=Frame(ventana,bg="purple")
seccion2.pack(expand=True,fill="both")
seccion1=Frame(ventana,bg="green")
seccion1.pack(expand=True,fill='both')
Ses = Label(seccion2, text="Iniciar sesion o registrarse", bg="purple")
Ses.pack()
sesion = ["Iniciar sesion", "Registrarse"]
opcion_seleccionada1 = tk.StringVar()
Sesion = ttk.Combobox(seccion2, textvariable=opcion_seleccionada1, values=sesion)
Sesion.pack()

Saldo = 15000
In = Cajero(Sesion,Saldo,seccion1,seccion2)
Iniciar=Button(seccion2,text="continuar",bg="black",fg="white",command=In.inicio)
Iniciar.pack()
        

ventana.mainloop()