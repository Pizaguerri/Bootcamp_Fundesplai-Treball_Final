""" Generador de Presupuestos """
#import os
from tkinter import *
from tkinter import ttk
import csv
from PIL import Image, ImageTk
#import popup_datos_profesional
#import popup_datos_cliente
from generarpdf import generar_factura

# Estilos
COLOR_OSCURO = "#373737"
COLOR_CLARO = "#f8f8f8"
COLOR_AZUL = "#1183b8"
COLOR_NARANJA = "#f48d24"
COLOR_GRIS_CLARO = "#ecedec"

dict_totals = {"Trabajo" : 0, "Horas" : 0, "Material" : 0, "Transporte" : 0, "Extra" : 0}
dict_tax = {"IVA" : 0, "IRPF": 0}
dict_unidades = {"Trabajo" : 0, "Horas" : 0, "Material" : 0, "Transporte" : 0, "Extra" : 0}
dict_precio = {"Trabajo" : 0, "Horas" : 0, "Material" : 0, "Transporte" : 0, "Extra" : 0}

dict_datos_profesional = {}
with open("datos_profesional.csv", "r", encoding="utf-8") as datos_profesional:
        dato = csv.DictReader(datos_profesional)
        for diccionario_en_fila in dato:
                dict_datos_profesional = diccionario_en_fila
        #print(dict_datos_profesional)

## Abre CSV Cliente y lee los datos guardados por defecto
dict_datos_cliente = {}
with open("datos_cliente.csv", "r", encoding="utf-8") as datos_cliente:
        dato = csv.DictReader(datos_cliente)
        for diccionario_en_fila in dato:
                dict_datos_cliente = diccionario_en_fila
        #print(dict_datos_cliente)



# Recoge datos de HTML para el PDF

## Profesional
# logo = "icono_camara.png"
nom_empresa_profesional = dict_datos_profesional['Profesional']
direccion_profesional = dict_datos_profesional['Direccion']
zip_profesional = dict_datos_profesional['CP']
telefono_profesional = dict_datos_profesional['Telefono']
email_profesional = dict_datos_profesional['Email']
portfolio_profesional = dict_datos_profesional['Portfolio']
cif_profesional = dict_datos_profesional['CIF']

## Cliente
nom_empresa_cliente = dict_datos_cliente['Cliente']
direccion_cliente = dict_datos_cliente['Direccion']
zip_cliente = dict_datos_cliente['CP']
telefono_cliente = dict_datos_cliente['Telefono']
email_cliente = dict_datos_cliente['Email']
cif_cliente = dict_datos_cliente['CIF']

# Funciones de los Conceptos
## Activa los campos Entry con cada Checkbox de los conceptos
def activar_textos(cont):
    if concepto_opciones[cont].get() == 1:
        concepto_contador_ent_1[cont].config(state=NORMAL)
        concepto_contador_ent_2[cont].config(state=NORMAL)
        concepto_contador_ent_3[cont].configure(disabledbackground=COLOR_CLARO, disabledforeground=COLOR_OSCURO)
    else:
        concepto_contador_ent_1[cont].delete(0,END)
        concepto_contador_ent_1[cont].config(state=DISABLED)
        entry2_vars[cont].set("")
        concepto_contador_ent_2[cont].config(state=DISABLED)
        entry3_vars[cont].set(0.00)
        concepto_contador_ent_3[cont].configure(disabledbackground=COLOR_GRIS_CLARO, disabledforeground=COLOR_OSCURO)

## Activa Entrys de los campos impuestos
def activa_impostos(imp):
    if imp.lower() == 'iva':
        if iva_var_cb.get() == 1:
            iva_ent.configure(state=NORMAL)
            iva_total_ent.config(disabledbackground=COLOR_CLARO, disabledforeground=COLOR_OSCURO)
        else:
            iva_ent.delete(0,END)
            iva_ent.configure(state=DISABLED)
            iva_total_ent.configure(state=NORMAL)
            iva_total_ent.delete(0,END)
            iva_total_ent.configure(state=DISABLED)
            iva_total_ent.config(disabledbackground=COLOR_GRIS_CLARO, disabledforeground=COLOR_OSCURO)
    elif imp.lower() == 'irpf':
        if irpf_var_cb.get() == 1:
            irpf_ent.configure(state=NORMAL)
            irpf_total_ent.config(disabledbackground=COLOR_CLARO, disabledforeground=COLOR_OSCURO)
        else:
            irpf_ent.delete(0,END)
            irpf_ent.configure(state=DISABLED)
            irpf_total_ent.config(state=NORMAL)
            irpf_total_ent.delete(0,END)
            irpf_total_ent.config(state=DISABLED)
            irpf_total_ent.config(disabledbackground=COLOR_GRIS_CLARO, disabledforeground=COLOR_OSCURO)

