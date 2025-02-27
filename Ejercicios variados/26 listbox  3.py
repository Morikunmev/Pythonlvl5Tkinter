import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.listbox1 = tk.Listbox(self.ventana)
        self.listbox1.grid(column=0,row=0)
        self.listbox1.insert(0,"1+2")
        self.listbox1.insert(1,"3+2")
        self.listbox1.insert(2,"4+2")
        self.listbox1.insert(3,"4+1")
        self.listbox1.insert(4,"5+2")

        self.boton1 = tk.Button(self.ventana,text="Calcular",command=self.calcular)
        self.boton1.grid(column=0,row=1)

        self.texto1 = tk.Label(self.ventana,text="Resultado")
        self.texto1.grid(column=0,row=2)

        self.ventana.mainloop()

    def calcular(self):
        selected_items = self.listbox1.curselection()
        resultados = []
        for index in selected_items:
            operacion = self.listbox1.get(index)
            resultado = eval(operacion)  # Evalúa la expresión matemática.
            resultados.append(f"{operacion} = {resultado}")

        resultado_final = "\n".join(resultados)
        self.texto1.config(text=resultado_final)


aplicacion1 = Aplicacion()