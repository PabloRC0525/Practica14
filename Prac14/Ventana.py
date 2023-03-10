from tkinter import *
from tkinter import ttk
import tkinter as tk 
from tkinter import Entry
from Clase import *

ventana = Tk()
ventana.title("Pedidos")
ventana.geometry("600x400")
seccion1=Frame(ventana,bg="green")
seccion1.pack(expand=True,fill='both')
Met = Label(seccion1, text="Seleccione accion a realizar", bg="green")
Met.pack()
metodos = ["Ingresar efectivo", "Retirar Efectivo","Consultar saldo", "Depositar a otra cuenta"]
opcion_seleccionada = tk.StringVar()
Metodo = ttk.Combobox(seccion1, textvariable=opcion_seleccionada, values=metodos)
Metodo.pack()
Num = Label(seccion1, bg="green")
dinero=ttk.Entry(seccion1)
def acc():
    if Metodo.get() == "Ingresar efectivo":
        Num.config(text="Ingrese la cantidad a depositar")
        dinero.config(textvariable="")
    elif Metodo.get() == "Retirar Efectivo":
        Num.config(text="Ingrese la cantidad a retirar")
        dinero.config(textvariable="")
    elif Metodo.get() == "Consultar saldo":
        Num.config(text="Su saldo es: ")
        dinero.config(textvariable="")
    elif Metodo.get() == "Depositar a otra cuenta":
        Num.config(text="Ingrese el número de cuenta")
        dinero.config(textvariable="")
    Num.pack()
    dinero.pack()
Continuar=Button(seccion1,text="continuar",bg="black",fg="white",command=acc)
Continuar.pack()
ventana.mainloop()