## Calcula el producto de cada concepto (Precio base * nº h)
def update_entry3(var,cont,dict_precio, dict_unidades, concepto):
    if var.get().replace('.', '').isnumeric() and concepto_contador_ent_1[cont].get().replace('.', '').isnumeric():
        # print("Soc update_entry_3", concepto_list[cont])
        entry3_vars[cont].set(round(float(concepto_contador_ent_1[cont].get())*float(var.get()),2))  


        # print("concept --> ", concepto)
        # print("68 --> ", round(float(var.get()),2)) 
        dict_precio[concepto_list[cont]]= round(float(var.get()),2)
        dict_unidades[concepto_list[cont]] = round(float(concepto_contador_ent_1[cont].get()),2)
    else:
        entry3_vars[cont].set(0.00)
    # print("linia 75", dict_unidades)
    # print("linia 76", dict_precio)
    


def actualitza_dicc_preus_unitats(var,cont,dict_precio, dict_unidades, concepto):
    
    if var.get().replace('.', '').isnumeric() and concepto_contador_ent_1[cont].get().replace('.', '').isnumeric():
        # print("74 --> " , concepto)
        dict_precio[concepto]= round(float(var.get()),2)
        dict_unidades[concepto] = round(float(concepto_contador_ent_1[cont].get()),2)
    # print("linia 75", dict_unidades)
    # print("linia 76", dict_precio)

## Recoge valores de entry total de cada concepto para crear un dict_totals
def recoger_totals(var,cont):
    if var.get().replace('.', '').isnumeric() and concepto_contador_ent_1[cont].get().replace('.', '').isnumeric():
        return (round(float(concepto_contador_ent_1[cont].get())*float(var.get()),2))
    else:
        return


## IVA e IRPF 
def update_impost(var,tipus, diccionari):
    if tipus.lower() == "iva":
        if var.get().isnumeric():
            if (subtotal_ent.get().replace('.', '').isnumeric()):
                iva_total_ent.config(state=NORMAL)
                iva_total_ent.delete(0,END)
                diccionari['IVA'] = int(var.get())
                iva_total_var.set(round(float(subtotal_ent.get())*int(var.get())/100,2))
                iva_total_ent.config(state=DISABLED)
    elif tipus.lower() == "irpf":
        if var.get().isnumeric():
            if (subtotal_ent.get().replace('.', '').isnumeric()):
                irpf_total_ent.config(state=NORMAL)
                irpf_total_ent.delete(0,END)
                diccionari['IRPF'] = int(var.get())
                irpf_total_var.set(round(float(subtotal_ent.get())*int(var.get())/100,2))
                irpf_total_ent.config(state=DISABLED)
    # print("diccionari taxes", diccionari)


## Subtotal, suma de productos de cada concepto
def update_subtotal(diccionario, lista):
    subtotal_var.set(0.00)
    suma = subtotal_var.get()
    contador = 0   
    for entry_var in entry3_vars:
        diccionario[lista[contador]] = entry_var.get()
        print(entry_var.get())
        suma += entry_var.get()
        contador += 1
    subtotal_var.set(round(suma,2))
    #print(diccionario)

## Total, suma de Subtotal e IVA y resta de IRPF
def update_total():
    # print("update_total -->")
    # print(type(subtotal_var.get()),type(iva_total_var.get()),type(irpf_total_var.get()))

    total_var.set(0.00)
    suma = subtotal_var.get()
    suma += iva_total_var.get()
    suma -= irpf_total_var.get()
    total_var.set(round(suma,2))


# Funciones de los Botones
## Genera una factura en PDF 
# # (Import generarpdf.py)
# def generar_factura(dict_totals):
#     crear_pdf(dict_totals)


## Registra las facturas generadas por número de recibo (Opción a eliminar y actualizar número de recibo) 
# # # (??????)
# def historial():
#     pass

# ## Envía las facturas por email
# def enviar_mail():
#     pass


