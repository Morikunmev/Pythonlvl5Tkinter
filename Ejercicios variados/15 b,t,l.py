import tkinter as tk
import sys
class Temporizador:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("TEMPORIZADOR")
        self.contador = 0

        self.etiqueta = tk.Label(self.ventana, text=str(self.contador))
        self.etiqueta.pack()

        self.iniciar_temporizador()
        self.ventana.mainloop()

    def iniciar_temporizador(self):
        if self.contador < 10:
            self.contador += 1
            self.etiqueta.config(text=str(self.contador))
            self.ventana.after(1000, self.iniciar_temporizador)  # Llamada recursiva después de 1000 ms (1 segundo)
        else:
            sys.exit(0)

temporizador1 = Temporizador()
