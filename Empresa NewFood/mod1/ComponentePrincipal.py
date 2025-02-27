import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mysql.connector
import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from datetime import datetime
import math

###LABEL FRAME, MENU###
class LabelFrame:
    def __init__(self,ventana):
        self.ventana = ventana

        self.estilolabelframe = ttk.Style()
        # Configurar el color de fondo para el Labelframe
        self.estilolabelframe.configure("Acceder.TLabelframe", background="white")
        self.estilolabelframe.configure("Acceder.TLabelframe.Label",font=("TkDefaultFont", 12, "bold"))

        self.labelframe1 = ttk.Labelframe(ventana,text="ACCEDER",style="Acceder.TLabelframe")
        #Relleno horizontal y vertical
        self.labelframe1.grid(column=0,row=0,padx=10,pady=10)

    def cuerpo_principal(self):

        self.texto1 = ttk.Label(self.labelframe1,text="Ingrese Usuario: ",foreground="black",background="#87CEEB",font=("Arial",9,"bold"))
        self.texto1.grid(column=0,row=0,padx=5,pady =5,sticky="e")

        self.dato1 = tk.StringVar()
        self.entrada1 = ttk.Entry(self.labelframe1,textvariable=self.dato1)
        self.entrada1.grid(column=1,row=0,padx=5,pady=5)

        self.texto2 = ttk.Label(self.labelframe1,text = "Ingrese Contraseña: ",foreground="black",background="#87CEEB",font=("Arial",9,"bold"))
        self.texto2.grid(column=0,row=1,padx=5,pady=5)

        self.dato2 = tk.StringVar()
        self.entrada2 = ttk.Entry(self.labelframe1,textvariable=self.dato2,show="*")
        self.entrada2.grid(column=1,row=1,padx=5,pady=5)
        #Boton ingresar
        self.boton1 = ttk.Button(self.labelframe1,text="Ingresar",command=self.apretar)

        self.boton1.grid(column=1,row= 3,padx=0,pady=0,sticky="we")

        #Configuracion de estilo para la entrada
        entrada_estilo = ttk.Style()
        entrada_estilo.configure("TEntry", foreground="black",font=("Arial", 10,"bold"),background="#FFA500")

        #Configuracion de estilo para el boton
        estilo = ttk.Style()
        estilo.configure("TButton", foreground="black", background="deep sky blue", font=("Arial", 10, "bold"))

    def apretar(self):
        if self.dato1.get() == "" and self.dato2.get() == "":
            mb.showerror("Error", "No se puede ingresar con los campos vacíos")
        elif self.dato1.get() == "" or self.dato2.get() == "":
            mb.showerror("Error", "Uno de los campos tiene que estar completo")
        else:
            usuario_correcto = False
            usuario_bd = None  # Variable para almacenar el usuario de la base de datos

            for registro in Usuario.registros:
                if registro["NombreUsuario"] == self.dato1.get() and registro["Contraseña"] == self.dato2.get():
                    usuario_correcto = True
                    break
            #Si el usuario no es encontrado en el diccionario, lo buscamos en la base de datos
            if not usuario_correcto:
                try:
                    conexion = mysql.connector.connect(user="root", password="xlgricky20131415", host="localhost",
                                                       database="gestion_newfood", port="3306")

                    #Se crea el cursos para ejecutar las consultas en la base de datos
                    #El parametro dictionary  = True Se utiliza para indicar que se desea que los resultados de las consultas
                    #se devuelvan como diccionarios en lugar de tuplas

                    cursor = conexion.cursor(dictionary=True)

                    sql = "SELECT * FROM Usuario WHERE NombreUsuario = %s"
                    cursor.execute(sql, (self.dato1.get(),))
                    usuario_bd = cursor.fetchone()
                    #Se utiliza el metodo fetchone para obtener la primera fila de resultados como un diccionario

                    if usuario_bd is not None and usuario_bd["Contraseña"] == self.dato2.get():
                        ventana1 = Ventana1(self.dato1.get())
                        self.ventana.destroy()
                    else:
                        mb.showerror("Error", "Credenciales inválidas")

                except mysql.connector.Error as e:
                    mb.showerror("Error", f"No se puede conectar a la base de datos: {e}")

                finally:
                    if cursor:
                        cursor.close()
                    if conexion:
                        conexion.close()

            # Resto del código para manejar las otras condiciones utilizando usuario_bd
            if usuario_correcto:
                ventana1 = Ventana1(self.dato1.get())
                self.ventana.destroy()

            elif usuario_bd is None:
                mb.showerror("Error", "Usuario no encontrado")

            elif usuario_bd["Contraseña"] != self.dato2.get():
                mb.showerror("Error", "Contraseña no coincidente")

            elif usuario_bd["NombreUsuario"] != self.dato1.get() and usuario_bd["Contraseña"] != self.dato2.get():
                mb.showerror("Error", "Usuario y contraseña inválidos")


class Menu:
    def __init__(self,ventana):
        self.ventana = ventana
        self.menubar1 = tk.Menu(ventana)
        ventana.config(menu =self.menubar1)

        #Menu de opciones 1 acerca de
        self.opciones1 = tk.Menu(self.menubar1,tearoff=0)
        self.opciones1.add_command(label="Acerca de...",command=self.acerca)
        self.menubar1.add_cascade(label="Opciones",menu=self.opciones1)

        #Menu de opciones 2 ver admnistradores
        self.opciones2 = tk.Menu(self.menubar1, tearoff=0)
        self.opciones2.add_command(label="Gestionar Administradores",command=self.ver_administradores)
        self.menubar1.add_cascade(label="Administradores",menu=self.opciones2)

    def acerca(self):
        mb.showinfo("Informacion","Gestion de servicios e informacion NewFood")
    def ver_administradores(self):
        ventana_info = tk.Toplevel(self.ventana)
        ventana_info.title("Información de Administradores")
        ventana_info.resizable(0,0)
        ventana_info.grab_set()

        CamposAdministradores = ["Nombre Usuario (primary key)","Nombre Completo","Contraseña","Perfil"]
        self.trewviewusus = ttk.Treeview(ventana_info,columns=CamposAdministradores,show="headings",selectmode="extended")
        for usu in CamposAdministradores:
            self.trewviewusus.heading(usu,text=usu)
            self.trewviewusus.column(usu,width=290)

        #Llenar el Trewview con registros de la base de datos
        conexion = mysql.connector.connect(user="root",password="xlgricky20131415",
                                               host="localhost",database="gestion_newfood",port="3306")
        cursor1 = conexion.cursor()
        cursor1.execute("SELECT * FROM Usuario")
        resultados = cursor1.fetchall()
        for usuario in resultados:
            self.trewviewusus.insert("","end",values=usuario)
        self.trewviewusus.grid(column=0,row=0)
        cursor1.close()
        conexion.close()

        BotonEliminar = ttk.Button(ventana_info,text="Eliminar Usuario",command=self.EliminarUsuario)
        BotonEliminar.grid(column=0,row=1)

        #Label y stringvar de Nombre de Usuario
        self.NombreUsuario = ttk.Label(ventana_info,text="Nombre Usuario")
        self.NombreUsuario.grid(column=0,row=2)

        self.EntradaNombreUsuarioDato = tk.StringVar()
        self.EntradaNombreUsuario = ttk.Entry(ventana_info,textvariable=self.EntradaNombreUsuarioDato)
        self.EntradaNombreUsuario.grid(column=0,row=3)

        #Label y stringvar de Nombre Completo
        self.NombreCompleto = ttk.Label(ventana_info,text="Nombre Completo")
        self.NombreCompleto.grid(column=0,row=4)

        self.EntradaNombreCompletoDato = tk.StringVar()
        self.EntradaNombreCompleto = ttk.Entry(ventana_info,textvariable=self.EntradaNombreCompletoDato)
        self.EntradaNombreCompleto.grid(column=0,row=5)

        #Label y stringvar de contraseña
        self.Contraseña = ttk.Label(ventana_info,text="Contraseña Usuario")
        self.Contraseña.grid(column=0,row=6)

        self.EntradaContraseñaDato = tk.StringVar()
        self.EntradaContraseña = ttk.Entry(ventana_info,textvariable=self.EntradaContraseñaDato)
        self.EntradaContraseña.grid(column=0,row=7)

        #Label y combobox de administrador
        self.Administrador = ttk.Label(ventana_info,text="Seleccione Cargo")
        self.Administrador.grid(column=0,row=8)

        self.opcionadministrador = tk.StringVar()
        opciones = ("Administrador")
        self.comboboxadmin = ttk.Combobox(ventana_info,width=20,textvariable=self.opcionadministrador,values=opciones,state="readonly")
        self.comboboxadmin.current(0)
        self.comboboxadmin.grid(column=0,row=9)
        #Boton de modificar administrador
        BotonModificar = ttk.Button(ventana_info,text="Modificar Usuario",command=self.ModificarUsuario)
        BotonModificar.grid(column=0,row=10)

        #BARRA DE DESPLAZAMIENTOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
        scrollbarusuarioy = ttk.Scrollbar(ventana_info, orient="vertical",command=self.trewviewusus.yview)
        scrollbarusuarioy.grid(row=0, column=1, sticky="ns")

        self.trewviewusus.config(yscrollcommand=scrollbarusuarioy.set)
    def EliminarUsuario(self):
        seleccionusuario = self.trewviewusus.selection()
        if not seleccionusuario:
            mb.showerror("Error","Seleccione un usuario para eliminar")
            return
        nombre_usuario = self.trewviewusus.item(seleccionusuario,"values")[0]
        confirmacion = mb.askokcancel("Confirmar Eliminacion",f"Esta seguro que desea eliminar al usuario {nombre_usuario}?")
        if confirmacion:
            for usu in Usuario.registros:
                if usu["NombreUsuario"] == nombre_usuario:
                    Usuario.registros.remove(usu)
                    mb.showinfo("Exito",f"Usuario {nombre_usuario} eliminado correctamente del diccionario de python")
                    break
            #Eliminar usuario de la base de datos

            conexion1 = mysql.connector.connect(user="root", password="xlgricky20131415", host="localhost",
                                                   database="gestion_newfood", port="3306")
            cursor1 = conexion1.cursor()

            sql = "DELETE FROM Usuario WHERE NombreUsuario = %s"
            valores = (nombre_usuario,)
            cursor1.execute(sql,valores)
            conexion1.commit()

            mb.showinfo("Exito",f"Usuario {nombre_usuario} eliminado correctamente de la base de datos")
            cursor1.close()
            conexion1.close()

        self.trewviewusus.delete(seleccionusuario)

    def ModificarUsuario(self):
        seleccionusuario = self.trewviewusus.selection()
        if not seleccionusuario:
            mb.showerror("Error", "Seleccione un usuario para modificar")
            return

        nuevo_nombre_usuario = self.EntradaNombreUsuarioDato.get()
        nuevo_nombre_completo = self.EntradaNombreCompletoDato.get()
        nueva_contraseña = self.EntradaContraseñaDato.get()
        nuevo_cargo = self.opcionadministrador.get()

        if not nuevo_nombre_usuario or not nuevo_nombre_completo or not nueva_contraseña or not nuevo_cargo:
            mb.showerror("Error", "Todos los campos deben estar llenos para modificar un usuario")
            return
        #Validaciones para contraseña
        if not (any(i.isupper() for i in nueva_contraseña) and "@" in nueva_contraseña):
            mb.showerror("Error","La contraseña debe tener una letra mayuscula y el simbolo '@'")
            return

        # Obtener el nombre de usuario existente que se va a modificar
        nombre_usuario_modificar = self.trewviewusus.item(seleccionusuario, "values")[0]

        # Validar si el nuevo nombre de usuario ya existe
        if self.existe_nombre_usuario(nuevo_nombre_usuario):
            mb.showerror("Error", "El nuevo nombre de usuario ya está en uso. Elija otro.")
            return

        # Actualizar la base de datos
        conexion1 = mysql.connector.connect(user="root", password="xlgricky20131415", host="localhost",
                                            database="gestion_newfood", port="3306")
        cursor1 = conexion1.cursor()

        # Actualizar los datos en la base de datos
        sql = "UPDATE Usuario SET NombreUsuario=%s, NombreCompleto=%s, Contraseña=%s, Perfil=%s WHERE NombreUsuario=%s"
        valores = (nuevo_nombre_usuario, nuevo_nombre_completo, nueva_contraseña, nuevo_cargo, nombre_usuario_modificar)
        cursor1.execute(sql, valores)
        conexion1.commit()

        mb.showinfo("Exito", f"Usuario {nombre_usuario_modificar} ha sido modificado correctamente en la base de datos")
        cursor1.close()
        conexion1.close()
        # Actualizar el diccionario de usuarios
        for usuario in Usuario.registros:
            if usuario["NombreUsuario"] == nombre_usuario_modificar:
                usuario["NombreUsuario"] = nuevo_nombre_usuario
                usuario["NombreCompleto"] = nuevo_nombre_completo
                usuario["Contraseña"] = nueva_contraseña
                usuario["Perfil"] = nuevo_cargo
                mb.showinfo("Exito",f"Usuario {nombre_usuario_modificar} ha sido modificado correctamente en la base de datos")
                break


        # Actualizar el Treeview
        self.trewviewusus.item(seleccionusuario,
                               values=(nuevo_nombre_usuario, nuevo_nombre_completo, nueva_contraseña, nuevo_cargo))

    def existe_nombre_usuario(self, nombre_usuario):
        # Verificar si el nombre de usuario ya existe en la base de datos
        conexion = mysql.connector.connect(user="root", password="xlgricky20131415", host="localhost",
                                           database="gestion_newfood", port="3306")
        cursor = conexion.cursor()
        sql = "SELECT COUNT(*) FROM Usuario WHERE NombreUsuario = %s"
        cursor.execute(sql, (nombre_usuario,))
        cantidad = cursor.fetchone()[0]
        cursor.close()
        conexion.close()
        return cantidad > 0


