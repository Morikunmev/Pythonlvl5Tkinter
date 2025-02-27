import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from datetime import datetime

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
            mb.showerror("Error","No se puede ingresar con los campos vacios")
        elif self.dato1.get() == "" or self.dato2.get() == "":
            mb.showerror("Error","Uno de los campos tiene que estar completo")
        else:
            usuario_correcto = False
            for registro in Usuario.registros:
                if registro["NombreUsuario"] == self.dato1.get() and registro["Contraseña"] == self.dato2.get():
                    usuario_correcto = True
                    break
            if usuario_correcto:
                ventana1 = Ventana1(self.dato1.get())
                self.ventana.destroy()

            elif registro["NombreUsuario"] !=self.dato1.get() and registro["Contraseña"] ==self.dato2.get():
                mb.showerror("Error","Usuario no encontrado")

            elif registro["NombreUsuario"] == self.dato1.get() and registro["Contraseña"] != self.dato2.get():
                mb.showerror("Error","Contraseña no coincidente")

            elif registro["NombreUsuario"] != self.dato1.get() and registro["Contraseña"] != self.dato2.get():
                mb.showerror("Error","Usuario y contraseña invalidas")

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
        for usuario in Usuario.registros:
            self.trewviewusus.insert("","end",values=(usuario["NombreUsuario"], usuario["NombreCompleto"],
                                               usuario["Contraseña"], usuario["Perfil"]))
            self.trewviewusus.grid(column=0,row=0)
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
                    mb.showinfo("Exito",f"Usuario {nombre_usuario} eliminado correctamente")
                    break
        self.trewviewusus.delete(seleccionusuario)
    def ModificarUsuario(self):
        seleccionusuario = self.trewviewusus.selection()
        if not seleccionusuario:
            mb.showerror("Error", "Seleccione un usuario para modificar")
            return
        nuevo_nombre_usuario = self.EntradaNombreUsuarioDato.get()
        nuevo_nombre_completo = self.EntradaNombreCompletoDato.get()
        nueva_contraseña_usuario = self.EntradaContraseñaDato.get()
        nuevo_perfil_administrador = self.opcionadministrador.get()

        if not (nuevo_nombre_usuario and nuevo_nombre_completo
                and nueva_contraseña_usuario and
                nuevo_perfil_administrador):
            mb.showerror("Error","Complete todos los campos para modificar el usuario")
            return
        #Validaciones para contraseña
        if not (any(i.isupper() for i in nueva_contraseña_usuario) and "@" in nueva_contraseña_usuario):
            mb.showerror("Error","La contraseña debe tener una letra mayuscula y el simbolo '@'")
            return
        #Obtener el indice
        indice_usuario = int(self.trewviewusus.index(seleccionusuario))
        #Actualizar los valores de la lista, del trewview w w w
        Usuario.registros[indice_usuario]["NombreUsuario"] = nuevo_nombre_usuario
        Usuario.registros[indice_usuario]["NombreCompleto"] = nuevo_nombre_completo
        Usuario.registros[indice_usuario]["Contraseña"] = nueva_contraseña_usuario
        Usuario.registros[indice_usuario]["Perfil"]=nuevo_perfil_administrador

        self.trewviewusus.item(seleccionusuario,values=(nuevo_nombre_usuario,nuevo_nombre_completo,nueva_contraseña_usuario,
                                                        nuevo_perfil_administrador))
        mb.showinfo("Actualizado",f"Usuario {nuevo_nombre_usuario} modificado correctamente")
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
        else:
            Usuario.agregar_usuario(self.dato1.get(), self.dato2.get(), self.dato3.get(), self.opcion1.get())


    def validar_contraseña(self,contraseña):
        return any(i.isupper() for i in contraseña) and "@" in contraseña

