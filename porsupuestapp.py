""" Generador de Presupuestos """
#import os
from tkinter import *
#from tkinter.ttk import *

# Gama de colores
color_primario = "#373737"
color_claro = "#f8f8f8"
color_secundario = "#1183b8"
color_terciario = "#f48d24"
gris_claro = "#ecedec"

# Funciones de los Conceptos
## Activa los campos Entry con cada Checkbox de los conceptos
def activar_textos(cont):
    if concepto_opciones[cont].get() == 1:
        concepto_contador_ent_1[cont].config(state=NORMAL)
        concepto_contador_ent_2[cont].config(state=NORMAL)
        concepto_contador_ent_3[cont].configure(disabledbackground=color_claro, disabledforeground=color_primario)
    else:
        concepto_contador_ent_1[cont].delete(0,END)
        concepto_contador_ent_1[cont].config(state=DISABLED)
        entry2_vars[cont].set("")
        concepto_contador_ent_2[cont].config(state=DISABLED)
        entry3_vars[cont].set(0.00)
        concepto_contador_ent_3[cont].configure(disabledbackground=gris_claro, disabledforeground=color_primario)

## Activa Entrys de los campos impuestos
def activa_impostos(imp):
    if imp.lower() == 'iva':
        if iva_var_cb.get() == 1:
            iva_ent.configure(state=NORMAL)
            iva_total_ent.config(disabledbackground=color_claro, disabledforeground=color_primario)
        else:
            iva_ent.delete(0,END)
            iva_ent.configure(state=DISABLED)
            iva_total_ent.configure(state=NORMAL)
            iva_total_ent.delete(0,END)
            iva_total_ent.configure(state=DISABLED)
            iva_total_ent.config(disabledbackground=gris_claro, disabledforeground=color_primario)
    elif imp.lower() == 'irpf':
        if irpf_var_cb.get() == 1:
            irpf_ent.configure(state=NORMAL)
            irpf_total_ent.config(disabledbackground=color_claro, disabledforeground=color_primario)
        else:
            irpf_ent.delete(0,END)
            irpf_ent.configure(state=DISABLED)
            irpf_total_ent.config(state=NORMAL)
            irpf_total_ent.delete(0,END)
            irpf_total_ent.config(state=DISABLED)
            irpf_total_ent.config(disabledbackground=gris_claro, disabledforeground=color_primario)

## Calcula el producto de cada concepto (Precio base * nº h)
def update_entry3(var,cont):
    if var.get().replace('.', '').isnumeric() and concepto_contador_ent_1[cont].get().replace('.', '').isnumeric():
        entry3_vars[cont].set(round(float(concepto_contador_ent_1[cont].get())*float(var.get()),2))
    else:
        entry3_vars[cont].set(0.00)

## IVA e IRPF 
def update_impost(var,tipus):
    if tipus.lower() == "iva":
        if var.get().isnumeric():
            if (subtotal_ent.get().replace('.', '').isnumeric()):
                iva_total_ent.config(state=NORMAL)
                iva_total_ent.delete(0,END)
                iva_total_var.set(round(float(subtotal_ent.get())*int(var.get())/100,2))
                iva_total_ent.config(state=DISABLED)
    elif tipus.lower() == "irpf":
        if var.get().isnumeric():
            if (subtotal_ent.get().replace('.', '').isnumeric()):
                irpf_total_ent.config(state=NORMAL)
                irpf_total_ent.delete(0,END)
                irpf_total_var.set(round(float(subtotal_ent.get())*int(var.get())/100,2))
                irpf_total_ent.config(state=DISABLED)

## Subtotal, suma de productos de cada concepto
def update_subtotal():
    subtotal_var.set(0.00)
    suma = subtotal_var.get()
    for entry_var in entry3_vars:
        print(entry_var.get())
        suma += entry_var.get()
    subtotal_var.set(round(suma,2))

## Total, suma de Subtotal e IVA y resta de IRPF
def update_total():
    total_var.set(0.00)
    suma = subtotal_var.get()
    suma += iva_total_var.get()
    suma -= irpf_total_var.get()
    total_var.set(round(suma,2))