class labelframe_registrarse:
    def __init__(self,ventana):
        self.ventana = ventana

        self.estilo_labelframe = ttk.Style()

        # Configuracion del Labelframe
        self.estilo_labelframe.configure("EstiloLabelframe.TLabelframe", background="white")

        # Configurar el estilo del texto dentro del Labelframe
        self.estilo_labelframe.configure("EstiloLabelframe.TLabelframe.Label", font=("TkDefaultFont", 12, "bold"))

        self.labelframe1 = ttk.Labelframe(ventana,text="REGISTRARSE",style="EstiloLabelframe.TLabelframe")
        self.labelframe1.grid(column=1, row=0,padx=10,pady=10)

    def cuerpo_principal(self):
        self.texto1 = ttk.Label(self.labelframe1,text="Nombre de Usuario: ",foreground="black",background="#87CEEB",font=("Arial",9,"bold"))
        self.texto1.grid(column=0,row=0,padx=1,pady =1,sticky="e")
        self.dato1 = tk.StringVar()
        self.entrada1 = ttk.Entry(self.labelframe1,width=25,textvariable=self.dato1)
        self.entrada1.grid(column=1,row=0,padx=1,pady=1)

        self.texto2 = ttk.Label(self.labelframe1,text="Nombre Completo: ",foreground="black",background="#87CEEB",font=("Arial",9,"bold"))
        self.texto2.grid(column=0,row=1,padx=1,pady=1,sticky="e")
        self.dato2 = tk.StringVar()
        self.entrada2 = ttk.Entry(self.labelframe1,width=25,textvariable=self.dato2)
        self.entrada2.grid(column=1,row=1,padx=1,pady=1)

        self.texto3 = ttk.Label(self.labelframe1,text="Contraseña: ",foreground="black",background="#87CEEB",font=("Arial",9,"bold"))
        self.texto3.grid(column=0,row=2,padx=1,pady=1,sticky="e")
        self.dato3 = tk.StringVar()
        self.entrada3 = ttk.Entry(self.labelframe1,width=25,textvariable=self.dato3,show="*")
        self.entrada3.grid(column=1,row=2,padx=1,pady=1)

        self.texto4 = ttk.Label(self.labelframe1, text="Perfil: ",foreground="black",background="#87CEEB",font=("Arial",9,"bold"))
        self.texto4.grid(column=0,row=3,padx=1,pady=1,sticky="e")

        self.opcion1 =tk.StringVar()
        administrador1 = ("Administrador")
        self.combobox1 = ttk.Combobox(self.labelframe1,width=22,textvariable=self.opcion1, values=administrador1 ,state="readonly")
        self.combobox1.current(0)
        self.combobox1.grid(column=1,row=3,padx=1,pady=1)

        self.boton1 = ttk.Button(self.labelframe1,text="Registrarse",command=self.apretar)
        self.boton1.grid(column=1,row=4,padx=1,pady=1,sticky="we")
    def apretar(self):
        if self.dato1.get() == "" and self.dato2.get() == "" and self.dato3.get() == "":
            mb.showerror("Error","No se puede registrar con todos los campos vacios")
            return
        elif self.dato1.get() == "" or self.dato2.get() == "" or self.dato3.get() == "":
            mb.showerror("Error","No se puede registrar con alguno de los campos vacios")
            return
        elif not self.validar_contraseña(self.dato3.get()):
            mb.showerror("Error","La contraseña no cumple con los requisitos minimos, tiene que tener una mayuscula y un @ ")
            return
        elif self.usuario_repetido(self.dato1.get()):
            mb.showerror("Error","El nombre de usuario ya esta en uso. Por favor elija otro nombre")
        else:
            Usuario.agregar_usuario(self.dato1.get(), self.dato2.get(), self.dato3.get(), self.opcion1.get())
    def usuario_repetido(self,nombre):
        return any(usuario["NombreUsuario"].lower() == nombre.lower() for usuario in Usuario.registros)

    def validar_contraseña(self,contraseña):
        return any(i.isupper() for i in contraseña) and "@" in contraseña

###CLASES PRINCIPALES###
class Usuario:
    registros = [{"NombreUsuario":"Juan","NombreCompleto":"Juan Alberto Ramirez","Contraseña":"12345","Perfil":"Hacker"},
                 {"NombreUsuario":"aux","NombreCompleto":"aux","Contraseña":"123","Perfil":"seguridad"}]
    @staticmethod
    def agregar_usuario(nombre_usuario, nombre_completo, contraseña, perfil):
        nombre_usuario = nombre_usuario.capitalize()
        nuevo_usuario = {"NombreUsuario": nombre_usuario, "NombreCompleto": nombre_completo, "Contraseña": contraseña, "Perfil": perfil}
        Usuario.registros.append(nuevo_usuario)
        mb.showinfo("Exito", "Usuario registrado correctamente al diccionario de Python")

        try:
        #Conectar a la base de datos
            conexion1 = mysql.connector.connect(user="root",password="xlgricky20131415",host="localhost",database="gestion_newfood",port="3306")
            cursor1 = conexion1.cursor()

        #Agregar datos a la tabla Usuario
            sql = "INSERT INTO Usuario (NombreUsuario,NombreCompleto,Contraseña,Perfil) VALUES (%s,%s,%s,%s)"
            valores = (nombre_usuario, nombre_completo, contraseña, perfil)
            cursor1.execute(sql,valores)
            conexion1.commit()
            mb.showinfo("Exito","Usuario registrado correctamente a la base de datos")
        except mysql.connector.Error:
            mb.showerror("Error","No se puede agregar al/la usuario a la base de datos")
        finally:
            if cursor1:
                cursor1.close()
            if conexion1:
                conexion1.close()


