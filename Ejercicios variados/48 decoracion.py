import tkinter as tk
from tkinter import ttk

class MiApp:
    def __init__(self, master):
        self.master = master
        master.title("Ejemplo de Fondo")

        # Configurar la imagen de fondo
        imagen_fondo = tk.PhotoImage(file="ruta_de_tu_imagen.png")  # Cambia "ruta_de_tu_imagen.png" por la ruta de tu propia imagen
        fondo = ttk.Label(master, image=imagen_fondo)
        fondo.place(x=0, y=0, relwidth=1, relheighg=1)

        # Crear contenido sobre la imagen de fondo
        self.etiqueta = ttk.Label(master, text="¡Hola, Tkinter!", font=("Arial", 12), foreground="white")
        self.etiqueta.place(relx=0.5, rely=0.5, anchor="center")

if __name__ == "__main__":
    root = tk.Tk()
    app = MiApp(root)
    root.mainloop()