# # Crea la función que se ejecutará al hacer clic en el botón de "Más"
# def agregar_campo():
#     cuadros_de_texto = [Entry(top_frame) for i in range(3)]
#     concepto_list.extend(agregar_campo)
#     for cuadro_de_texto in cuadros_de_texto:
#         cuadro_de_texto.pack()
#     for i, cuadro_de_texto in enumerate(cuadros_de_texto):
#         add_entry = app.Label(concepto_frame_lbl, text="Campo {}:".format(i+1))
#         add_entry.pack(concepto_frame_lbl, font=("Helvetica",18), relief=FLAT, justify=CENTER, bd=2, width=7, fg=COLOR_OSCURO, bg=COLOR_CLARO)
#         add_entry.place(x=cuadro_de_texto.winfo_x()-add_entry.winfo_width()-10, y=cuadro_de_texto.winfo_y())
#         # cajas_texto = Checkbutton(concepto_frame_lbl, text=concepto, bd=2, bg=COLOR_CLARO, fg=COLOR_OSCURO, font=("Helvetica",18), relief=FLAT, variable=concepto_opciones[contador], command=lambda cont=contador:activar_textos(cont))
#         # cajas_texto.grid(row=contador,column=0,sticky=W, padx=30, pady=5)

# def agregar_concepto():
#     nuevo_concepto = input("Introduce el nuevo elemento: ")
    
#     concepto_list.append(nuevo_concepto)


# Abrir programa
app = Tk()

# Ventana Principal
app.title("PORSUPUESTAPP")
app.config(bg=COLOR_OSCURO) #Color del fondo de la ventana
app.resizable(1,1)
app.minsize(625, 675)

# Icono de la app
icon = "/Users/pabloizaguerri/Documents/Python_2023/Treball Final/"
load = Image.open("icon6.png")
render = ImageTk.PhotoImage(load)
app.iconphoto(False, render)
print("El profesional es", dict_datos_profesional['Profesional'])
print("El cliente es", dict_datos_cliente['Cliente'])
# Tabs
paginas = ttk.Notebook(app)
s = ttk.Style(paginas)
s.configure('TFrame', background=COLOR_OSCURO)
tab1 = ttk.Frame(paginas, style='TFrame') ############################No cambia el color del frame al Color Oscuro
tab2 = ttk.Frame(paginas)
tab3 = ttk.Frame(paginas)
tab4 = ttk.Frame(paginas)
paginas.add(tab1, text ='Calculadora')
paginas.add(tab2, text ='Historial')
paginas.add(tab3, text ='Datos del Profesional')
paginas.add(tab4, text ='Datos del Cliente')
#paginas.add(tab3, popup_datos_profesional.py.main(), text ='Datos del Profesional')
paginas.pack(expand = 1, fill ="both")


# Frames 
top_frame = Frame(app,bd=10,relief=FLAT, bg=COLOR_CLARO)
left_frame = Frame(app,bd=10,relief=FLAT, bg=COLOR_CLARO)
right_frame = Frame(app,bd=10,relief=FLAT, bg=COLOR_CLARO)
bottom_frame = Frame(app,bd=10,relief=FLAT, bg=COLOR_CLARO)

top_frame.pack(side=TOP, fill="both", expand=True, padx=20, pady=20)
top_frame.place(in_=app, anchor="c", relx=.5, rely=.5)
left_frame.pack(side=LEFT)
right_frame.pack(side=RIGHT)
bottom_frame.pack(side=BOTTOM)

# Labels
concepto_frame = Frame(top_frame,bd=0,relief=FLAT, bg=COLOR_CLARO)
concepto_frame_lbl = LabelFrame(concepto_frame,font=("Helvetica",18),text="Conceptos",fg=COLOR_OSCURO, bg=COLOR_CLARO)
botones_frame = Frame(top_frame,bd=0,relief=FLAT, bg=COLOR_CLARO)
botones_frame_lbl = LabelFrame(botones_frame,font=("Helvetica",18),text="Opciones",fg=COLOR_OSCURO, bg=COLOR_CLARO)

concepto_frame.grid(row=0,column=0)
concepto_frame_lbl.pack(side=TOP)
botones_frame.grid(row=1,column=0)
botones_frame_lbl.pack(side=TOP)



# Listas de conceptos y opciones
concepto_list = ["Trabajo", "Horas", "Material", "Transporte", "Extra"]

