ESTRUTURAS:

----------------------Label:----------------------
self.label1 = tk.Label(self.ventana, text = "texto 1")

----------------------Buton:----------------------
self.boton1 = tk.Button(self.ventana, text = "Ingresar texto", command = self.ingresar)

----------------------Entry:----------------------
self.dato1 = tk.StringVar()
self.entrada1 = tk.Entry(self.ventana,width = 10,textvariable = self.dato1)

llamada al metodo get


----------------------Radiobutton:----------------------
self.seleccion = tk.IntVar()
self.seleccion.set(2)

self.radio1 = tk.Radiobutton(self.ventana,text = "Varon",variable=self.seleccion, value=1)

llamada al metodo get

----------------------Checkbutton----------------------
self.seleccion1 = tk.IntVar()
self.check1 = tk.chekbutton(self.ventana,text= "Python",variable=self.seleccion1)

self.seleccion2= tk.IntVar()
self.check2 = tk.chekbutton(self.ventana,text = "C++",variable=self.seleccion2)

[chek con command]
self.seleccion1 = tk.IntVar()
self.check1 = tk.Checkbutton(self.ventana,text="Esta de acuerdo con los terminos y condiciones?", variable=self.seleccion1,command=self.cambiar_estado)

llamada al metodo get



----------------------control listbox----------------------
self.listbox1 = tk.Listbox(self.ventana)
self.listbox1.grid(column=0,row=0)
self.listbox1.insert(0,"Papas")
self.listbox1.insert(1,"Manzanas")
self.listbox1.insert(2,"Melon")
self.listbox1.insert(3,"Naranjas")

multiple seleccion:
self.listbox1 = tk.Listbox(self.ventana,selectmode=tk.MULTIPLE)
self.listbox1.grid(column=0,row=0)
self.listbox1.insert(0,"Papas")
self.listbox1.insert(1,"Manzanas")
self.listbox1.insert(2,"Melon")
self.listbox1.insert(3,"Naranjas")

---- ttk: label, button, entry, radiobutton, checkbutton, 
----------------------ttk: combobox----------------------
self.opcion = tk.StringVar()
paises = ("Chile","Argentina","Uruguay","Mexico","Colombia")
self.combobox1 = ttk.Combobox(self.ventana, width = 20,textvariable = self.opcion, values = paises, state = "readonly")
self.combobox1.grid(column=0,row = 0)
self.combobox1.current(0)

----------------------tkinter: control menu----------------------
import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        menubar1 = tk.Menu(self.ventana)
        self.ventana.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1)
        opciones1.add_command(label="Rojo",command=self.fijarrojo)
        opciones1.add_command(label="Verde", command=self.fijarverde)
        opciones1.add_command(label="Azul", command=self.fijarazul)
        menubar1.add_cascade(label="Colores",menu=opciones1)

        opciones2 = tk.Menu(menubar1)
        opciones2.add_command(label="640x480",command=self.ventanachica)
        opciones2.add_command(label="1024x800",command=self.ventanagrande)
        menubar1.add_cascade(label="Tamaños",menu=opciones2)
        self.ventana.mainloop()
    def fijarrojo(self):
        self.ventana.configure(background="red")
    def fijarverde(self):
        self.ventana.configure(background="green")
    def fijarazul(self):
        self.ventana.configure(background="blue")
    def ventanachica(self):
        self.ventana.geometry("640x480")
    def ventanagrande(self):
        self.ventana.geometry("1024x800")
aplicacion1 =Aplicacion()