class Ventana1(tk.Tk):
    def __init__(self,nombre):
        super().__init__()
        self.title(f"Bienvenido {nombre} admin al Gestor de datos")
        self.Interfaz()
    def Interfaz(self):
        self.notebook =ttk.Notebook(self)
        self.resizable(0, 0)
        #Creacion de los colores para los botones
        self.estilo = ttk.Style(self)
        self.estilo.configure("Agregar.TButton",background="blue",font=("Arial", 9, "bold"))
        self.estilo.configure("Modificar.TButton",background="green",font=("Arial", 9, "bold"))
        self.estilo.configure("Eliminar.TButton",background="red",font=("Arial", 9, "bold"))
        self.estilo.configure("Buscar.TButton",background="#8B4513",font=("Arial", 9, "bold"))

        #Estilos para label
        self.estilo.configure("1.TLabel", foreground="navy", background="#87CEEB", font=("Arial", 9, "bold"))
        self.estilo.configure("2.TLabel", foreground="black", background="#C0C0C0", font=("Arial", 9, "bold"))
        self.estilo.configure("3.TLabel", foreground="black", background="#FFDAB9", font=("Arial", 9, "bold"))
        self.estilo.configure("4.TLabel", foreground="black", background="#7CFC00", font=("Arial", 9, "bold"))
        self.estilo.configure("5.TLabel", foreground="black", background="#FFC0CB", font=("Arial", 9, "bold"))


        #Estilos para el frame
        self.estilo.configure("Estilo.TFrame", background="lightblue")
        self.estilo.configure("Estilo1.TFrame",background = "#E6E6FA")
        self.estilo.configure("Estulo2.TFrame",background = "#FFE4B5")
        self.estilo.configure("Estilo3.TFrame",background="#98FB98")
        self.estilo.configure("Estilo4.TFrame", background="#FFC0CB")

        #Estilos para el treview
        self.estilo.configure("Treeview.Heading", bordercolor="yellow", background="lightgray")
        self.estilo.configure("Treeview", bordercolor="yellow", background="white")
        #Frame de cliente
        self.administracion = ttk.Frame(self.notebook,style="Estilo.TFrame")
        self.notebook.add(self.administracion,text="Gestor datos Clientes")
        #Frame de evento
        self.gestorevento = ttk.Frame(self.notebook,style="Estilo1.TFrame")
        self.notebook.add(self.gestorevento,text="Gestor datos Eventos")
        #Frame de producto
        self.gestorproducto = ttk.Frame(self.notebook,style="Estulo2.TFrame")
        self.notebook.add(self.gestorproducto,text="Gestor datos productos")
        #Frame de ventas totales
        self.mostradorventas =ttk.Frame(self.notebook,style="Estilo3.TFrame")
        self.notebook.add(self.mostradorventas,text="Total Registros del Diccionario")
        self.notebook.grid(column=0, row=0, sticky="n")

        # Listas de clientes, eventos y productos
        self.clientes = []
        self.eventos = []
        self.productos = []

        # ESTABLECER LA CONEXION CON LA BASE DE DATOS
        conexion = mysql.connector.connect(user="root", password="xlgricky20131415",
                                           host="localhost", database="gestion_newfood", port="3306")

        # Frame de registros en cada Clase
        self.motradorclase = ttk.Frame(self.notebook, style="Estilo4.TFrame")
        self.notebook.add(self.motradorclase, text="Registros en la base de datos")
        #######################################
        TituloBaseDatos = ttk.Label(self.motradorclase,text="CONTADOR DE REGISTROS DE LA BASE DE DATOS - CLIENTE - EVENTO - PRODUCTO",
                                    font=("New Times Roman",12,"bold"),style="5.TLabel")
        TituloBaseDatos.grid(column=0,row=0,padx=1,pady=1,sticky="n")

        self.canvas2 = tk.Canvas(self.motradorclase, width=800, height=230, bg="white")
        self.canvas2.grid(column=0, row=1, padx=10, pady=10)

        #Contador de clientes
        self.contar_clientes()
        self.contar_eventos()
        self.contar_productos()


        #Trewvie 4
        TituloTotal = ttk.Label(self.mostradorventas, text="VENTAS TOTALES - EVENTOS TOTALES - PRODUCTOS TOTALES - PORCENTAJE DE TIPO DE PRODUCTO VENDIDO",
                                font=("New Times Roman", 12, "bold"),style="4.TLabel")
        TituloTotal.grid(column=0, row=0, padx=1, pady=1, sticky="n")
        CamposTotales = ["Clientes Totales", "Eventos Totales", "Productos Totales", "Ventas Totales", "Canape",
                         "Mini-pizzas", "Mini-empanadas", "Sushi", "Mini-chacarero", "Jugo", "Bebida",
                         "PiscoSour", "Champagne", "Vino"]

        self.treeview4 = ttk.Treeview(self.mostradorventas, columns=CamposTotales, show="headings",
                                      selectmode="extended",style="Treeview")
        for dato4 in CamposTotales:
            self.treeview4.heading(dato4, text=dato4)
            self.treeview4.column(dato4, width=100)
        self.treeview4.grid(column=0, row=1, padx=40, pady=40)

        # Crear un canvas en el frame mostradorventas
        self.canvas1 = tk.Canvas(self.mostradorventas, width=800, height=350, bg="white")
        self.canvas1.grid(column=0, row=2, padx=20, pady=20)






        #Label y Entry de productos
        TituloProducto = ttk.Label(self.gestorproducto,text="PRODUCTOS",font=("New Times Roman",12,"bold"),style="3.TLabel")
        TituloProducto.grid(column=0,row=0,padx=1,pady=1,sticky="n")

        NumSerie = ttk.Label(self.gestorproducto,text="Numero de Serie (solo 9 caracteres)",style="3.TLabel")
        NumSerie.grid(column=0,row=1,padx=1,pady=1)
        self.EntradaNumSerie = ttk.Entry(self.gestorproducto,textvariable=tk.StringVar())
        self.EntradaNumSerie.grid(column=0,row=2,padx=1,pady=1)

        TextoProducto =ttk.Label(self.gestorproducto,text="Seleccione un producto",style="3.TLabel")
        TextoProducto.grid(column=0,row=3,padx=1,pady=1)

        tuplaproducto = ("Canape", "Mini-pizzas", "Mini-empanadas", "Sushi", "Mini-chacarero", "Jugo", "Bebida", "PiscoSour", "Champagne", "Vino")
        self.combobox2 = ttk.Combobox(self.gestorproducto,
                                      width=20,textvariable=tk.StringVar(),
                                      values=tuplaproducto,state="readonly")
        self.combobox2.grid(column=0,row=4,padx=1,pady=1)
        self.combobox2.current(0)

        ValorNeto = ttk.Label(self.gestorproducto,text="Valor Neto (valor float)",style="3.TLabel")
        ValorNeto.grid(column=0,row=5,padx=1,pady=1)
        self.EntradaValorNeto = ttk.Entry(self.gestorproducto,textvariable=tk.StringVar())
        self.EntradaValorNeto.grid(column=0,row=6,padx=1,pady=1)

        TextoIdEvento = ttk.Label(self.gestorproducto,text="Clave foranea Id Evento (rango entre 1 y 9)",style="3.TLabel")
        TextoIdEvento.grid(column=0,row=7,padx=1,pady=1)
        self.EntradaIdEvento2 = ttk.Entry(self.gestorproducto,textvariable=tk.StringVar())
        self.EntradaIdEvento2.grid(column=0,row=8,padx=1,pady=1)

        TextoIdCliente = ttk.Label(self.gestorproducto,text="Clave foranea Id Cliente (rango numerico entre 1 y 8)",style="3.TLabel")
        TextoIdCliente.grid(column=0,row=9,padx=1,pady=1)
        self.EntradaIdClienteForeign2 = ttk.Entry(self.gestorproducto,textvariable=tk.StringVar())
        self.EntradaIdClienteForeign2.grid(column=0,row=10,padx=1,pady=1)

        #Declaracion de botones de producto
        self.BotonAgregarProducto = ttk.Button(self.gestorproducto,text="Agregar Producto",width=30,command=self.AgregarProducto,
                                               style="Agregar.TButton")
        self.BotonAgregarProducto.grid(column=0,row=11,padx=5,pady=5)

        self.BotonModificarProducto = ttk.Button(self.gestorproducto,text="Modificar Producto",width=30,command=self.ModificarProducto,
                                                 style="Modificar.TButton")
        self.BotonModificarProducto.grid(column=0,row=12,padx=5,pady=5)

        self.BotonEliminarProducto = ttk.Button(self.gestorproducto,text="Eliminar Producto",width=30,command=self.EliminarProducto,
                                                style="Eliminar.TButton")
        self.BotonEliminarProducto.grid(column=0,row=13,padx=5,pady=5)

        self.BotonBuscarProducto = ttk.Button(self.gestorproducto,text="Buscar Producto por id",width=30,command=self.BuscarProducto,
                                              style="Buscar.TButton")
        self.BotonBuscarProducto.grid(column=0,row=14,padx=5,pady=5)

        self.BusquedaProducto = ttk.Entry(self.gestorproducto,textvariable=tk.StringVar())
        self.BusquedaProducto.grid(column=0,row=15,padx=5,pady=5)

        CamposProducto = ["Numero de serie (primary key)","Tipo de producto","Valor neto","Id evento (foreign key)","Id Cliente (foreign key)"]

        self.treeview3 = ttk.Treeview(self.gestorproducto,columns=CamposProducto,show="headings",
                                      selectmode="extended",style="Treeview")
        for dato2 in CamposProducto:
            self.treeview3.heading(dato2,text=dato2)
            self.treeview3.column(dato2,width=290)
        self.treeview3.grid(column=0,row=16,padx=5,pady=5,sticky="n")

        #Llenamos el Trewvirw con los datos de la base de datos de la tabla Producto
        cursor3 = conexion.cursor()
        cursor3.execute("SELECT * FROM Producto")
        ResultadoProducto = cursor3.fetchall()
        for producto in ResultadoProducto:
            self.treeview3.insert("","end",values=producto)


        scrollbar_y1v3 = ttk.Scrollbar(self.gestorproducto, orient="vertical", command=self.treeview3.yview)
        scrollbar_y1v3.grid(row=16, column=1, sticky="ns")

        scrollbar_x1v3 = ttk.Scrollbar(self.gestorproducto, orient="horizontal", command=self.treeview3.xview)
        scrollbar_x1v3.grid(row=17, column=0, sticky="ew")

        self.treeview3.config(yscrollcommand=scrollbar_y1v3.set, xscrollcommand=scrollbar_x1v3.set)

#Label y Entry de eventos
        TituloEvento = ttk.Label(self.gestorevento,text="EVENTOS",font=("New Times Roman",12,"bold"),style="2.TLabel")
        TituloEvento.grid(column=0,row=0,padx=1,pady=1,sticky="n")

        IdEvento = ttk.Label(self.gestorevento,text="Id Evento (rango entre 1 y 9)",style="2.TLabel")
        IdEvento.grid(column=0,row=1,padx=1,pady=1)
        self.EntradaIdEvento = ttk.Entry(self.gestorevento,textvariable=tk.StringVar())
        self.EntradaIdEvento.grid(column=0,row=2,padx=1,pady=1)

        NombreEvento = ttk.Label(self.gestorevento,text="Nombre Evento",style="2.TLabel")
        NombreEvento.grid(column=0,row=3,padx=1,pady=1)
        self.EntradaNombreEvento = ttk.Entry(self.gestorevento,textvariable=tk.StringVar())
        self.EntradaNombreEvento.grid(column=0,row=4,padx=1,pady=1)

        CantidadEvento = ttk.Label(self.gestorevento,text="Cantidad Personas Evento (minimo 2 personas)",style="2.TLabel")
        CantidadEvento.grid(column=0,row=5,padx=1,pady=1)
        self.EntradaCantidadEvento = ttk.Entry(self.gestorevento,textvariable=tk.StringVar())
        self.EntradaCantidadEvento.grid(column=0,row=6,padx=1,pady=1)

        ProductoxCantidad = ttk.Label(self.gestorevento,text="Producto x Cantidad (minimo 3 productos)",style="2.TLabel")
        ProductoxCantidad.grid(column=0,row=7,padx=1,pady=1)
        self.EntradaProductoxCantidad = ttk.Entry(self.gestorevento,textvariable=tk.StringVar())
        self.EntradaProductoxCantidad.grid(column=0,row=8,padx=1,pady=1)

        FechaEvento = ttk.Label(self.gestorevento,text="Fecha del Evento (dd/mm/yyyy)",style="2.TLabel")
        FechaEvento.grid(column=0,row=9,padx=1,pady=1)
        self.EntradaFechaEvento = ttk.Entry(self.gestorevento,textvariable=tk.StringVar())
        self.EntradaFechaEvento.grid(column=0,row=10,padx=1,pady=1)

        HoraEvento = ttk.Label(self.gestorevento,text="Hora del Evento (HH:MM) (00 a 23 hrs)",style="2.TLabel")
        HoraEvento.grid(column=0,row=11,padx=1,pady=1)
        self.EntradaHoraEvento = ttk.Entry(self.gestorevento,textvariable=tk.StringVar())
        self.EntradaHoraEvento.grid(column=0,row=12,padx=1,pady=1)

        Id_Cliente_Foreign = ttk.Label(self.gestorevento,text="Id Cliente del evento (rango numerico entre 1 y 8)",style="2.TLabel")
        Id_Cliente_Foreign.grid(column=0,row=13,padx=1,pady=1)
        self.EntradaIdClienteForeign = ttk.Entry(self.gestorevento,textvariable=tk.StringVar())
        self.EntradaIdClienteForeign.grid(column=0,row=14,padx=1,pady=1)

        self.BotonAgregarEvento = ttk.Button(self.gestorevento,text="Agregar Evento",width=30,command=self.AgregarEvento,
                                             style="Agregar.TButton")
        self.BotonAgregarEvento.grid(column=0,row=15,padx=5,pady=5)

        self.BotonModificarEvento = ttk.Button(self.gestorevento,text="Modificar Evento",width=30,command=self.ModificarEvento,
                                               style="Modificar.TButton")
        self.BotonModificarEvento.grid(column=0,row=16,padx=5,pady=5)

        self.BotonEliminarEvento = ttk.Button(self.gestorevento,text="Eliminar Evento",width=30,command=self.EliminarEvento,
                                              style="Eliminar.TButton")
        self.BotonEliminarEvento.grid(column=0,row=17,padx=5,pady=5)

        self.BotonBuscarEvento = ttk.Button(self.gestorevento,text="Buscar Evento por id",width=30,command=self.BuscarEvento,
                                            style="Buscar.TButton")
        self.BotonBuscarEvento.grid(column=0,row=18,padx=5,pady=5)

        self.BusquedaEvento = ttk.Entry(self.gestorevento,textvariable=tk.StringVar())
        self.BusquedaEvento.grid(column=0,row=19,padx=5,pady=5)

        #Creacion del trewview
        CamposEvento = ["Id Evento (primary key)","Nombre Evento","Cantidad de personas",
                        "Producto x Cantidad","Fecha Evento","Hora Evento","Id cliente (foreign key)"]

        self.treeview2 = ttk.Treeview(self.gestorevento, columns=CamposEvento, show='headings', selectmode='extended',style="Treeview")
        for dato1 in CamposEvento:
            self.treeview2.heading(dato1,text=dato1)
            self.treeview2.column(dato1,width=200)
        self.treeview2.grid(column=0,row=20,padx=1, pady=1, sticky="n")

        # Llenamos el Trewvirw con los datos de la base de datos de la tabla Cliente

        # Antes de la línea donde se ejecuta la consulta para obtener eventos, agrega un bloque try-except
        cursor2 = conexion.cursor()
        cursor2.execute("SELECT * FROM Evento")
        ResultadoEvento = cursor2.fetchall()
        for evento in ResultadoEvento:
            self.treeview2.insert("","end",values=evento)

        #############################

        scrollbar_y1v2 = ttk.Scrollbar(self.gestorevento, orient="vertical", command=self.treeview2.yview)
        scrollbar_y1v2.grid(row=20, column=2, sticky="ns")

        scrollbar_x1v2 = ttk.Scrollbar(self.gestorevento,orient="horizontal",command=self.treeview2.xview)
        scrollbar_x1v2.grid(row=21, column=0, sticky="ew")

        self.treeview2.config(yscrollcommand=scrollbar_y1v2.set, xscrollcommand=scrollbar_x1v2.set)

