import tkinter as tk
from tkinter import ttk
from mod1 import ComponentePrincipal
from tkinter import messagebox as mb

class Principal:
    def __init__(self):
        # Creacion de la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Empresa New Food - Inicio de Sesion")
        self.ventana.resizable(False,False)
        # Añadir la instancia llamada "labelframe" de la clase que esta dentro
        # del paquete "componente principal" = labelframe
        self.labelframe1 = ComponentePrincipal.LabelFrame(self.ventana)
        #Uso de metodos del atributo de clase labelframe
        self.labelframe1.cuerpo_principal()
        #Añadir instancia "Menu" de la clase menu en el paquete "ComponentePrincipal"
        self.menu1 = ComponentePrincipal.Menu(self.ventana)
        #añadir la instancia labelframe1 de "registrarse" de la clase labelframe_registrar
        self.labelframe2 = ComponentePrincipal.labelframe_registrarse(self.ventana)
        self.labelframe2.cuerpo_principal()

        self.ventana.mainloop()
aplicacion1 = Principal()