# Funciones de los Botones
## Traspasa los Totales de los conceptos e impuestos y totales
def calc_pressupost():
    pass

## Genera una factura en PDF
def fer_factura():
    pass

## Registra las facturas generadas por número de recibo (Opción a eliminar y actualizar número de recibo)
def historial():
    pass

## Envía las facturas por email
def send_mail():
    pass


# Abrir programa
main = Tk()

# Ventana Principal
main.title("PORSUPUESTAPP")
main.config(bg=color_primario) #Color del fondo de la ventana
main.resizable(1,1)
main.minsize(625, 675)

# Frames 
top_frame = Frame(main,bd=10,relief=FLAT, bg=color_claro)
left_frame = Frame(main,bd=10,relief=FLAT, bg=color_claro)
right_frame = Frame(main,bd=10,relief=FLAT, bg=color_claro)
bottom_frame = Frame(main,bd=10,relief=FLAT, bg=color_claro)

top_frame.pack(side=TOP, fill="both", expand=True, padx=20, pady=20)
top_frame.place(in_=main, anchor="c", relx=.5, rely=.5)
left_frame.pack(side=LEFT)
right_frame.pack(side=RIGHT)
bottom_frame.pack(side=BOTTOM)

# Labels
concepto_frame = Frame(top_frame,bd=0,relief=FLAT, bg=color_claro)
concepto_frame_lbl = LabelFrame(concepto_frame,font=("Helvetica",18),text="Conceptos",fg=color_primario, bg=color_claro)
botones_frame = Frame(top_frame,bd=0,relief=FLAT, bg=color_claro)
botones_frame_lbl = LabelFrame(botones_frame,font=("Helvetica",18),text="Opciones",fg=color_primario, bg=color_claro)

concepto_frame.grid(row=0,column=0)
concepto_frame_lbl.pack(side=TOP)
botones_frame.grid(row=1,column=0)
botones_frame_lbl.pack(side=TOP)

# Listas de conceptos y opciones
concepto_list = ["Trabajo", "Extra", "Equipo", "Material", "Transporte"]

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
    cajas_texto = Checkbutton(concepto_frame_lbl, text=concepto, bd=2, bg=color_claro, fg=color_primario, font=("Helvetica",18), relief=FLAT, variable=concepto_opciones[contador], command=lambda cont=contador:activar_textos(cont))
    cajas_texto.grid(row=contador,column=0,sticky=W, padx=30, pady=5)

    # Columna Entry 1
    concepto_contador_ent_1.append(Entry(concepto_frame_lbl, font=("Helvetica",18), relief=FLAT, justify=CENTER, bd=2, width=7, state=DISABLED, fg=color_primario, bg=color_claro))
    concepto_contador_ent_1[contador].grid(row=contador,column=1,sticky=W)
    
    # Variable entry 2
    entry2_var = StringVar()
    entry2_var.trace("w", lambda name,index,mode,var=entry2_var,cont=contador:update_entry3(var,cont))
    entry2_vars.append(entry2_var)
    # Segunda columna
    concepto_contador_ent_2.append(Entry(concepto_frame_lbl, font=("Helvetica",18), relief=FLAT, justify=CENTER, bd=2, width=7, state=DISABLED, fg=color_primario, bg=color_claro, textvariable=entry2_vars[contador]))
    concepto_contador_ent_2[contador].grid(row=contador,column=2,sticky=W)
    
    # Variable entry 3
    entry3_var = DoubleVar()
    entry3_var.trace('w',lambda name,index,mode,var=entry3_var,:update_subtotal())
    entry3_vars.append(entry3_var)
    # Tercera columna
    concepto_contador_ent_3.append(Entry(concepto_frame_lbl, font=("Helvetica",18), relief=FLAT, justify=CENTER, bd=2, width=7, state=DISABLED, fg=color_primario, bg=color_claro,textvariable=entry3_vars[contador]))
    concepto_contador_ent_3[contador].grid(row=contador,column=3,sticky=W)
    contador += 1

# Calcular Impuestos
## IVA
iva_var_cb = IntVar()
iva_var_ent = StringVar()
iva_var_ent.trace('w',lambda name,index,mode,var=iva_var_ent,tipus="IVA":update_impost(var,tipus))
iva_total_var = DoubleVar()
iva_total_var.trace('w',lambda name,index,mode:update_total())