# Checkbuttons de los conceptos con caja de entrada de valores
# Entrys por columnas 
concepto_opciones = list()
concepto_contador_ent_1 = list()
concepto_contador_ent_2 = list()
concepto_contador_ent_3 = list()
entry2_vars = list()
entry3_vars = list()



contador = 0
for concepto in concepto_list:
    concepto_opciones.append(IntVar())
    cajas_texto = Checkbutton(concepto_frame_lbl, text=concepto, bd=2, bg=COLOR_CLARO, fg=COLOR_OSCURO, font=("Helvetica",18), relief=FLAT, variable=concepto_opciones[contador], command=lambda cont=contador:activar_textos(cont))
    cajas_texto.grid(row=contador,column=0,sticky=W, padx=30, pady=5)

    # Columna Entry 1
    concepto_contador_ent_1.append(Entry(concepto_frame_lbl, font=("Helvetica",18), relief=FLAT, justify=CENTER, bd=2, width=8, state=DISABLED, fg=COLOR_OSCURO, bg=COLOR_CLARO))
    concepto_contador_ent_1[contador].grid(row=contador,column=1,sticky=W)
    
    # Variable entry 2
    entry2_var = StringVar()
    #print("linia 247 --> ", concepto)
    # actualitza_dicc_preus_unitats(entry2_var,contador,dict_precio, dict_unidades, concepto)
    entry2_var.trace("w", lambda name,index,mode,var=entry2_var,cont=contador:update_entry3(var,cont,dict_precio, dict_unidades, concepto))
    #total = (lambda name,index,mode,var=entry2_var,cont=contador:update_entry3(var,cont))
    entry2_vars.append(entry2_var)
    # print("entry2_vars", entry2_vars)
    # Segunda columna
    concepto_contador_ent_2.append(Entry(concepto_frame_lbl, font=("Helvetica",18), relief=FLAT, justify=CENTER, bd=2, width=8, state=DISABLED, fg=COLOR_OSCURO, bg=COLOR_CLARO, textvariable=entry2_vars[contador]))
    concepto_contador_ent_2[contador].grid(row=contador,column=2,sticky=W)
    
    # Variable entry 3
    entry3_var = DoubleVar()
    entry3_var.trace('w',lambda name,index,mode,var=entry3_var,:update_subtotal(dict_totals, concepto_list))
    entry3_vars.append(entry3_var)
    # Tercera columna
    concepto_contador_ent_3.append(Entry(concepto_frame_lbl, font=("Helvetica",18), relief=FLAT, justify=CENTER, bd=2, width=8, state=DISABLED, fg=COLOR_OSCURO, bg=COLOR_CLARO,textvariable=entry3_vars[contador]))
    concepto_contador_ent_3[contador].grid(row=contador,column=3,sticky=W)
    contador += 1

    #dict_totals[concepto] = total #Rellena diccionario con conceptos

#print(dict_totals)
# Conceptos dinámicos


# Calcular Impuestos
## IVA
iva_var_cb = IntVar()
iva_var_ent = StringVar()
iva_var_ent.trace('w',lambda name,index,mode,var=iva_var_ent,tipus="IVA":update_impost(var,tipus, dict_tax))
iva_total_var = DoubleVar()
iva_total_var.trace('w',lambda name,index,mode:update_total())

iva_cb = Checkbutton(concepto_frame_lbl, text="IVA", bd=2, bg=COLOR_CLARO, fg=COLOR_OSCURO, font=("Helvetica",18), relief=FLAT, variable=iva_var_cb, command=lambda:activa_impostos('IVA'))
iva_ent = Entry(concepto_frame_lbl, font=("Helvetica",18), relief=FLAT, justify=CENTER, bd=2, width=18, state=DISABLED, fg=COLOR_OSCURO, bg=COLOR_CLARO, textvariable=iva_var_ent)
iva_total_ent = Entry(concepto_frame_lbl, font=("Helvetica",18), relief=FLAT, justify=CENTER, bd=2, width=8, state=DISABLED, fg=COLOR_OSCURO, bg=COLOR_CLARO,textvariable=iva_total_var)

## IRPF
irpf_var_cb = IntVar()
irpf_var_ent = StringVar()
irpf_var_ent.trace('w',lambda name,index,mode,var=irpf_var_ent,tipus="IRPF":update_impost(var,tipus, dict_tax))
irpf_total_var = DoubleVar()
irpf_total_var.trace('w',lambda name,index,mode:update_total())