#Label y Entry de Cliente
        TituloCliente = ttk.Label(self.administracion,text="CLIENTE", font=("New Times Roman", 12, "bold"),style="1.TLabel")
        TituloCliente.grid(column=0,row=0,padx=1,pady=1,sticky="n")

        IdCliente = ttk.Label(self.administracion,text="Id Cliente (rango numerico entre 1 y 8) (primary key): ",style="1.TLabel")
        IdCliente.grid(column=0,row=1,padx=1,pady=1)
        self.EntradaIdCliente = ttk.Entry(self.administracion,textvariable=tk.StringVar())
        self.EntradaIdCliente.grid(column=0,row=2,padx=1,pady=1)

        NombreCliente = ttk.Label(self.administracion,text="Nombre Cliente: ",style="1.TLabel")
        NombreCliente.grid(column=0,row=3,padx=1,pady=1)
        self.EntradaNombreCliente =ttk.Entry(self.administracion,textvariable=tk.StringVar())
        self.EntradaNombreCliente.grid(column=0,row=4,padx=1,pady=1)

        RunCliente = ttk.Label(self.administracion,text="Run Cliente (rango solo numerico entre 8 y 9): ",style="1.TLabel")
        RunCliente.grid(column=0,row=5,padx=1,pady=1)
        self.EntradaRunCliente = ttk.Entry(self.administracion,textvariable=tk.StringVar())
        self.EntradaRunCliente.grid(column=0,row=6,padx=1,pady=1)

        EmpresaCliente = ttk.Label(self.administracion,text="Empresa Cliente: ",style="1.TLabel")
        EmpresaCliente.grid(column=0,row=7,padx=1,pady=1)
        self.EntradaEmpresaCliente = ttk.Entry(self.administracion,textvariable=tk.StringVar())
        self.EntradaEmpresaCliente.grid(column=0,row=8,padx=1,pady=1)

        ComunaCliente = ttk.Label(self.administracion,text="Comuna Cliente: ",style="1.TLabel")
        ComunaCliente.grid(column=0,row=9,padx=1,pady=1)
        self.EntradaComunaCliente = ttk.Entry(self.administracion,textvariable=tk.StringVar())
        self.EntradaComunaCliente.grid(column=0,row=10,padx=1,pady=1)

        NumeroCliente = ttk.Label(self.administracion,text="Numero del Cliente (numeros enteros entre 8 y 11): ",style="1.TLabel")
        NumeroCliente.grid(column=0,row=11,padx=1,pady=1)
        self.EntradaNumeroCliente = ttk.Entry(self.administracion,textvariable=tk.StringVar())
        self.EntradaNumeroCliente.grid(column=0,row=12,padx=1,pady=1)

        EmailCliente = ttk.Label(self.administracion,text="Email del Cliente: ",style="1.TLabel")
        EmailCliente.grid(column=0,row=13,padx=1,pady=1)
        self.EntradaEmailCliente = ttk.Entry(self.administracion,textvariable=tk.StringVar())
        self.EntradaEmailCliente.grid(column=0,row=14,padx=4,pady=4)

        MetodoPagoCliente = ttk.Label(self.administracion,text="Metodo de pago del Cliente:",style="1.TLabel")
        MetodoPagoCliente.grid(column=0,row=15,padx=4,pady=4)
        tuplametodopago = ("Efectivo","Debito","Credito")
        self.combobox3 = ttk.Combobox(self.administracion,width=20,textvariable=tk.StringVar(),values=tuplametodopago,state="readonly")
        self.combobox3.grid(column=0,row=16,padx=1,pady=1)

        self.combobox3.current(0)