###CLASES PRINCIPALES###
class Usuario:
    registros = [{"NombreUsuario":"Richard","NombreCompleto":"Richard Rocuant Obreque","Contraseña":"1234","Perfil":"Administrador"},
                 {"NombreUsuario":"Juan","NombreCompleto":"Juan Alberto Ramirez","Contraseña":"12345","Perfil":"Administracion"}]

    def agregar_usuario(nombre_usuario, nombre_completo, contraseña, perfil):
        nombre_usuario = nombre_usuario.capitalize()
        nuevo_usuario = {"NombreUsuario": nombre_usuario, "NombreCompleto": nombre_completo, "Contraseña": contraseña, "Perfil": perfil}
        Usuario.registros.append(nuevo_usuario)
        mb.showinfo("Exito", "Usuario registrado correctamente")


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

        #Estilos para el frame
        self.estilo.configure("Estilo.TFrame", background="lightblue")
        self.estilo.configure("Estilo1.TFrame",background = "#E6E6FA")
        self.estilo.configure("Estulo2.TFrame",background = "#FFE4B5")
        self.estilo.configure("Estilo3.TFrame",background="#98FB98")

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
        self.notebook.add(self.mostradorventas,text="Total")

        self.notebook.grid(column=0, row=0, sticky="n")

        # Listas de clientes, eventos y productos
        self.clientes = []
        self.eventos = []
        self.productos = []

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


#Label y Entry de productos
        TituloProducto = ttk.Label(self.gestorproducto,text="PRODUCTOS",font=("New Times Roman",12,"bold"),style="3.TLabel")
        TituloProducto.grid(column=0,row=0,padx=1,pady=1,sticky="n")

        NumSerie = ttk.Label(self.gestorproducto,text="Numero de Serie (solo 9 caracteres)",style="3.TLabel")
        NumSerie.grid(column=0,row=1,padx=1,pady=1)
        self.EntradaNumSerie = ttk.Entry(self.gestorproducto,textvariable=tk.StringVar())
        self.EntradaNumSerie.grid(column=0,row=2,padx=1,pady=1)

        TextoProducto =ttk.Label(self.gestorproducto,text="Seleccione un producto",style="3.TLabel")
        TextoProducto.grid(column=0,row=3,padx=1,pady=1)

        tuplaproducto = ("Canape", "Cinipizzas", "Mini-empanadas", "Sushi", "Mini-chacarero", "Jugo", "Bebida", "Pisco sour", "Champagne", "Vino")
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

        CamposEvento = ["Id Evento (primary key)","Nombre Evento","Cantidad de personas",
                        "Producto x Cantidad","Fecha Evento","Hora Evento","Id cliente (foreign key)"]

        self.treeview2 = ttk.Treeview(self.gestorevento, columns=CamposEvento, show='headings', selectmode='extended',style="Treeview")
        for dato1 in CamposEvento:
            self.treeview2.heading(dato1,text=dato1)
            self.treeview2.column(dato1,width=200)
        self.treeview2.grid(column=0,row=20,padx=1, pady=1, sticky="n")

        scrollbar_y1v2 = ttk.Scrollbar(self.gestorevento, orient="vertical", command=self.treeview2.yview)
        scrollbar_y1v2.grid(row=20, column=2, sticky="ns")

        scrollbar_x1v2 = ttk.Scrollbar(self.gestorevento,orient="horizontal",command=self.treeview2.xview)
        scrollbar_x1v2.grid(row=21, column=0, sticky="ew")

        self.treeview2.config(yscrollcommand=scrollbar_y1v2.set, xscrollcommand=scrollbar_x1v2.set)