----------------------ttk: Notebook y Frame----------------------
import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Prueba del control Notebook")
        self.cuaderno1 = ttk.Notebook(self.ventana)

        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1,text="Button")
        self.label1 = ttk.Label(self.pagina1,text="La clase button nospermite capturar el click y lanzar un evento")
        self.label1.grid(column=0,row=0)

        self.boton1 = ttk.Button(self.pagina1,text="Ejemplo de boton")
        self.boton1.grid(column=0,row=1)

        self.boton2 = ttk.Button(self.pagina1,text="Ejemplo de boton inactivo",state="disabled")
        self.boton2.grid(column=0,row=2)

        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2,text="Label")
        self.label2 = ttk.Label(self.pagina2,text="La clase Label permite mostrar un mensaje")
        self.label2.grid(column=0,row=0)

        self.label3 = ttk.Label(self.pagina2,text="Con los caracteres no se que poner xd")
        self.label3.grid(column=0,row=1)

        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3,text="Entry")
        self.label4 = ttk.Label(self.pagina3,text="En tkinter el control de entrada de datos por teclado se llama entry")
        self.label4.grid(column=0,row=0)

        self.entry = ttk.Entry(self.pagina3,width=30)
        self.entry.grid(column=0,row=1)

        self.cuaderno1.grid(column=0,row=0)
        self.ventana.mainloop()

aplicacion1 = Aplicacion()


----------------------ttk: Control LabelFrame----------------------

import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Prueba del control Notebook")
        self.cuaderno1 = ttk.Notebook(self.ventana)

        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1,text="Button")
        self.label1 = ttk.Label(self.pagina1,text="La clase button nospermite capturar el click y lanzar un evento")
        self.label1.grid(column=0,row=0)

        self.boton1 = ttk.Button(self.pagina1,text="Ejemplo de boton")
        self.boton1.grid(column=0,row=1)

        self.boton2 = ttk.Button(self.pagina1,text="Ejemplo de boton inactivo",state="disabled")
        self.boton2.grid(column=0,row=2)

        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2,text="Label")
        self.label2 = ttk.Label(self.pagina2,text="La clase Label permite mostrar un mensaje")
        self.label2.grid(column=0,row=0)

        self.label3 = ttk.Label(self.pagina2,text="Con los caracteres no se que poner xd")
        self.label3.grid(column=0,row=1)

        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3,text="Entry")
        self.label4 = ttk.Label(self.pagina3,text="En tkinter el control de entrada de datos por teclado se llama entry")
        self.label4.grid(column=0,row=0)

        self.entry = ttk.Entry(self.pagina3,width=30)
        self.entry.grid(column=0,row=1)

        self.cuaderno1.grid(column=0,row=0)
        self.ventana.mainloop()

aplicacion1 = Aplicacion()




----------------------ttk: Control LabelFrame----------------------
import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.labelframe1 = ttk.Labelframe(self.ventana,text="Login")
        self.labelframe1.grid(column=0,row=0,padx=5,pady =10)
        self.login()
        self.labelframe2 = ttk.Labelframe(self.ventana,text="Operaciones")
        self.labelframe2.grid(column=0,row=1,padx=5,pady=10)
        self.operaciones()
        self.ventana.mainloop()
    def login(self):
        self.label1 = ttk.Label(self.labelframe1,text="Nombre de Usuario: ")
        self.label1.grid(column=0,row=0,padx=4,pady=4)
        self.entry = ttk.Entry(self.labelframe1)
        self.entry.grid(column=1,row=0,padx=4,pady=4)
        self.label2 = ttk.Label(self.labelframe1,text="Ingrese clave: ")
        self.label2.grid(column=0,row=1,padx=4,pady=4)
        self.entry2 = ttk.Entry(self.labelframe1,show="*")
        self.entry2.grid(column=1,row=1,padx=4,pady=4)
        self.boton1 = ttk.Button(self.labelframe1,text="Ingresar")
        self.boton1.grid(column=1,row=2,padx=4,pady=4)
    def operaciones(self):
        self.boton2 = ttk.Button(self.labelframe2,text="Agregar usuario")
        self.boton2.grid(column=0,row=0,padx=4,pady=4)

        self.boton3 = ttk.Button(self.labelframe2,text="Modificar usuario")
        self.boton3.grid(column=1,row=0,padx=4,pady=4)

        self.boton4 = ttk.Button(self.labelframe2,text="Borrar Usuario")
        self.boton4.grid(column=2,row=0,padx=4,pady=4)
aplicacion1 = Aplicacion()


