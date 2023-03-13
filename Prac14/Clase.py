from tkinter import *
from tkinter import ttk
import tkinter as tk 
from tkinter import Entry
from tkinter import messagebox
class Cajero:
    def __init__(self,Sesion,Saldo,seccion1,seccion2):
        self.Sesion = Sesion
        self.Saldo=Saldo
        self.seccion1=seccion1
        self.seccion2=seccion2
        self.etiqueta_anterior = None
        self.C = None
        self.dp = None
        self.NM = None

    def SS(self):
        if self.Cuenta.get()=="121038827":
            
            self.Met = Label(self.seccion1, text="Seleccione accion a realizar", bg="green")
            self.Met.pack()
            self.metodos = ["Ingresar efectivo", "Retirar Efectivo","Consultar saldo", "Depositar a otra cuenta"]
            self.opcion_seleccionada = tk.StringVar()
            self.Metodo = ttk.Combobox(self.seccion1, textvariable=self.opcion_seleccionada, values=self.metodos)
            self.Metodo.pack()
            self.Continuar=Button(self.seccion1,text="continuar",bg="black",fg="white",command=self.acc)
            self.Continuar.pack()
        else:
            messagebox.showerror("Error","Ingrese una cuenta existente")
    def SS2(self):
        if self.Edad.get() == "":
            edad=0
        else:
            edad=int(self.Edad.get())
        if self.Nombre.get()=="" or self.Edad.get()=="" or self.NC.get=="":
            messagebox.showerror("Error","Uno o más datos no han sido ingresados")
        elif edad < 18:
            messagebox.showerror("Error","Debe ser mayor de edad para poder ingresar")
        else: 
            self.Met = Label(self.seccion1, text="Seleccione accion a realizar", bg="green")
            self.Met.pack()
            self.metodos = ["Ingresar efectivo", "Retirar Efectivo","Consultar saldo", "Depositar a otra cuenta"]
            self.opcion_seleccionada = tk.StringVar()
            self.Metodo = ttk.Combobox(self.seccion1, textvariable=self.opcion_seleccionada, values=self.metodos)
            self.Metodo.pack()
            self.Continuar=Button(self.seccion1,text="continuar",bg="black",fg="white",command=self.acc)
            self.Continuar.pack()
    def destruir_anterior(self):
        if self.etiqueta_anterior is not None:
            Num.destroy()
            self.dinero.destroy()
            BOT.destroy()
        if self.dp is not None:
            dep.destroy()
            self.ct.destroy()
        if self.C is not None:
            self.Cuenta.destroy()
            cuen.destroy()
            btn.destroy()
        if self.NM is not None:
            self.Nombre.destroy()
            self.NC.destroy()
            self.Edad.destroy()
            Nom.destroy()
            num.destroy()
            ed.destroy()
            Continuar.destroy()
    def TT(self):
        self.w=2
    def gg(self):
        global Total
        
        if self.Metodo.get() == "Ingresar efectivo":
            if self.dinero.get()=="":
                messagebox.showerror("Error","Ingrese una cantidad")
            else:
                dineros = int(self.dinero.get())
                Total = self.Saldo + dineros
                self.Saldo = Total
                messagebox.showinfo("Ingreso","Su saldo anterior era de: " + str(self.Saldo-dineros) + ", Su saldo actual es de " + str(Total))
        elif self.Metodo.get() == "Retirar Efectivo":
            if self.dinero.get()=="":
                messagebox.showerror("Error","Ingrese una cantidad")
            else:
                dineros = int(self.dinero.get())
                Total = self.Saldo - dineros
                self.Saldo = Total
                messagebox.showinfo("Retiro","Su saldo anterior era de: " + str(self.Saldo+dineros) + ", Su saldo actual es de " + str(Total))
        elif self.Metodo.get() == "Consultar saldo":
                Total = self.Saldo
                messagebox.showinfo("Saldo","Su saldo es de: " + str(Total))
        else:
            if self.dinero.get()=="":
                messagebox.showerror("Error","Ingrese una cantidad")
            else:
                messagebox.showinfo("Deposito","Su deposito se ha realizado con exito")
                
    def acc(self):
            global Num
            global BOT
            global dep
            global Ter
            self.destruir_anterior()
            if self.Metodo.get() == "Ingresar efectivo":
                Num = Label(self.seccion1, text="Ingrese la cantidad a depositar", bg="green")
                Num.pack()
                self.dinero=ttk.Entry(self.seccion1)
                self.dinero.pack()
                self.etiqueta_anterior = 1
                BOT = Button(self.seccion1, text="cotinuar", bg="black",fg="white",command=self.gg)
                BOT.pack()
            elif self.Metodo.get() == "Retirar Efectivo":
                Num = Label(self.seccion1, text="Ingrese la cantidad a retirar", bg="green")
                Num.pack()
                self.dinero=ttk.Entry(self.seccion1)
                self.dinero.pack()
                self.etiqueta_anterior = 1
                BOT = Button(self.seccion1, text="cotinuar", bg="black",fg="white",command=self.gg)
                BOT.pack()
            elif self.Metodo.get() == "Consultar saldo":
                Total = str(self.Saldo)
                Num = Label(self.seccion1, text="Su saldo es: " + Total, bg="green")
                Num.pack()
                self.dinero=ttk.Entry(self.seccion1,state="disabled")
                self.etiqueta_anterior = 1
                BOT = Button(self.seccion1, text="cotinuar", bg="black",fg="white",command=self.gg)
                BOT.pack()
            elif self.Metodo.get() == "Depositar a otra cuenta":
                Num = Label(self.seccion1, text="Ingrese la cantidad a depositar", bg="green")
                Num.pack()
                self.dinero=ttk.Entry(self.seccion1)
                self.dinero.pack()
                dep = Label(self.seccion1, text="Ingrese la cuenta a depositar", bg="green")
                dep.pack()
                self.ct = ttk.Entry(self.seccion1)
                self.ct.pack()
                BOT = Button(self.seccion1, text="cotinuar", bg="black",fg="white",command=self.gg)
                BOT.pack()
                self.etiqueta_anterior = 1
                self.dp = 1
                self.cct = self.ct

    
    def inicio(self):
            global cuen
            global btn
            global Nom
            global num
            global ed
            global Continuar
            self.destruir_anterior()
            if self.Sesion.get() == "Iniciar sesion":
                cuenta = Label(self.seccion2, text="Ingrese su Numero de cuenta",bg="purple")
                cuenta.pack()
                self.Cuenta = ttk.Entry(self.seccion2)
                self.Cuenta.pack()
                Continuar = Button(self.seccion2, text="Continuar",bg="black",fg="white",command=self.SS)
                Continuar.pack()
                cuen=cuenta
                self.C=self.Cuenta
                btn=Continuar
                self.C = 1
                
            elif self.Sesion.get() == "Registrarse":
                Nom= Label(self.seccion2, text="Ingrese su nombre", bg="purple")
                Nom.pack()
                self.Nombre = ttk.Entry(self.seccion2)
                self.Nombre.pack()
                self.NM = 1
                num=Label(self.seccion2,text="Ingrese su numero de cuenta",bg="purple")
                num.pack()
                self.NC = ttk.Entry(self.seccion2)
                self.NC.pack()
                ed=Label(self.seccion2,text="Ingrese su edad",bg="purple")
                ed.pack()
                self.Edad = ttk.Entry(self.seccion2)
                self.Edad.pack()
                Continuar = Button(self.seccion2, text="Continuar",bg="black",fg="white",command=self.SS2)
                Continuar.pack()    