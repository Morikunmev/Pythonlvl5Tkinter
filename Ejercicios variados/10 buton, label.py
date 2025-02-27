import tkinter as tk
import sys

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ejercicio")
        self.ventana.resizable(False,False)

        self.resultados()
        self.textos()
        self.botones()
        self.entradas()
        self.botones1()
        self.ventana.mainloop()
    def comandos(self):
    def botones1(self):
        self.boton11 = tk.Button(self.ventana,text="AGREGAR",command =self.comandos)
        self.boton11.grid(column=2,row=0)

        self.boton2 = tk.Button(self.ventana,text="AGREGAR")
        self.boton2.grid(column=2,row =1)

        self.boton3 = tk.Button(self.ventana,text="AGREGAR")
        self.boton3.grid(column=2,row=2)

        self.boton4 = tk.Button(self.ventana,text="AGREGAR")
        self.boton4.grid(column=2,row=3)

        self.boton5 = tk.Button(self.ventana,text = "AGREGAR")
        self.boton5.grid(column=2,row =4)

        self.boton6 = tk.Button(self.ventana,text="AGREGAR")
        self.boton6.grid(column=2,row=5)

        self.boton7 = tk.Button(self.ventana,text="AGREGAR")
        self.boton7.grid(column=2,row=6)
    def entradas(self):
        self.dato1 = tk.StringVar()
        self.entrada1 = tk.Entry(self.ventana,width=30,textvariable=self.dato1)
        self.entrada1.grid(column=1,row=0)

        self.dato2 = tk.StringVar()
        self.entrada2 = tk.Entry(self.ventana,width=30,textvariable=self.dato2)
        self.entrada2.grid(column=1,row=1)

        self.dato3 = tk.StringVar()
        self.entrada3 = tk.Entry(self.ventana,width=30,textvariable=self.dato3)
        self.entrada3.grid(column=1,row=2)

        self.dato4 = tk.StringVar()
        self.entrada4 = tk.Entry(self.ventana,textvariable=self.dato4,width=30)
        self.entrada4.grid(column=1,row=3)

        self.dato5 = tk.StringVar()
        self.entrada5 = tk.Entry(self.ventana,textvariable=self.dato5,width=30)
        self.entrada5.grid(column=1,row=4)

        self.dato6 = tk.StringVar()
        self.entrada6 = tk.Entry(self.ventana,textvariable=self.dato6,width=30)
        self.entrada6.grid(column=1,row=5)

        self.dato7 = tk.StringVar()
        self.entrada7 = tk.Entry(self.ventana,textvariable=self.dato7,width=30)
        self.entrada7.grid(column=1,row=6)
    def finalizar(self):
        sys.exit(0)
    def botones(self):
        self.boton1 = tk.Button(self.ventana,text="Finalizar: ",width=25,command=self.finalizar)
        self.boton1.grid(column=1,row=7)
    def textos(self):
        self.texto1 = tk.Label(self.ventana,text="Nombre: ")
        self.texto1.grid(column=0,row=0)

        self.texto2 = tk.Label(self.ventana,text="Run: ")
        self.texto2.grid(column=0,row=1)

        self.texto3 = tk.Label(self.ventana,text="Empresa: ")
        self.texto3.grid(column=0,row=2)

        self.texto4 = tk.Label(self.ventana,text="Comuna: ")
        self.texto4.grid(column=0,row=3)

        self.texto5 = tk.Label(self.ventana,text="Numero de contacto: ")
        self.texto5.grid(column=0,row=4)

        self.texto5 = tk.Label(self.ventana,text="Email: ")
        self.texto5.grid(column=0,row=5)

        self.texto6 = tk.Label(self.ventana,text="Metodo de pago: ")
        self.texto6.grid(column=0,row=6)

aplicacion1 = Aplicacion()