iva_cb = Checkbutton(concepto_frame_lbl, text="IVA", bd=1, bg=color_claro, fg=color_primario, font=("Helvetica",18), relief=FLAT, variable=iva_var_cb, command=lambda:activa_impostos('IVA'))
iva_ent = Entry(concepto_frame_lbl, font=("Helvetica",18), relief=FLAT, justify=CENTER, bd=2, width=7, state=DISABLED, fg=color_primario, bg=color_claro, textvariable=iva_var_ent)
iva_total_ent = Entry(concepto_frame_lbl, font=("Helvetica",18), relief=FLAT, justify=CENTER, bd=2, width=7, state=DISABLED, fg=color_primario, bg=color_claro,textvariable=iva_total_var)

## IRPF
irpf_var_cb = IntVar()
irpf_var_ent = StringVar()
irpf_var_ent.trace('w',lambda name,index,mode,var=irpf_var_ent,tipus="IRPF":update_impost(var,tipus))
irpf_total_var = DoubleVar()
irpf_total_var.trace('w',lambda name,index,mode:update_total())

irpf_cb = Checkbutton(concepto_frame_lbl, text="IRPF", bd=2, bg=color_claro, fg=color_primario, font=("Helvetica",18), relief=FLAT, variable=irpf_var_cb, command=lambda:activa_impostos('IRPF'))
irpf_ent = Entry(concepto_frame_lbl, font=("Helvetica",18), relief=FLAT, justify=CENTER, bd=2, width=7, state=DISABLED, fg=color_primario, bg=color_claro, textvariable=irpf_var_ent)
irpf_total_ent = Entry(concepto_frame_lbl, font=("Helvetica",18), relief=FLAT, justify=CENTER, bd=2, width=7, state=DISABLED, fg=color_primario, bg=color_claro,textvariable=irpf_total_var)

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
subtotal_lbl = Label(concepto_frame_lbl, text="Subtotal", bd=2, bg=color_claro, fg=color_primario, font=("Helvetica",18))
subtotal_ent = Entry(concepto_frame_lbl, font=("Helvetica",18), relief=FLAT, justify=CENTER,state=DISABLED, bd=2, width=23, fg=color_primario, bg=color_claro,textvariable=subtotal_var)

## Total
total_var = DoubleVar(value=0.00)
total_lbl = Label(concepto_frame_lbl, text="Total", bd=2, bg=color_claro, fg=color_primario, font=("Helvetica",18))
total_ent = Entry(concepto_frame_lbl, font=("Helvetica",18), relief=FLAT, justify=CENTER,state=DISABLED, bd=2, width=23, fg=color_primario, bg=color_claro,textvariable=total_var)

subtotal_lbl.grid(row=5, column=0)
subtotal_ent.grid(row=5, column=1,columnspan=3)
total_lbl.grid(row=8, column=0)
total_ent.grid(row=8, column=1,columnspan=3)


#Botones de funciones
pres_btn = Button(botones_frame_lbl, text="Calcular Presupuesto", font=("Helvetica",18), bd=1, padx=5, pady=5, width=36, relief=FLAT, bg=color_claro, fg=color_primario,command=calc_pressupost)
fact_btn = Button(botones_frame_lbl, text="Generar Factura", font=("Helvetica",18), bd=1, padx=5, pady=5, width=36, relief=FLAT, bg=color_claro, fg=color_primario,command=fer_factura)
reg_btn = Button(botones_frame_lbl, text="Registro Histórico", font=("Helvetica",18), bd=1, padx=5, pady=5, width=36, relief=FLAT, bg=color_claro, fg=color_primario,command=historial)
mail_btn = Button(botones_frame_lbl, text="Enviar email", font=("Helvetica",18), bd=1, padx=5, pady=5, width=36, relief=FLAT, bg=color_claro, fg=color_primario,command=send_mail)

pres_btn.grid(row=0)
fact_btn.grid(row=1)
reg_btn.grid(row=2)
mail_btn.grid(row=3)

main.mainloop()