#Botones CRUD Agregar, modificar, eliminar, buscar
        self.boton1 = ttk.Button(self.administracion,text="Agregar Cliente",width=30,command=self.Agregar_Cliente,
                                 style="Agregar.TButton")
        self.boton1.grid(column=0,row=17,padx=1,pady=1)

        self.boton2 = ttk.Button(self.administracion,text="Modificar Cliente",width=30,command=self.Modificar_Cliente,
                                 style="Modificar.TButton")
        self.boton2.grid(column=0,row=18,padx=1,pady=1)

        self.boton3 = ttk.Button(self.administracion,text="Eliminar Cliente",width=30,command=self.Eliminar_Cliente,
                                 style="Eliminar.TButton")
        self.boton3.grid(column=0,row=19,padx=1,pady=1)

        #Entrada de cliente
        self.entrada_busqueda = ttk.Entry(self.administracion,textvariable=tk.StringVar())
        self.entrada_busqueda.grid(column=0, row=21, padx=1, pady=1)

        self.boton4 = ttk.Button(self.administracion,text="Buscar Cliente por Id",width=30,command=self.Buscar_Cliente,
                                 style="Buscar.TButton")
        self.boton4.grid(column=0,row=20,padx=1,pady=1)

        #Creacion del Treewview de la tabla clientes
        CamposCliente = ["IdCliente","Nombre Completo", "Run Cliente",
                         "Empresa Cliente","Comuna Cliente","Numero Cliente","Email Cliente","Metodo Pago Cliente"]
        self.treeview1 = ttk.Treeview(self.administracion,columns=CamposCliente,show='headings',selectmode='extended',style="Treeview")
        for dato in CamposCliente:
            self.treeview1.heading(dato,text=dato)
            self.treeview1.column(dato,width=175)
        self.treeview1.grid(column=0,row=22,padx=1, pady=1, sticky="n")

        #Llenamos el Trewvirw con los datos de la base de datos de la tabla Cliente
        cursor1 = conexion.cursor()
        cursor1.execute("SELECT * FROM Cliente")
        ResultadoCliente = cursor1.fetchall()
        for cliente in ResultadoCliente:
            self.treeview1.insert("","end",values=cliente)

        # Agregar barras de desplazamiento
        scrollbar_y1 = ttk.Scrollbar(self.administracion, orient="vertical", command=self.treeview1.yview)
        scrollbar_y1.grid(row=22, column=2, sticky="ns")

        scrollbar_x1 = ttk.Scrollbar(self.administracion, orient="horizontal", command=self.treeview1.xview)
        scrollbar_x1.grid(row=23, column=0, sticky="ew")

        self.treeview1.config(yscrollcommand=scrollbar_y1.set, xscrollcommand=scrollbar_x1.set)

    def BuscarEvento(self):
        Valor = self.BusquedaEvento.get()
        #Limpiar el Treeview antes de motrar nuevos resultados
        self.treeview2.delete(*self.treeview2.get_children())

        conexion = mysql.connector.connect(user="root", password="xlgricky20131415", host="localhost",
                                           database="gestion_newfood", port="3306")
        cursor = conexion.cursor()
        if not Valor:
            sql = "SELECT * FROM Evento"
            cursor.execute(sql)
        else:
            sql = "SELECT * FROM Evento WHERE IdEvento = %s"
            cursor.execute(sql,(Valor,))
        resultados = cursor.fetchall()
        #Mostrar los resultados en el Treewview
        for evento in resultados:
            self.treeview2.insert("","end",values=evento)

        self.contar_clientes()
        self.contar_eventos()
        self.contar_productos()

        cursor.close()
        conexion.close()


    def Agregar_Cliente(self):
        id_cliente = self.administracion.grid_slaves(row= 2,column=0)[0].get()
        nombre_completo = self.administracion.grid_slaves(row=4, column=0)[0].get()
        run = self.administracion.grid_slaves(row=6, column=0)[0].get()
        empresa = self.administracion.grid_slaves(row=8, column=0)[0].get()
        comuna = self.administracion.grid_slaves(row=10, column=0)[0].get()
        numero = self.administracion.grid_slaves(row=12, column=0)[0].get()
        email = self.administracion.grid_slaves(row=14, column=0)[0].get()
        metodo_pago = self.administracion.grid_slaves(row=16, column=0)[0].get()

        if not all([id_cliente, nombre_completo, run, empresa, comuna, numero, email, metodo_pago]):
            mb.showerror("Error", "Todos los campos deben ser completados")
            return

        if not (id_cliente.isdigit() and numero.isdigit()):
            mb.showerror("Error",
                         "Los campos 'Id Cliente' y 'Numero Cliente' deben contener solo dígitos")
            return

        if not 1 <= len(id_cliente) <= 8:
            mb.showerror("Error", "El rango de id cliente sobrepasa el límite requerido, que es entre 1 y 8")
            return
        if self.primary_cliente_id(id_cliente):
            mb.showerror("Error","El IdCliente ya esta en uso, porque es primary key")
            return


        if not run.isdigit() or not 8 <= len(run) <= 9:
            mb.showerror("Error", "El RUT debe contener solo dígitos y estar en el rango de 8 a 9 caracteres")
            return

        elif not 8 <= len(numero) <= 11:
            mb.showerror("Error", "El rango del número del cliente sobrepasa el límite requerido, que es entre 8 y 11")
            return
        elif not ('@' in email and '.' in email):
            mb.showerror("Error", "La dirección de correo electrónico no es válida. Debe contener '@' y un '.' ")
            return

        nuevo_cliente = Cliente()
        nuevo_cliente.RegistroCliente["IdCliente"] = id_cliente
        nuevo_cliente.RegistroCliente["NombreCompleto"]=nombre_completo
        nuevo_cliente.RegistroCliente["RunCliente"]=run
        nuevo_cliente.RegistroCliente["EmpresaCliente"]=empresa
        nuevo_cliente.RegistroCliente["ComunaCliente"]=comuna
        nuevo_cliente.RegistroCliente["NumeroCliente"]=numero
        nuevo_cliente.RegistroCliente["EmailCliente"]=email
        nuevo_cliente.RegistroCliente["MetodoPago"]=metodo_pago

        self.clientes.append(nuevo_cliente)

        mb.showinfo("Agregado","Cliente agregado al diccionario de Python")

        # Conectar a la base de datos
        conexion = mysql.connector.connect(user="root", password="xlgricky20131415",
                                           host="localhost", database="gestion_newfood", port="3306")
        cursor = conexion.cursor()

        # Insertar el nuevo cliente en la base de datos
        sql = "INSERT INTO Cliente (IdCliente, NombreCliente, RunCliente, EmpresaCliente, ComunaCliente, NumeroCliente, EmailCliente, MetodoPagoCliente) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (id_cliente, nombre_completo, int(run), empresa, comuna, int(numero), email, metodo_pago)
        cursor.execute(sql, valores)

        conexion.commit()
        conexion.close()

        # Limpiar el treeview antes de cargar los datos de la base de datos
        for fila in self.treeview1.get_children():
            self.treeview1.delete(fila)

        # Recuperar datos de la base de datos y cargarlos en el treeview
        conexion = mysql.connector.connect(user="root", password="xlgricky20131415",
                                           host="localhost", database="gestion_newfood", port="3306")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Cliente")
        datos_clientes = cursor.fetchall()
        conexion.close()

        for dato in datos_clientes:
            self.treeview1.insert("", "end", values=dato)
        mb.showinfo("Agregado", "Cliente agregado a la base de datos")

        #Clases que cuentas los clietes, eventos, productos en la base de datos
        self.contar_clientes()
        self.contar_eventos()
        self.contar_productos()

        self.ActualizarTotal()

    def primary_cliente_id(self, id_cliente):
        # Verificar en la lista de clientes en diccionario
        for cliente in self.clientes:
            if cliente.RegistroCliente["IdCliente"] == id_cliente:
                return True

        # Verificar en la base de datos
        conexion = mysql.connector.connect(user="root", password="xlgricky20131415",
                                           host="localhost", database="gestion_newfood", port="3306")
        cursor = conexion.cursor()
        cursor.execute("SELECT IdCliente FROM Cliente WHERE IdCliente = %s", (id_cliente,))
        resultado = cursor.fetchone()
        conexion.close()

        return resultado is not None

    def Eliminar_Cliente(self):
        ItemSeleccionado = self.treeview1.selection()
        if not ItemSeleccionado:
            mb.showerror("Error", "Seleccione un cliente para eliminar")
            return
        id_cliente = self.treeview1.item(ItemSeleccionado, "values")[0]

        # Eliminar registros relacionados de la tabla Producto y Evento
        conexion = mysql.connector.connect(user="root", password="xlgricky20131415", host="localhost",
                                           database="gestion_newfood", port="3306")
        cursor = conexion.cursor()

        try:
            # Eliminar productos relacionados con el cliente
            sql_producto = "DELETE FROM Producto WHERE id_cliente_2 = %s"
            cursor.execute(sql_producto, (id_cliente,))

            # Eliminar eventos relacionados con el cliente
            sql_evento = "DELETE FROM Evento WHERE Id_Cliente = %s"
            cursor.execute(sql_evento, (id_cliente,))

            # Eliminar el cliente de la base de datos
            sql_cliente = "DELETE FROM Cliente WHERE IdCliente = %s"
            cursor.execute(sql_cliente, (id_cliente,))

            conexion.commit()
            mb.showinfo("Eliminado",
                        f"El cliente de id {id_cliente} y sus registros relacionados han sido eliminados de la base de datos")

            # Eliminar el cliente de la lista
            for cliente in self.clientes:
                if cliente.RegistroCliente["IdCliente"] == id_cliente:
                    self.clientes.remove(cliente)
                    mb.showinfo("Eliminado",
                                f"El cliente de id {id_cliente} ha sido eliminado del diccionario de Python")
                    break
            # Eliminar los elementos
            self.contar_clientes()
            self.contar_eventos()
            self.contar_productos()

            self.treeview1.delete(ItemSeleccionado)

        except Exception as e:
            conexion.rollback()
            mb.showerror("Error", f"No se pudo eliminar el cliente. Error: {str(e)}")
        finally:
            cursor.close()
            conexion.close()

        #Actualizar las 3 clases
        self.contar_clientes()
        self.contar_eventos()
        self.contar_productos()

    def Buscar_Cliente(self):
        valor_busqueda = self.entrada_busqueda.get()

        # Limpiar el Treeview antes de mostrar nuevos resultados
        self.treeview1.delete(*self.treeview1.get_children())

        try:
            # Conectar a la base de datos
            conexion = mysql.connector.connect(user="root", password="xlgricky20131415", host="localhost",
                                               database="gestion_newfood", port="3306")
            cursor = conexion.cursor()

            if not valor_busqueda:
                sql = "SELECT * FROM Cliente"
                cursor.execute(sql)
            else:
                sql = "SELECT * FROM Cliente WHERE IdCliente = %s"
                cursor.execute(sql, (valor_busqueda,))
            resultados = cursor.fetchall()
            # Mostrar los resultados en el Treeview
            for cliente in resultados:
                self.treeview1.insert("", "end", values=cliente)

        except mysql.connector.Error as error:
            mb.showerror("Error","Error en la base de datos")
        finally:
            # Cerrar el cursor y la conexión
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()
        self.contar_clientes()
        self.contar_eventos()
        self.contar_productos()

    def Modificar_Cliente(self):
        ItemSeleccionado = self.treeview1.selection()
        if not ItemSeleccionado:
            mb.showerror("Error", "Seleccione un cliente para modificar")
            return
        # Obtener los nuevos valores de los Entry
        nuevo_id_cliente = self.EntradaIdCliente.get()
        nuevo_nombre_cliente = self.EntradaNombreCliente.get()
        nuevo_run_cliente = self.EntradaRunCliente.get()
        nuevo_empresa_cliente = self.EntradaEmpresaCliente.get()
        nuevo_comuna_cliente = self.EntradaComunaCliente.get()
        nuevo_numero_cliente = self.EntradaNumeroCliente.get()
        nuevo_email_cliente = self.EntradaEmailCliente.get()
        nuevo_metodo_pago = self.combobox3.get()
        # Verificar que todos los datos estan ingresados
        if not (nuevo_id_cliente and nuevo_nombre_cliente and nuevo_run_cliente and nuevo_empresa_cliente
                and nuevo_comuna_cliente and nuevo_numero_cliente and nuevo_email_cliente and nuevo_metodo_pago):
            mb.showerror("Error", "Complete todos los campos para modificar el cliente")
            return
        # Validaciones
        if not (nuevo_id_cliente.isdigit() and nuevo_numero_cliente.isdigit()):
            mb.showerror("Error", "Los campos 'Id Cliente' y 'Numero Cliente' deben contener solo dígitos")
            return
        if not 1 <= len(nuevo_id_cliente) <= 8:
            mb.showerror("Error",
                         "El rango de id cliente sobrepasa el límite requerido para modificar, que es entre 1 y 8")
        elif not 8 <= len(nuevo_run_cliente) <= 9:
            mb.showerror("Error", "El rango del run sobrepasa el límite requerido, que es entre 8 y 9")
            return
        elif not 8 <= len(nuevo_numero_cliente) <= 11:
            mb.showerror("Error", "El rango del número del cliente sobrepasa el límite requerido, que es entre 8 y 11")
            return
        elif not ('@' in nuevo_email_cliente and '.' in nuevo_email_cliente):
            mb.showerror("Error", "La dirección de correo electrónico no es válida. Debe contener '@' y un '.' ")
            return

        # Establecemos la conexion con la base de datos
        conexion1 = mysql.connector.connect(user="root", password="xlgricky20131415", host="localhost",
                                            database="gestion_newfood", port="3306")
        cursor1 = conexion1.cursor()

        # Obtener el ID del cliente seleccionado en el treeview
        ClienteSeleccionado = self.treeview1.item(ItemSeleccionado, "values")[0]

        if nuevo_id_cliente != ClienteSeleccionado  and self.existe_id_cliente(nuevo_id_cliente):
            mb.showerror("Error", "El IdCliente ya está en uso en la base de datos")
            return

        # Actualizar la fila en la base de datos
        sql = ("UPDATE Cliente SET IdCliente = %s, NombreCliente = %s, RunCliente = %s, EmpresaCliente = %s, ComunaCliente = %s, NumeroCliente = %s, EmailCliente = %s, "
               "MetodoPagoCliente = %s WHERE IdCliente = %s")

        parametros = (nuevo_id_cliente, nuevo_nombre_cliente, nuevo_run_cliente, nuevo_empresa_cliente,
                      nuevo_comuna_cliente, nuevo_numero_cliente, nuevo_email_cliente,
                      nuevo_metodo_pago, ClienteSeleccionado)

        # Ejecutar la consulta
        cursor1.execute(sql, parametros)

        # Confirmar los cambios y cerrar la conexión
        conexion1.commit()
        mb.showinfo("Modificado", "Cliente modificado en la base de datos")
        cursor1.close()
        conexion1.close()

        # Limpiar el treeview antes de cargar los datos de la base de datos
        for fila in self.treeview1.get_children():
            self.treeview1.delete(fila)

        # Recuperar datos de la base de datos y cargarlos en el treeview
        conexion2 = mysql.connector.connect(user="root", password="xlgricky20131415", host="localhost",
                                            database="gestion_newfood", port="3306")
        cursor2 = conexion2.cursor()
        cursor2.execute("SELECT * FROM Cliente")
        datos_clientes = cursor2.fetchall()
        for dato in datos_clientes:
            self.treeview1.insert("", "end", values=dato)

        # Actualizar en el diccionario
        for i, cliente in enumerate(self.clientes):
            if cliente.RegistroCliente["IdCliente"] == ClienteSeleccionado:
                # Actualizar el cliente en la lista con los nuevos valores
                self.clientes[i].RegistroCliente["IdCliente"] = nuevo_id_cliente
                self.clientes[i].RegistroCliente["NombreCompleto"] = nuevo_nombre_cliente
                self.clientes[i].RegistroCliente["RunCliente"] = nuevo_run_cliente
                self.clientes[i].RegistroCliente["EmpresaCliente"] = nuevo_empresa_cliente
                self.clientes[i].RegistroCliente["ComunaCliente"] = nuevo_comuna_cliente
                self.clientes[i].RegistroCliente["NumeroCliente"] = nuevo_numero_cliente
                self.clientes[i].RegistroCliente["EmailCliente"] = nuevo_email_cliente
                self.clientes[i].RegistroCliente["MetodoPago"] = nuevo_metodo_pago
                mb.showinfo("Actualizado", "Cliente modificado en el diccionario de python")
                break # Salir del bucle después de encontrar y actualizar el cliente

    def existe_id_cliente(self, nuevo_id_cliente):
        # Conectar a la base de datos
        conexion = mysql.connector.connect(user="root", password="xlgricky20131415", host="localhost",
                                           database="gestion_newfood", port="3306")
        cursor = conexion.cursor()

        # Consultar si el IdCliente ya existe en la base de datos
        sql = "SELECT * FROM Cliente WHERE IdCliente = %s"
        cursor.execute(sql, (nuevo_id_cliente,))
        resultado = cursor.fetchone()

        conexion.close()
        return resultado is not None

    def AgregarEvento(self):
        id_evento = self.gestorevento.grid_slaves(row=2,column=0)[0].get()
        nombre_evento = self.gestorevento.grid_slaves(row=4,column=0)[0].get()
        cantidad_evento = self.gestorevento.grid_slaves(row=6,column=0)[0].get()
        productoxcantidad = self.gestorevento.grid_slaves(row=8,column=0)[0].get()
        fecha_evento = self.gestorevento.grid_slaves(row=10,column=0)[0].get()
        hora_evento =self.gestorevento.grid_slaves(row=12,column=0)[0].get()
        id_cliente_foreign = self.gestorevento.grid_slaves(row=14,column=0)[0].get()

        if self.primary_evento_id(id_evento):
            mb.showerror("Error","El Id Evento ya esta en uso, porque es primary key")
            return

        if not all([id_evento,nombre_evento,cantidad_evento,productoxcantidad,fecha_evento,hora_evento,id_cliente_foreign]):
            mb.showerror("Error","Todos los campos deben ser completados para poder ser agregados")
            return
        #Validaciones para Evento
        if not (cantidad_evento.isdigit() and productoxcantidad.isdigit() and id_cliente_foreign.isdigit()):
            mb.showerror("Error","La cantidad de personas en el evento, el productoxcantidad y el id cliente foreign deben ser enteros")
            return

        productoxcantidad = int(productoxcantidad)
        if productoxcantidad < 3:
            mb.showerror("Error","Producto x cantidad debe ser mayor o igual a 3 por persona")
            return
        productoxcantidad*=3
        try:
            fecha_evento = datetime.strptime(fecha_evento,"%d/%m/%Y")
        except ValueError:
            mb.showerror("Error","El formato de fecha es incorrecto. Utiliza el formato dd/mm/yyyy")
            return
        try:
            hora_evento = datetime.strptime(hora_evento, "%H:%M").time()
        except ValueError:
            mb.showerror("Error","El formato de hora es incorrecto. Utiliza el formato HH:MM (00 a 23 hrs)")
            return
        if not 1<=len(id_evento)<=9:
            mb.showerror("Error","El rango de id evento sobrepasa el límite requerido para agregar, que es entre 1 y 9")
            return
        if int(cantidad_evento) < 2:
            mb.showerror("Error", "La cantidad de personas debe ser mayor o igual a 2")
            return
        if not 1 <= len(id_cliente_foreign) <= 8:
            mb.showerror("Error", "El rango de id cliente foreign sobrepasa el límite requerido, que es entre 1 y 8")
            return
        if not self.id_foreign_cliente(id_cliente_foreign):
            mb.showerror("Error","La clave foranea de id_cliente_foreign no existe en la tabla Cliente")
            return

        nuevo_evento =Evento()
        nuevo_evento.RegistoEvento["IdEvento"] = id_evento
        nuevo_evento.RegistoEvento["NombreEvento"]=nombre_evento
        nuevo_evento.RegistoEvento["CantidadEvento"]=cantidad_evento
        nuevo_evento.RegistoEvento["ProductoxCantidad"]=productoxcantidad
        nuevo_evento.RegistoEvento["FechaEvento"]=fecha_evento
        nuevo_evento.RegistoEvento["HoraEvento"]=hora_evento
        nuevo_evento.RegistoEvento["IdClienteForeing"]=id_cliente_foreign

        self.eventos.append(nuevo_evento)
        mb.showinfo("Agregado","Evento agregado al diccionario de Python")

        #Conectar a la base de datos
        conexion = mysql.connector.connect(user="root", password="xlgricky20131415",
                                           host="localhost", database="gestion_newfood", port="3306")
        cursor = conexion.cursor()
        #Insertar el nuevo evento en la base de datos
        sql = ("INSERT INTO Evento (IdEvento, NombreEvento, CantidadPersonasEvento, ProductoCantidad,"
               " FechaEvento, HoraEvento, Id_Cliente) VALUES (%s, %s, %s, %s, %s, %s, %s)")

        valores = (id_evento,nombre_evento,cantidad_evento,productoxcantidad,fecha_evento,hora_evento,id_cliente_foreign)
        cursor.execute(sql,valores)

        conexion.commit()
        conexion.close()

        #Limpiar el trewview antes de cargar los datos en la base de datos
        for fila in self.treeview2.get_children():
            self.treeview2.delete(fila)
        #recupear datos de la base de datos y cargarlos en el trewvirw
        conexion = mysql.connector.connect(user="root", password="xlgricky20131415",
                                           host="localhost", database="gestion_newfood", port="3306")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Evento")
        datos_eventos = cursor.fetchall()
        conexion.close()
        for dato in datos_eventos:
            self.treeview2.insert("","end",values=dato)
        mb.showinfo("Agregado","Evento agregado a la base de datos")

        #Acualizar Las 3 clases
        self.contar_clientes()
        self.contar_eventos()
        self.contar_productos()

        self.ActualizarTotal()
    def primary_evento_id(self,IdEvento):
        return any(evento.RegistoEvento["IdEvento"] == IdEvento for evento in self.eventos)

    def EliminarEvento(self):
        ItemSeleccionado1 = self.treeview2.selection()
        if not ItemSeleccionado1:
            mb.showerror("Error", "Seleccione un evento para eliminar")
            return
        id_evento = self.treeview2.item(ItemSeleccionado1, "values")[0]

        # Eliminar productos relacionados con el evento
        conexion = mysql.connector.connect(user="root", password="xlgricky20131415", host="localhost",
                                           database="gestion_newfood", port="3306")
        cursor = conexion.cursor()

        try:
            # Eliminar productos relacionados con el evento
            sql_producto = "DELETE FROM Producto WHERE id_evento_2 = %s"
            cursor.execute(sql_producto, (id_evento,))

            # Eliminar el evento de la base de datos
            sql_evento = "DELETE FROM Evento WHERE IdEvento = %s"
            cursor.execute(sql_evento, (id_evento,))

            conexion.commit()
            mb.showinfo("Eliminado",
                        f"El evento de id {id_evento} y sus registros relacionados han sido eliminados de la base de datos")

            # Eliminar el evento de la lista
            for evento in self.eventos:
                if evento.RegistoEvento["IdEvento"] == id_evento:
                    self.eventos.remove(evento)
                    mb.showinfo("Eliminado", f"El evento de id {id_evento} ha sido eliminado del diccionario de Python")
                    break

            # Eliminar el evento de la Treeview
            self.treeview2.delete(ItemSeleccionado1)

        except Exception as e:
            conexion.rollback()
            mb.showerror("Error", f"No se pudo eliminar el evento. Error: {str(e)}")
        finally:
            cursor.close()
            conexion.close()
        #Actualizar las 3 clases
        self.contar_clientes()
        self.contar_eventos()
        self.contar_productos()

    def ModificarEvento(self):
        ItemSeleccionado1 = self.treeview2.selection()
        if not ItemSeleccionado1:
            mb.showerror("Error","Seleccione un evento para modificar")
            return
        #Obtener los nuevos valores de los Entry
        nuevo_id_evento = self.EntradaIdEvento.get()
        nuevo_nombre_evento = self.EntradaNombreEvento.get()
        nueva_cantidad_evento = self.EntradaCantidadEvento.get()
        nuevo_productoxcantidad = self.EntradaProductoxCantidad.get()
        nueva_fecha_evento = self.EntradaFechaEvento.get()
        nueva_hora_evento = self.EntradaHoraEvento.get()
        nuevo_id_cliente_foreign = self.EntradaIdClienteForeign.get()

        #Verificar que todos los datos esten ingresados
        if not (nuevo_id_evento and nuevo_nombre_evento and nueva_cantidad_evento and nuevo_productoxcantidad and nueva_fecha_evento and nueva_hora_evento and nuevo_id_cliente_foreign):
            mb.showerror("Error", "Complete todos los campos para modificar el evento")
            return

        if not (nueva_cantidad_evento.isdigit() and nuevo_productoxcantidad.isdigit() and nuevo_id_cliente_foreign.isdigit()):
            mb.showerror("Error", "La cantidad de personas en el evento, el productoxcantidad y el nuevo id cliente deben ser enteros")
            return
        nuevo_productoxcantidad = int(nuevo_productoxcantidad)
        if nuevo_productoxcantidad < 3:
            mb.showerror("Error", "Producto x cantidad debe ser mayor o igual a 3 por persona")
            return
        nuevo_productoxcantidad *= 3
        try:
            fecha_evento = datetime.strptime(nueva_fecha_evento,"%d/%m/%Y")
        except ValueError:
            mb.showerror("Error","El formato de fecha es incorrecto. Utiliza el formato dd/mm/yyyy")
            return
        try:
            hora_evento = datetime.strptime(nueva_hora_evento, "%H:%M").time()
        except ValueError:
            mb.showerror("Error","El formato de hora es incorrecto. Utiliza el formato HH:MM (00 a 23 hrs)")
            return

        if not 1 <= len(nuevo_id_evento) <= 9:
            mb.showerror("Error",
                         "El rango de Id evento sobrepasa el límite requerido para agregar, que es entre 1 y 9")
            return

        if int(nueva_cantidad_evento) < 2:
            mb.showerror("Error", "La cantidad de personas debe ser mayor o igual a 2")
            return

        if not 1 <= len(nuevo_id_cliente_foreign) <= 8:
            mb.showerror("Error", "El rango de Id cliente foreign sobrepasa el límite requerido, que es entre 1 y 8")
            return
        if not self.id_foreign_cliente2(nuevo_id_cliente_foreign):
            mb.showerror("Error de modificacion","La clave foranea de id_cliente_foreign no existe en la tabla Cliente")
            return

        #Establecer conexion con la base de datos
        conexion1 = mysql.connector.connect(user="root",password="xlgricky20131415",
                                            host="localhost",database = "gestion_newfood",port="3306")
        cursor1 = conexion1.cursor()

        #Obtener el ID del Evento seleccionado en el trewview
        EventoSeleccionado = self.treeview2.item(ItemSeleccionado1,"values")[0]


        #Validacion para en el caso de que se desee modificar solo el nombre o cualquier atributo de la entidad
        #Y no se quiera modificar la clave primaria

        if nuevo_id_evento!=EventoSeleccionado and self.existe_id_evento(nuevo_id_evento):
            mb.showerror("Error","El IdEvento ya esta en uso en la base de datos")
            return
        sql = ("UPDATE Evento SET IdEvento = %s, NombreEvento = %s, CantidadPersonasEvento = %s, "
               "ProductoCantidad = %s, FechaEvento = %s, HoraEvento = %s, Id_Cliente = %s "
               "WHERE IdEvento = %s")

        parametros = (nuevo_id_evento, nuevo_nombre_evento, nueva_cantidad_evento, nuevo_productoxcantidad,
                      fecha_evento, hora_evento, nuevo_id_cliente_foreign,EventoSeleccionado)
        #Ejecucion de la consultaaaaaaaaaaaaaaaaaaaaa
        cursor1.execute(sql,parametros)
        conexion1.commit()
        mb.showinfo("Modificado","Evento modificado en la base de datos")
        cursor1.close()
        conexion1.close()

        #Limpiar el trewview antes de cargar los datos de la base de datos
        for fila in self.treeview2.get_children():
            self.treeview2.delete(fila)

        # Recuperar datos de la base de datos y cargarlos en el treeview
        conexion2 = mysql.connector.connect(user="root", password="xlgricky20131415", host="localhost",
                                            database="gestion_newfood", port="3306")
        cursor2 = conexion2.cursor()
        cursor2.execute("SELECT * FROM Evento")
        datos_eventos = cursor2.fetchall()
        for dato in datos_eventos:
            self.treeview2.insert("","end",values=dato)

        #Actualizar en el diccionario
        for i, evento in enumerate(self.eventos):
            if evento.RegistoEvento["IdEvento"]==EventoSeleccionado:
            #Actualizar el evento en la lista con los nuevos valores
                self.eventos[i].RegistoEvento["IdEvento"]= nuevo_id_evento
                self.eventos[i].RegistroEvento["NombreEvento"] =nuevo_nombre_evento
                self.eventos[i].RegistroEvento["CantidadEvento"] = nueva_cantidad_evento
                self.eventos[i].RegistroEvento["ProductoxCantidad"] = nuevo_productoxcantidad
                self.eventos[i].RegistroEvento["FechaEvento"] = nueva_fecha_evento
                self.eventos[i].RegistroEvento["HoraEvento"] = nueva_hora_evento
                self.eventos[i].RegistroEvento["IdClienteForeing"]=nuevo_id_cliente_foreign
                mb.showinfo("Actualizado","Evento modificado en el diccionario de Python")
                break
    def existe_id_evento(self,nuevo_id_evento):
        # Conectar a la base de datos
        conexion = mysql.connector.connect(user="root", password="xlgricky20131415", host="localhost",
                                           database="gestion_newfood", port="3306")
        cursor = conexion.cursor()
        sql = "SELECT * FROM Evento where IdEvento = %s"
        cursor.execute(sql,(nuevo_id_evento,))
        resultado = cursor.fetchone()

        conexion.close()
        return resultado is not None

    def AgregarProducto(self):
        num_serie = self.gestorproducto.grid_slaves(row=2,column=0)[0].get()
        tipo_producto = self.gestorproducto.grid_slaves(row=4,column=0)[0].get()
        valor_neto = self.gestorproducto.grid_slaves(row=6,column=0)[0].get()
        id_evento_foreign = self.gestorproducto.grid_slaves(row=8,column=0)[0].get()
        id_cliente_foreign = self.gestorproducto.grid_slaves(row=10,column=0)[0].get()

        if self.primary_num_serie(num_serie):
            mb.showerror("Error","El NumSerie ya esta en uso, porque es primary key")
            return

        if not all([num_serie,tipo_producto,valor_neto,id_evento_foreign,id_cliente_foreign]):
            mb.showerror("Error","Todos los campos deben ser completados")
            return

        # validaciones
        if not (id_cliente_foreign.isdigit()):
            mb.showerror("Error","El campo id cliente debe contener solo digitos")

        if not len(num_serie) == 9:
            mb.showerror("Error", "El numero de serie del producto debe tener solo y solo 9 caracteres")
            return
        if not 1 <= len(id_cliente_foreign) <= 8:
            mb.showerror("Error", "El rango de id cliente foreign sobrepasa el límite requerido, que es entre 1 y 8")
        if not 1<=len(id_evento_foreign)<=9:
            mb.showerror("Error","El rango de id evento sobrepasa el límite requerido para agregar, que es entre 1 y 9")

        try:
            valor_neto = float(valor_neto)
        except ValueError:
            mb.showerror("Error", "El Valor neto debe ser un número decimal")
            return
        if not self.id_foreign_evento(id_evento_foreign):
            mb.showerror("Error","La clave foranea de id_evento_foreign no existe en la tabla Evento")
            return
        if not self.id_foreign_cliente(id_cliente_foreign):
            mb.showerror("Error","La clave foranea de id_cliente_foreign no existe en la tabla Cliente")
            return



        nuevo_producto = Producto()
        nuevo_producto.RegistroProducto["NumSerie"] = num_serie
        nuevo_producto.RegistroProducto["TipoProducto"] = tipo_producto
        nuevo_producto.RegistroProducto["ValorNeto"] = valor_neto
        nuevo_producto.RegistroProducto["IdEventoForeign"]=id_evento_foreign
        nuevo_producto.RegistroProducto["IdClienteForeign"]=id_cliente_foreign

        self.productos.append(nuevo_producto)

        Producto.TotalValorNeto+=valor_neto

        mb.showinfo("Agregado","Producto agregado al diccionario de Python")
        #Conectar a la base de datos
        conexion = mysql.connector.connect(user="root", password="xlgricky20131415",
                                           host="localhost", database="gestion_newfood", port="3306")
        cursor = conexion.cursor()
        #Insertar el nuevo producto en la base de datos
        sql = "INSERT INTO Producto (NumSerie, TipoProducto, ValorNeto, id_evento_2, id_cliente_2) VALUES (%s, %s, %s, %s, %s)"
        valores = (num_serie, tipo_producto, valor_neto, id_evento_foreign, id_cliente_foreign)
        cursor.execute(sql,valores)
        conexion.commit()
        conexion.close()

        #Limpiar el treewview antes de cargar los datos de la base de datos
        for fila in self.treeview3.get_children():
            self.treeview3.delete(fila)

        # Recuperar datos de la base de datos y cargarlos en el treeview
        conexion = mysql.connector.connect(user="root", password="xlgricky20131415",
                                           host="localhost", database="gestion_newfood", port="3306")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Producto")
        datos_productos = cursor.fetchall()
        conexion.close()

        for dato in datos_productos:
            self.treeview3.insert("","end",values=dato)
        mb.showinfo("Agregado","Producto agregado a la base de datos")

        #Actualizar las 3 clases
        self.contar_clientes()
        self.contar_eventos()
        self.contar_productos()

        self.ActualizarTotal()
        self.GenerarGrafico()
    def primary_num_serie(self,NumSerie):
        #Verificar en la lista Productos en diccionario
        for producto in self.productos:
            if producto.RegistroProducto["NumSerie"]==NumSerie:
                return True
        #Verificar en la base de datos
        conexion = mysql.connector.connect(user = "root",password="xlgricky20131415",host="localhost",
                                           database = "gestion_newfood",port="3306")
        cursor = conexion.cursor()
        cursor.execute("SELECT NumSerie FROM Producto WHERE NumSerie = %s",(NumSerie,))
        resultado = cursor.fetchone()
        conexion.close()
        return resultado is not None


    def ModificarProducto(self):
        ItemSeleccionado3 = self.treeview3.selection()
        if not ItemSeleccionado3:
            mb.showerror("Error","Selecciones un producto para modificar")
            return

        #Obtener los nuevos valores del Entry
        nuevo_num_serie = self.EntradaNumSerie.get()
        nuevo_tipo_producto = self.combobox2.get()
        nuevo_valor_neto = self.EntradaValorNeto.get()
        nuevo_evento_foreign2 = self.EntradaIdEvento2.get()
        nuevo_id_cliente_foreign2 = self.EntradaIdClienteForeign2.get()

        #Verificador de los datos
        if not (nuevo_num_serie and nuevo_tipo_producto and
                nuevo_valor_neto and nuevo_evento_foreign2 and
                nuevo_id_cliente_foreign2):
            mb.showerror("Error","Complete todos los campos para modificar el producto")
            return
        # Validaciones
        if not (nuevo_id_cliente_foreign2.isdigit()):
            mb.showerror("Error", "El campo id cliente debe contener solo dígitos para ser modificado")

        if not len(nuevo_num_serie) == 9:
            mb.showerror("Error", "El número de serie del producto debe tener exactamente 9 caracteres para ser modificado")
            return
        if not 1 <= len(nuevo_id_cliente_foreign2) <= 8:
            mb.showerror("Error",
                             "El rango de id cliente foreign sobrepasa el límite requerido, que es entre 1 y 8")
            return
        if not 1 <= len(nuevo_evento_foreign2) <= 9:
            mb.showerror("Error",
                             "El rango de id evento sobrepasa el límite requerido para modificar, que es entre 1 y 9")
            return
        try:
            nuevo_valor_neto = float(nuevo_valor_neto)
        except ValueError:
            mb.showerror("Error", "El Valor neto debe ser un número decimal")
            return
        if not self.id_foreign_evento(nuevo_evento_foreign2):
            mb.showerror("Error","La clave foranea de id_evento_foreign no existe en la tabla Evento")
            return
        if not self.id_foreign_cliente(nuevo_id_cliente_foreign2):
            mb.showerror("Error","La clave foranea de id_cliente_foreign no existe en la tabla Cliente")
            return

        #Establecer la conexion con la base de datos
        conexion1 = mysql.connector.connect(user="root",password="xlgricky20131415",
                                            host="localhost",database = "gestion_newfood",port="3306")
        cursor1 = conexion1.cursor()

        #Obtener el ID del Producto seleccionado en el trewview

        ProductoSeleccionado = self.treeview3.item(ItemSeleccionado3,"values")[0]

        if nuevo_num_serie!=ProductoSeleccionado and self.existe_id_producto(nuevo_num_serie):
            mb.showerror("Error","El NumSerie ya esta en uso en la base de datos")
            return
        sql = ("UPDATE Producto SET NumSerie = %s, TipoProducto = %s, ValorNeto = %s, id_evento_2 = %s, id_cliente_2 = %s WHERE NumSerie = %s")

        parametros = (nuevo_num_serie,nuevo_tipo_producto,nuevo_valor_neto,nuevo_evento_foreign2,nuevo_id_cliente_foreign2,ProductoSeleccionado)
        #Ejecucion de la consulta
        cursor1.execute(sql,parametros)
        conexion1.commit()
        mb.showinfo("Modificado", "Producto modificado en la base de datos")
        cursor1.close()
        conexion1.close()

        #Limpiar el trewvies antes de cargar los datos de la base de datos
        for fila in self.treeview3.get_children():
            self.treeview3.delete(fila)

        #Recupear datos de la base de datos y cargarlos en el trewview
        conexion2 = mysql.connector.connect(user="root", password="xlgricky20131415", host="localhost",
                                            database="gestion_newfood", port="3306")
        cursor2 = conexion2.cursor()
        cursor2.execute("SELECT * FROM Producto")
        datos_productos = cursor2.fetchall()
        for dato in datos_productos:
            self.treeview3.insert("","end",values=dato)
        #Actualizar en el diccionario
        for i,producto in enumerate(self.productos):
            if producto.RegistroProducto["NumSerie"] == ProductoSeleccionado:
            #Actualizar el producto en la lista con los nuevos valores
                self.productos[i].RegistroProducto["NumSerie"]=nuevo_num_serie
                self.productos[i].RegistroProducto["TipoProducto"]=nuevo_tipo_producto
                self.productos[i].RegistroProducto["ValorNeto"] = nuevo_valor_neto
                self.productos[i].RegistroProducto["IdEventoForeign"] = nuevo_evento_foreign2
                self.productos[i].RegistroProducto["IdClienteForeign"]=nuevo_id_cliente_foreign2
                mb.showinfo("Actualizado","Producto modificado en el diccionario de Python")
                break

    def EliminarProducto(self):
        ItemSeleccionado3 = self.treeview3.selection()
        if not ItemSeleccionado3:
            mb.showerror("Error", "Seleccione un producto para eliminar")
            return
        num_serie = self.treeview3.item(ItemSeleccionado3, "values")[0]

        # Eliminar el producto de la base de datos
        conexion = mysql.connector.connect(user="root", password="xlgricky20131415", host="localhost",
                                           database="gestion_newfood",
                                           port="3306")
        cursor = conexion.cursor()

        try:
            # Eliminar el producto de la base de datos
            sql_producto = "DELETE FROM Producto WHERE NumSerie = %s"
            cursor.execute(sql_producto, (num_serie,))

            conexion.commit()
            mb.showinfo("Eliminado",
                        f"El producto de número de serie {num_serie} ha sido eliminado de la base de datos")

            # Eliminar el producto de la lista
            for x in self.productos:
                if x.RegistroProducto["NumSerie"] == num_serie:
                    self.productos.remove(x)
                    mb.showinfo("Eliminado",
                                f"Producto de número de serie {num_serie} ha sido eliminado del diccionario de Python")
                    break

            # Eliminar el producto de la Treeview
            self.treeview3.delete(ItemSeleccionado3)

        except Exception as e:
            conexion.rollback()
            mb.showerror("Error", f"No se pudo eliminar el producto. Error: {str(e)}")
        finally:
            cursor.close()
            conexion.close()

        #Actualizar las 3 clases
        self.contar_clientes()
        self.contar_eventos()
        self.contar_productos()

    def id_foreign_evento(self,id_evento):
        conexion = mysql.connector.connect(user="root", password="xlgricky20131415", host="localhost",
                                           database="gestion_newfood", port="3306")
        cursor = conexion.cursor()
        cursor.execute("SELECT IdEvento FROM Evento WHERE IdEvento = %s", (id_evento,))
        resultado = cursor.fetchone()
        conexion.close()
        return resultado is not None
    def id_foreign_cliente(self,id_cliente):
        conexion = mysql.connector.connect(user="root", password="xlgricky20131415", host="localhost",
                                           database="gestion_newfood", port="3306")
        cursor = conexion.cursor()
        cursor.execute("SELECT IdCliente FROM Cliente WHERE IdCliente = %s", (id_cliente,))
        resultado = cursor.fetchone()
        conexion.close()
        return resultado is not None
    def id_foreign_cliente2(self,id_cliente):
        conexion = mysql.connector.connect(user="root", password="xlgricky20131415", host="localhost",
                                           database="gestion_newfood", port="3306")
        cursor = conexion.cursor()
        cursor.execute("SELECT IdCliente FROM Cliente WHERE IdCliente = %s", (id_cliente,))
        resultado = cursor.fetchone()
        conexion.close()
        return resultado is not None
    def BuscarProducto(self):
        valor3 = self.BusquedaProducto.get()
        self.treeview3.delete(*self.treeview3.get_children())
        conexion = mysql.connector.connect(user="root", password="xlgricky20131415", host="localhost",
                                           database="gestion_newfood", port="3306")
        cursor = conexion.cursor()
        if not valor3:
            sql = "SELECT * FROM Producto"
            cursor.execute(sql)
        else:
            sql = "SELECT * FROM Producto WHERE NumSerie = %s"
            cursor.execute(sql,(valor3,))
        resultados = cursor.fetchall()
        #Mostrar los resultados en el Treewview
        for producto in resultados:
            self.treeview3.insert("","end",values=producto)
        self.contar_clientes()
        self.contar_eventos()
        self.contar_productos()

        cursor.close()
        conexion.close()


    def existe_id_producto(self,nuevo_id_producto):
    # Conectar a la base de datos
        conexion = mysql.connector.connect(user="root", password="xlgricky20131415", host="localhost",
                                           database="gestion_newfood", port="3306")
        cursor = conexion.cursor()
        sql = "SELECT * FROM Producto WHERE NumSerie = %s"
        cursor.execute(sql,(nuevo_id_producto,))
        resultado = cursor.fetchone()
        conexion.close()
        return resultado is not None


    def ActualizarTotal(self):
        num_clientes = Cliente.NumClientes
        num_eventos = Evento.NumEventos
        num_productos = Producto.NumProductos
        total_valor_neto = Producto.TotalValorNeto

    # la funcion hassattr verifica si el Treeview ya está creado, y no se vuelva a crear el treeview4 de forma innecesaria
        if not hasattr(self, 'treeview4'):
            CamposTotales = ["Clientes Totales", "Eventos Totales", "Productos Totales", "Ventas Totales",
                             "Canape",
                             "Mini-pizzas",
                             "Mini-empanadas",
                             "Sushi",
                             "Mini-chacarero",
                             "Jugo",
                             "Bebida",
                         "PiscoSour", "Champagne", "Vino"]
            self.treeview4 = ttk.Treeview(self.mostradorventas, columns=CamposTotales, show="headings",
                                      selectmode="extended")
            for dato4 in CamposTotales:
                self.treeview4.heading(dato4, text=dato4)
                self.treeview4.column(dato4, width=100)
                self.treeview4.grid(column=0, row=1, padx=40, pady=40)
    # Calcular el porcentaje de cada producto
        porcentajes_productos = {}
        for producto in ["Canape", "Mini-pizzas", "Mini-empanadas", "Sushi", "Mini-chacarero", "Jugo", "Bebida",
                     "PiscoSour", "Champagne", "Vino"]:
            count_producto = sum(1 for prod in self.productos if prod.RegistroProducto["TipoProducto"] == producto)
            porcentaje_producto = (count_producto / num_productos) * 100 if num_productos > 0 else 0 #Operador ternario
            porcentajes_productos[producto] = round(porcentaje_producto, 2)

        self.treeview4.delete(*self.treeview4.get_children())  # Se borran todos los elementos

    # Inserta una nueva fila con los valores actualizados
        self.treeview4.insert("", "end", values=(
            num_clientes, num_eventos, num_productos, total_valor_neto,
            porcentajes_productos["Canape"], porcentajes_productos["Mini-pizzas"], porcentajes_productos["Mini-empanadas"],
            porcentajes_productos["Sushi"], porcentajes_productos["Mini-chacarero"], porcentajes_productos["Jugo"],
            porcentajes_productos["Bebida"], porcentajes_productos["PiscoSour"], porcentajes_productos["Champagne"],
            porcentajes_productos["Vino"]
        ))

    def GenerarGrafico(self):
        num_productos = Producto.NumProductos
        porcentajes_productos = {}

        # Paleta de colores para cada tipo de producto
        colores = {
            "Canape": "blue",
            "Mini-pizzas": "green",
            "Mini-empanadas": "yellow",
            "Sushi": "orange",
            "Mini-chacarero": "purple",
            "Jugo": "pink",
            "Bebida": "brown",
            "PiscoSour": "gray",
            "Champagne": "cyan",
            "Vino": "red"
        }

        # Calcular porcentajes y encontrar el máximo
        #Keys devuelve una vista de todas las claves en el diccionario a diferencia de items, por lo tanto iteramos sobre las claves
        for producto in colores.keys():
            #Misma regla de 3 que el anterior codigo
            count_producto = sum(1 for prod in self.productos if prod.RegistroProducto["TipoProducto"] == producto)
            porcentaje_producto = (count_producto / num_productos) * 100 if num_productos > 0 else 0

            #Despues de efectuar la regla de 3 lo agregamos al diccionario
            porcentajes_productos[producto] = porcentaje_producto

        # Grados para cada producto
        #Usamdo la llamada "lista de comprension" llamando al metodo get
        grados = [porcentajes_productos.get(producto, 0) * 3.6 for producto in colores.keys()]

        # Coordenadas del cuadro que contiene el gráfico
        cuadro = [5, 5, 300, 300]

        # Dibujar arcos individuales para cada producto
        #
        for i, producto in enumerate(colores.keys()):
            grado = grados[i]

            # Calcular los ángulos de inicio y final para cada arco
            #el uso [:i] crea una sublista de todos los elementos desde el principio hasta el indice i-1 de la lista grados

            angulo_inicio = sum(grados[:i])
            angulo_final = angulo_inicio + grado

            # Dibujar el arco con el color correspondiente al producto
            self.canvas1.create_arc(*cuadro, fill=colores[producto], start=angulo_inicio, extent=grado)
        self.canvas1.create_text(500,50,text="Canape",fill="blue",font="Arial")
        self.canvas1.create_text(500, 70, text="Mini-pizzas", fill="green", font="Arial")
        self.canvas1.create_text(500, 90, text="Mini-empanadas", fill="yellow", font="Arial")
        self.canvas1.create_text(500, 110, text="Sushi", fill="orange", font="Arial")
        self.canvas1.create_text(500, 130, text="Mini-chacarero", fill="purple", font="Arial")
        self.canvas1.create_text(500, 150, text="Jugo", fill="pink", font="Arial")
        self.canvas1.create_text(500, 170, text="Bebida", fill="brown", font="Arial")
        self.canvas1.create_text(500, 190, text="PiscoSour", fill="gray", font="Arial")
        self.canvas1.create_text(500, 210, text="Champagne", fill="cyan", font="Arial")
        self.canvas1.create_text(500, 230, text="Vino", fill="red", font="Arial")

    def contar_clientes(self):
        conexion = mysql.connector.connect(user="root", password="xlgricky20131415", host="localhost",
                                           database="gestion_newfood", port="3306")
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM Cliente")
        cantidad_clientes = cursor.fetchone()[0]

        label_clientes = tk.Label(self.motradorclase, text=f"Clientes: {cantidad_clientes}")
        self.canvas2.create_window(10, 10, anchor='nw', window=label_clientes)

        # Mostrar resultado en el Canvas
        self.canvas2.create_rectangle(10, 40, 10 + cantidad_clientes * 10, 70, fill="blue",outline="gold")

    def contar_eventos(self):
        conexion = mysql.connector.connect(user="root", password="xlgricky20131415", host="localhost",
                                           database="gestion_newfood", port="3306")
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM Evento")
        cantidad_eventos = cursor.fetchone()[0]

        label_eventos = tk.Label(self.motradorclase, text=f"Eventos: {cantidad_eventos}")
        self.canvas2.create_window(10, 80, anchor='nw', window=label_eventos)

        # Mostrar resultado en el Canvas
        self.canvas2.create_rectangle(10, 110, 10 + cantidad_eventos * 10, 140, fill="green",outline="gold")

    def contar_productos(self):
        conexion = mysql.connector.connect(user="root", password="xlgricky20131415", host="localhost",
                                           database="gestion_newfood", port="3306")
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM Producto")
        cantidad_productos = cursor.fetchone()[0]

        label_productos = tk.Label(self.motradorclase, text=f"Productos: {cantidad_productos}")
        self.canvas2.create_window(10, 150, anchor='nw', window=label_productos)

        # Mostrar resultado en el Canvas
        self.canvas2.create_rectangle(10, 180, 10 + cantidad_productos * 10, 210, fill='red',outline="gold")


#Clases Principales
class Cliente:
    NumClientes = 0
    def __init__(self):
        self.RegistroCliente = {"IdCliente":"",
                                "NombreCompleto":"","RunCliente": "","EmpresaCliente":"","ComunaCliente":"","NumeroCliente":"","EmailCliente":"","MetodoPago":""}
        Cliente.NumClientes+=1

class Evento:
    NumEventos = 0
    def __init__(self):
        self.RegistoEvento = {"IdEvento":"","NombreEvento":"","CantidadEvento":"","ProductoxCantidad":"","FechaEvento":"","HoraEvento":"","IdClienteForeing":""}
        Evento.NumEventos+=1
class Producto:
    NumProductos = 0
    TotalValorNeto = 0
    def __init__(self):
        self.RegistroProducto ={
            "NumSerie":"",
            "TipoProducto":"",
            "ValorNeto":"",
            "IdEventoForeign":"",
            "IdClienteForeign":""
        }
        Producto.NumProductos+=1