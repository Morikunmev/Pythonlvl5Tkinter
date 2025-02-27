import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.valor1 = 0
        self.valor2 = 0
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora")
        self.ventana.resizable(False, False)

        self.etiquetas()
        self.botones()
        self.mostrar_multiplicacion()
        self.mostrar_division()
        self.ventana.mainloop()

    def etiquetas(self):
        self.texto1 = tk.Label(self.ventana, text=self.valor1)
        self.texto1.grid(column=0, row=0)

        self.texto2 = tk.Label(self.ventana, text=self.valor2)
        self.texto2.grid(column=0, row=1)

    def botones(self):
        self.boton1 = tk.Button(self.ventana, text="Sumar", command=self.sumar)
        self.boton1.grid(column=1, row=0)

        self.boton2 = tk.Button(self.ventana, text="Restar", command=self.restar)
        self.boton2.grid(column=2, row=0)

        self.boton3 = tk.Button(self.ventana, text="Sumar", command=self.sumar1)
        self.boton3.grid(column=1, row=1)

        self.boton4 = tk.Button(self.ventana, text="Restar", command=self.restar1)
        self.boton4.grid(column=2, row=1)

    def mostrar_multiplicacion(self):
        self.valor3 = self.valor1 * self.valor2
        self.mult = tk.Label(self.ventana, text=self.valor3)
        self.mult.grid(column=0, row=2)

    def mostrar_division(self):
        try:
            self.valor4 = self.valor1 / self.valor2
            self.divid = tk.Label(self.ventana,text=self.valor4)
            self.divid.grid(column=0, row=3)
        except ZeroDivisionError:
            self.valor4 = "No se puede dividir por 0"
        

    def sumar(self):
        self.valor1 += 1
        self.texto1.config(text=self.valor1)
        self.mostrar_multiplicacion()  # Actualiza la multiplicación
        self.mostrar_division()

    def restar(self):
        self.valor1 -= 1
        self.texto1.config(text=self.valor1)
        self.mostrar_multiplicación()  # Actualiza la multiplicación
        self.mostrar_division()

    def sumar1(self):
        self.valor2 += 1
        self.texto2.config(text=self.valor2)
        self.mostrar_multiplicacion()  # Actualiza la multiplicación
        self.mostrar_division()

    def restar1(self):
        self.valor2 -= 1
        self.texto2.config(text=self.valor2)
        self.mostrar_multiplicacion()  # Actualiza la multiplicación
        self.mostrar_division()

aplicacion1 = Aplicacion()