#Label y Entry de Cliente
        TituloCliente = ttk.Label(self.administracion,text="CLIENTE", font=("New Times Roman", 12, "bold"),style="1.TLabel")
        TituloCliente.grid(column=0,row=0,padx=1,pady=1,sticky="n")

        IdCliente = ttk.Label(self.administracion,text="Id Cliente (rango numerico entre 1 y 8): ",style="1.TLabel")
        IdCliente.grid(column=0,row=1,padx=1,pady=1)
        self.EntradaIdCliente = ttk.Entry(self.administracion,textvariable=tk.StringVar())
        self.EntradaIdCliente.grid(column=0,row=2,padx=1,pady=1)

        NombreCliente = ttk.Label(self.administracion,text="Nombre Cliente: ",style="1.TLabel")
        NombreCliente.grid(column=0,row=3,padx=1,pady=1)
        self.EntradaNombreCliente =ttk.Entry(self.administracion,textvariable=tk.StringVar())
        self.EntradaNombreCliente.grid(column=0,row=4,padx=1,pady=1)

        RunCliente = ttk.Label(self.administracion,text="Run Cliente (rango entre 8 y 9): ",style="1.TLabel")
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
        tuplametodopago = ("Efecto","Debito","Credito")
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

        CamposCliente = ["IdCliente","Nombre Completo", "Run Cliente",
                         "Empresa Cliente","Comuna Cliente","Numero Cliente","Email Cliente","Metodo Pago Cliente"]
        self.treeview1 = ttk.Treeview(self.administracion,columns=CamposCliente,show='headings',selectmode='extended',style="Treeview")
        for dato in CamposCliente:
            self.treeview1.heading(dato,text=dato)
            self.treeview1.column(dato,width=175)
        self.treeview1.grid(column=0,row=22,padx=1, pady=1, sticky="n")


        # Agregar barras de desplazamiento
        scrollbar_y1 = ttk.Scrollbar(self.administracion, orient="vertical", command=self.treeview1.yview)
        scrollbar_y1.grid(row=22, column=2, sticky="ns")

        scrollbar_x1 = ttk.Scrollbar(self.administracion, orient="horizontal", command=self.treeview1.xview)
        scrollbar_x1.grid(row=23, column=0, sticky="ew")

        self.treeview1.config(yscrollcommand=scrollbar_y1.set, xscrollcommand=scrollbar_x1.set)

    def BuscarEvento(self):
        #Limpiar la treeview antes de realizar la busqueda
        self.treeview2.delete(*self.treeview2.get_children())
        Valor = self.BusquedaEvento.get()

        if not Valor:
            for evento in self.eventos:
                self.treeview2.insert("", "end", values=(
                    evento.RegistoEvento["IdEvento"],
                    evento.RegistoEvento["NombreEvento"],
                    evento.RegistoEvento["CantidadEvento"],
                    evento.RegistoEvento["ProductoxCantidad"],
                    evento.RegistoEvento["FechaEvento"],
                    evento.RegistoEvento["HoraEvento"],
                    evento.RegistoEvento["IdClienteForeing"]
                ))
        else:
            self.treeview2.delete(*self.treeview2.get_children())
            for i in self.eventos:
                if Valor == i.RegistoEvento["IdEvento"]:
                    self.treeview2.insert("", "end", values=(
                        i.RegistoEvento["IdEvento"],
                        i.RegistoEvento["NombreEvento"],
                        i.RegistoEvento["CantidadEvento"],
                        i.RegistoEvento["ProductoxCantidad"],
                        i.RegistoEvento["FechaEvento"],
                        i.RegistoEvento["HoraEvento"],
                        i.RegistoEvento["IdClienteForeing"]))

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
        elif not 8 <= len(run) <= 9:
            mb.showerror("Error", "El rango del run sobrepasa el límite requerido, que es entre 8 y 9")
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

        #Actualizar la visualizacion de la lista
        self.treeview1.insert("", "end", values=(
            nuevo_cliente.RegistroCliente["IdCliente"],
            nuevo_cliente.RegistroCliente["NombreCompleto"],
            nuevo_cliente.RegistroCliente["RunCliente"],
            nuevo_cliente.RegistroCliente["EmpresaCliente"],
            nuevo_cliente.RegistroCliente["ComunaCliente"],
            nuevo_cliente.RegistroCliente["NumeroCliente"],
            nuevo_cliente.RegistroCliente["EmailCliente"],
            nuevo_cliente.RegistroCliente["MetodoPago"]
        ))
        self.ActualizarTotal()

    def Eliminar_Cliente(self):
        ItemSeleccionado = self.treeview1.selection()
        if not ItemSeleccionado:
            mb.showerror("Error","Seleccione un cliente para eliminar")
            return
        id_cliente = self.treeview1.item(ItemSeleccionado, "values")[0]

        # Eliminar el cliente de la lista
        for cliente in self.clientes:
            if cliente.RegistroCliente["IdCliente"] == id_cliente:
                self.clientes.remove(cliente)
                break

        # Eliminar los elementos
        self.treeview1.delete(ItemSeleccionado)

    def Buscar_Cliente(self):
        self.treeview1.delete(*self.treeview1.get_children())
        Valor = self.entrada_busqueda.get()


        if not Valor:
            for cliente in self.clientes:
                self.treeview1.insert("", "end", values=(
                    cliente.RegistroCliente["IdCliente"],
                    cliente.RegistroCliente["NombreCompleto"],
                    cliente.RegistroCliente["RunCliente"],
                    cliente.RegistroCliente["EmpresaCliente"],
                    cliente.RegistroCliente["ComunaCliente"],
                    cliente.RegistroCliente["NumeroCliente"],
                    cliente.RegistroCliente["EmailCliente"],
                    cliente.RegistroCliente["MetodoPago"]
                ))
        else:
            #Obtener los clientes que coincidan con el valor
            self.treeview1.delete(*self.treeview1.get_children())
            for cliente in self.clientes:
                if Valor == cliente.RegistroCliente["IdCliente"]:
                    self.treeview1.insert("", "end", values=(
                        cliente.RegistroCliente["IdCliente"],
                        cliente.RegistroCliente["NombreCompleto"],
                        cliente.RegistroCliente["RunCliente"],
                        cliente.RegistroCliente["EmpresaCliente"],
                        cliente.RegistroCliente["ComunaCliente"],
                        cliente.RegistroCliente["NumeroCliente"],
                        cliente.RegistroCliente["EmailCliente"],
                        cliente.RegistroCliente["MetodoPago"]
                    ))

    def Modificar_Cliente(self):
        ItemSeleccionado = self.treeview1.selection()
        if not ItemSeleccionado:
            mb.showerror("Error","Seleccione un cliente para modificar")
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
#Verificar que todos los datos estan ingresados
        if not (nuevo_id_cliente and nuevo_nombre_cliente and nuevo_run_cliente and nuevo_empresa_cliente
                and nuevo_comuna_cliente and nuevo_numero_cliente and nuevo_email_cliente and nuevo_metodo_pago):
            mb.showerror("Error", "Complete todos los campos para modificar el cliente")
            return
        #Validaciones
        if not (nuevo_id_cliente.isdigit() and nuevo_numero_cliente.isdigit()):
            mb.showerror("Error","Los campos 'Id Cliente' y 'Numero Cliente' deben contener solo dígitos")
            return
        if not 1<=len(nuevo_id_cliente)<=8:
            mb.showerror("Error","El rango de id cliente sobrepasa el límite requerido para modificar, que es entre 1 y 8")
        elif not 8<=len(nuevo_run_cliente)<=9:
            mb.showerror("Error", "El rango del run sobrepasa el límite requerido, que es entre 8 y 9")
            return
        elif not 8 <= len(nuevo_numero_cliente) <= 11:
            mb.showerror("Error", "El rango del número del cliente sobrepasa el límite requerido, que es entre 8 y 11")
            return
        elif not ('@' in nuevo_email_cliente and '.' in nuevo_email_cliente):
            mb.showerror("Error", "La dirección de correo electrónico no es válida. Debe contener '@' y un '.' ")
            return
        # Obtener el indice numerico de la fila seleccionada
        indice_cliente = int(self.treeview1.index(ItemSeleccionado))
        #Actualizar los valores de la lista clientes segun el indice encontrado en hacer click
        cliente_seleccionado = self.clientes[indice_cliente]
        cliente_seleccionado.id_cliente = nuevo_id_cliente
        cliente_seleccionado.nombre_completo = nuevo_nombre_cliente
        cliente_seleccionado.run = nuevo_run_cliente
        cliente_seleccionado.empresa = nuevo_empresa_cliente
        cliente_seleccionado.comuna = nuevo_comuna_cliente
        cliente_seleccionado.numero_contacto = nuevo_numero_cliente
        cliente_seleccionado.email = nuevo_email_cliente
        cliente_seleccionado.metodo_pago = nuevo_metodo_pago

        #Actualizar la visualizacion en el Treeview1

        self.treeview1.item(ItemSeleccionado, values=(
            nuevo_id_cliente, nuevo_nombre_cliente, nuevo_run_cliente, nuevo_empresa_cliente,
            nuevo_comuna_cliente, nuevo_numero_cliente, nuevo_email_cliente, nuevo_metodo_pago
        ))

        mb.showinfo("Exito","Cliente modificado exitosamente")
    def AgregarEvento(self):
        id_evento = self.gestorevento.grid_slaves(row=2,column=0)[0].get()
        nombre_evento = self.gestorevento.grid_slaves(row=4,column=0)[0].get()
        cantidad_evento = self.gestorevento.grid_slaves(row=6,column=0)[0].get()
        productoxcantidad = self.gestorevento.grid_slaves(row=8,column=0)[0].get()
        fecha_evento = self.gestorevento.grid_slaves(row=10,column=0)[0].get()
        hora_evento =self.gestorevento.grid_slaves(row=12,column=0)[0].get()
        id_cliente_foreign = self.gestorevento.grid_slaves(row=14,column=0)[0].get()

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

        nuevo_evento =Evento()
        nuevo_evento.RegistoEvento["IdEvento"] = id_evento
        nuevo_evento.RegistoEvento["NombreEvento"]=nombre_evento
        nuevo_evento.RegistoEvento["CantidadEvento"]=cantidad_evento
        nuevo_evento.RegistoEvento["ProductoxCantidad"]=productoxcantidad
        nuevo_evento.RegistoEvento["FechaEvento"]=fecha_evento
        nuevo_evento.RegistoEvento["HoraEvento"]=hora_evento
        nuevo_evento.RegistoEvento["IdClienteForeing"]=id_cliente_foreign

        self.eventos.append(nuevo_evento)

        #Actualizar la visualizacion de la lista Evento
        self.treeview2.insert("","end",values=(
            nuevo_evento.RegistoEvento["IdEvento"],
            nuevo_evento.RegistoEvento["NombreEvento"],
            nuevo_evento.RegistoEvento["CantidadEvento"],
            nuevo_evento.RegistoEvento["ProductoxCantidad"],
            nuevo_evento.RegistoEvento["FechaEvento"],
            nuevo_evento.RegistoEvento["HoraEvento"],
            nuevo_evento.RegistoEvento["IdClienteForeing"]
        ))
        self.ActualizarTotal()
    def EliminarEvento(self):
        ItemSeleccionado1 = self.treeview2.selection()
        if not ItemSeleccionado1:
            mb.showerror("Error", "Seleccione un evento para eliminar")
            return
        id_evento = self.treeview2.item(ItemSeleccionado1, "values")[0]

        # Eliminar el evento de la lista
        for evento in self.eventos:
            if evento.RegistoEvento["IdEvento"] == id_evento:
                self.eventos.remove(evento)
                break

        # Eliminar el evento de la Treeview
        self.treeview2.delete(ItemSeleccionado1)
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

        #Obtener el indie numerico de la fila
        indice_evento = int(self.treeview2.index(ItemSeleccionado1))
        evento_seleccionado = self.eventos[indice_evento]

        evento_seleccionado.id_evento = nuevo_id_evento
        evento_seleccionado.nombre_evento =nuevo_nombre_evento
        evento_seleccionado.cantidad_evento = nueva_cantidad_evento
        evento_seleccionado.productoxcantidad = nuevo_productoxcantidad
        evento_seleccionado.fecha_evento = nueva_fecha_evento
        evento_seleccionado.hora_evento  = nueva_hora_evento
        evento_seleccionado.id_cliente_foreign =nuevo_id_cliente_foreign

        #Actualizar la visualizacion en el treview2
        self.treeview2.item(ItemSeleccionado1,values=(nuevo_id_evento,nuevo_nombre_evento,nueva_cantidad_evento,nuevo_productoxcantidad,
                                                      nueva_fecha_evento,nueva_hora_evento,nuevo_id_cliente_foreign))
        mb.showinfo("Actualizacion exitosa","Los campos de evento se han modificado correctamente")

    def AgregarProducto(self):
        num_serie = self.gestorproducto.grid_slaves(row=2,column=0)[0].get()
        tipo_producto = self.gestorproducto.grid_slaves(row=4,column=0)[0].get()
        valor_neto = self.gestorproducto.grid_slaves(row=6,column=0)[0].get()
        id_evento_foreign = self.gestorproducto.grid_slaves(row=8,column=0)[0].get()
        id_cliente_foreign = self.gestorproducto.grid_slaves(row=10,column=0)[0].get()

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



        nuevo_producto = Producto()
        nuevo_producto.RegistroProducto["NumSerie"] = num_serie
        nuevo_producto.RegistroProducto["TipoProducto"] = tipo_producto
        nuevo_producto.RegistroProducto["ValorNeto"] = valor_neto
        nuevo_producto.RegistroProducto["IdEventoForeign"]=id_evento_foreign
        nuevo_producto.RegistroProducto["IdClienteForeign"]=id_cliente_foreign

        self.productos.append(nuevo_producto)

        Producto.TotalValorNeto+=valor_neto

        #Actualizar la lista, el trieview
        self.treeview3.insert("","end",values=(
            nuevo_producto.RegistroProducto["NumSerie"],
            nuevo_producto.RegistroProducto["TipoProducto"],
            nuevo_producto.RegistroProducto["ValorNeto"],
            nuevo_producto.RegistroProducto["IdEventoForeign"],
            nuevo_producto.RegistroProducto["IdClienteForeign"]
        ))
        self.ActualizarTotal()

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
        indice_producto = int(self.treeview3.index(ItemSeleccionado3))
        producto_seleccionado = self.productos[indice_producto]
        producto_seleccionado.num_serie =nuevo_num_serie
        producto_seleccionado.tipo_producto = nuevo_tipo_producto
        producto_seleccionado.valor_neto = nuevo_valor_neto
        producto_seleccionado.id_evento_foreign = nuevo_evento_foreign2
        producto_seleccionado.id_cliente_foreign = nuevo_id_cliente_foreign2

        #Actualizar la vista en el trewview3
        self.treeview3.item(ItemSeleccionado3,values=(
            nuevo_num_serie,
            nuevo_tipo_producto,
            nuevo_valor_neto,
            nuevo_evento_foreign2,
            nuevo_id_cliente_foreign2
        ))
        mb.showinfo("Actualizacion Exitosa","Los campos de producto se han modificado correctamente")
    def EliminarProducto(self):
        ItemSeleccionado3 = self.treeview3.selection()
        if not ItemSeleccionado3:
            mb.showerror("Error","Selecciones un producto para eliminar")
        num_serie = self.treeview3.item(ItemSeleccionado3,"values")[0]

        #Eliminar el producto de la lista
        for x in self.productos:
            if x.RegistroProducto["NumSerie"] ==num_serie:
                self.productos.remove(x)
                break
        #Eliminar el producto de la trewview3
        self.treeview3.delete(ItemSeleccionado3)
    def BuscarProducto(self):
        self.treeview3.delete(*self.treeview3.get_children())
        valor3 = self.BusquedaProducto.get()
        #Si la busqueda esta vacia, mostrar todos los productos
        if not valor3:
            for x in self.productos:
                self.treeview3.insert("","end",values=(
                    x.RegistroProducto["NumSerie"],
                    x.RegistroProducto["TipoProducto"],
                    x.RegistroProducto["ValorNeto"],
                    x.RegistroProducto["IdEventoForeign"],
                    x.RegistroProducto["IdClienteForeign"]
                ))
        else:
            self.treeview3.delete(*self.treeview3.get_children())
            for x in self.productos:
                if valor3 == x.RegistroProducto["NumSerie"]:
                    self.treeview3.insert("","end",values=(
                    x.RegistroProducto["NumSerie"],
                    x.RegistroProducto["TipoProducto"],
                    x.RegistroProducto["ValorNeto"],
                    x.RegistroProducto["IdEventoForeign"],
                    x.RegistroProducto["IdClienteForeign"]
                    ))

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
#Clases Principales
class Cliente:
    NumClientes = 0
    def __init__(self):
        self.RegistroCliente = {"IdCliente":"","NombreCompleto":"","RunCliente": "","EmpresaCliente":"","ComunaCliente":"","NumeroCliente":"","EmailCliente":"","MetodoPago":""}
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