import tkinter as tk
import sys

class Registros:
    registros = [{"nombre":"richard","contraseña":"2121"},{"nombre":"juan","contreña":"1212"}]

class Aplicacion2:
    def __init__(self,NombreUsuario):
        self.ventana1 = tk.Toplevel()
        self.ventana1.title(f"Bienvenido: {NombreUsuario}")
        self.ventana1.geometry("400x400")

        self.texto1 = tk.Label(self.ventana1,text=f"Bienvenido {NombreUsuario}")
        self.texto1.grid(column=0,row =0)

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Interfaz de ususario")
        self.ventana.resizable(False,False)

        self.interfaz()
        self.botones()
        self.ventana.mainloop()

    def interfaz(self):
        self.nombre = tk.Label(self.ventana,text="Ingrese su nombre: ")
        self.nombre.grid(column=0,row=0)

        self.dato1 = tk.StringVar()
        self.entrada1 = tk.Entry(self.ventana,width=30,textvariable=self.dato1)
        self.entrada1.grid(column=1,row=0)

        self.contraseña =tk.Label(self.ventana,text="Ingrese su contraseña: ")
        self.contraseña.grid(column=0,row=1)

        self.dato2 = tk.StringVar()
        self.entrada2 = tk.Entry(self.ventana,width=30,textvariable=self.dato2,show="*")
        self.entrada2.grid(column=1,row=1)

    def botones(self):
        self.boton1 = tk.Button(self.ventana,text="Ingresar",width=40,command=self.ingresardef)
        self.boton1.grid(column=1,row=2)

    def ingresardef(self):
        for registro in Registros.registros:
            if registro["nombre"] == self.dato1.get() and registro["contraseña"] == self.dato2.get():
                aplicacion2 = Aplicacion2(self.dato1.get())


aplicacion1 = Aplicacion()