irpf_cb = Checkbutton(concepto_frame_lbl, text="IRPF", bd=2, bg=COLOR_CLARO, fg=COLOR_OSCURO, font=("Helvetica",18), relief=FLAT, variable=irpf_var_cb, command=lambda:activa_impostos('IRPF'))
irpf_ent = Entry(concepto_frame_lbl, font=("Helvetica",18), relief=FLAT, justify=CENTER, bd=2, width=18, state=DISABLED, fg=COLOR_OSCURO, bg=COLOR_CLARO, textvariable=irpf_var_ent)
irpf_total_ent = Entry(concepto_frame_lbl, font=("Helvetica",18), relief=FLAT, justify=CENTER, bd=2, width=8, state=DISABLED, fg=COLOR_OSCURO, bg=COLOR_CLARO,textvariable=irpf_total_var)

iva_cb.grid(row=6,column=0)
iva_ent.grid(row=6,column=1,columnspan=2)
iva_total_ent.grid(row=6,column=3)
irpf_cb.grid(row=7,column=0)
irpf_ent.grid(row=7,column=1,columnspan=2)
irpf_total_ent.grid(row=7,column=3)

# Calcular Subtotal y Total
## Subtotal
subtotal_var = DoubleVar(value=0.00)
subtotal_var.trace('w',lambda name,index,mode:update_total())
subtotal_lbl = Label(concepto_frame_lbl, text="Subtotal", bd=2, bg=COLOR_CLARO, fg=COLOR_OSCURO, font=("Helvetica",18))
subtotal_ent = Entry(concepto_frame_lbl, font=("Helvetica",18), relief=FLAT, justify=CENTER,state=DISABLED, bd=2, width=27, fg=COLOR_OSCURO, bg=COLOR_CLARO,textvariable=subtotal_var)

## Total
total_var = DoubleVar(value=0.00)
total_lbl = Label(concepto_frame_lbl, text="Total", bd=2, bg=COLOR_CLARO, fg=COLOR_OSCURO, font=("Helvetica",18))
total_ent = Entry(concepto_frame_lbl, font=("Helvetica",18), relief=FLAT, justify=CENTER,state=DISABLED, bd=2, width=27, fg=COLOR_OSCURO, bg=COLOR_CLARO,textvariable=total_var)

subtotal_lbl.grid(row=5, column=0)
subtotal_ent.grid(row=5, column=1,columnspan=3)
total_lbl.grid(row=8, column=0)
total_ent.grid(row=8, column=1,columnspan=3)

# Agregar Más
# boton_mas = Button(concepto_frame, text="Agregar Conceptos", font=("Helvetica",14), bd=0, padx=5, pady=5, relief=FLAT, bg=COLOR_GRIS_CLARO, fg=COLOR_OSCURO, command=lambda: agregar_concepto())
# boton_mas.grid(row=9, column=0)
# boton_mas.pack(side="bottom", anchor="center", padx=2, pady=10)

# print("337 -->", dict_totals)
# # print(dict_tax)
# print("=" * 50)
# print("\n")
# print("Preu", dict_precio)
# print("Unitats", dict_unidades)
# print("\n")
# print("=" * 50)

# Botones de funciones
#pres_btn = Button(botones_frame_lbl, text="Calcular Presupuesto", font=("Helvetica",18), bd=0, padx=5, pady=5, width=40, relief=FLAT, bg=COLOR_GRIS_CLARO, fg=COLOR_OSCURO,command=calc_pressupost)
fact_btn = Button(botones_frame_lbl, text="Generar Factura", font=("Helvetica",18), bd=0, padx=5, pady=5, width=40, relief=FLAT, bg=COLOR_GRIS_CLARO, fg=COLOR_OSCURO,command=lambda:generar_factura(dict_totals, dict_tax, dict_precio, dict_unidades))
# reg_btn = Button(botones_frame_lbl, text="Registro Histórico", font=("Helvetica",18), bd=0, padx=5, pady=5, width=40, relief=FLAT, bg=COLOR_GRIS_CLARO, fg=COLOR_OSCURO,command=historial)
#mail_btn = Button(botones_frame_lbl, text="Enviar email", font=("Helvetica",18), bd=0, padx=5, pady=5, width=40, relief=FLAT, bg=COLOR_GRIS_CLARO, fg=COLOR_OSCURO,command=enviar_mail)

#pres_btn.grid(row=0)
fact_btn.grid(row=1)
# reg_btn.grid(row=2)
#mail_btn.grid(row=2)

app.mainloop()