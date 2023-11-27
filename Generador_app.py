""" Generador """

import os
from tkinter import *
import tkinter.messagebox as mb

main = Tk()

color_primario = "#373737"
color_claro = "#f8f8f8"
color_secundario = "#1183b8"
color_terciario = "#f48d24"


#Precio Base o unitario por defecto (pb)
def activar_pb(list_n):
    pb_lists = [pb_opciones]
    contador_pb_lists = [pb_contador]

    for contador_pb in range(0,len(pb_lists[list_n])):

        if pb_lists[list_n][contador_pb].get() == 1:
            contador_pb_lists[list_n][contador_pb].configure(state=NORMAL)
        else:
            contador_pb_lists[list_n][contador_pb].configure(state=DISABLED)


#Valor horas trabajadas (h)
def activar_h(list_n):
    h_lists = [h_opciones]
    contador_h_lists = [h_contador]

    for contador_h in range(0,len(h_lists[list_n])):

        if h_lists[list_n][contador_h].get() == 1:
            contador_h_lists[list_n][contador_h].configure(state=NORMAL)
        else:
            contador_h_lists[list_n][contador_h].configure(state=DISABLED)


#Ventana Principal
main.title("Generador de Presupuestos")
main.config(bg=color_primario)
main.resizable(1,1)

#Frames 
top_frame = Frame(main,bd=5,relief=FLAT)
left_frame = Frame(main,bd=5,relief=FLAT)
right_frame = Frame(main,bd=5,relief=FLAT)
bottom_frame = Frame(main,bd=5,relief=FLAT)

top_frame.pack(side=TOP)
left_frame.pack(side=LEFT)
right_frame.pack(side=RIGHT)
bottom_frame.pack(side=BOTTOM)

#Labels
# top_frame_lbl = Label(top_frame,font=("Helvetica",78),text="Generador de Presupuestos",fg="White",bg=color_primario)
# top_frame_lbl.pack()

concepto_frame = Frame(top_frame,bd=0,relief=FLAT, bg=color_claro)
concepto_frame.grid(row=0,column=0)
concepto_frame_lbl = LabelFrame(concepto_frame,font=("Helvetica",18),text="Concepto",fg=color_primario)
concepto_frame_lbl.pack(side=TOP)

funciones_frame = Frame(top_frame,bd=0,relief=FLAT)
funciones_frame.grid(row=1,column=0)
funciones_frame_lbl = LabelFrame(funciones_frame,font=("Helvetica",18),text="Funciones",fg=color_primario)
funciones_frame_lbl.pack(side=TOP)

#entry

#Conceptos
concepto_list = ["Trabajo", "Extra", "Equipo", "Material", "Transporte", "Subtotal", "IVA", "IRPF", "Total"]
funciones_list = ["Calcular Presupuesto", "Generar Factura", "Registro Histórico", "Enviar email"]

concepto_opciones = list()
concepto_contador = list()
contador = 0
for concepto in concepto_list:

    concepto_opciones.append(IntVar())
    Checkbutton(concepto_frame_lbl,text=concepto,font=("Helvetica",18),onvalue=1,offvalue=0,variable=concepto_opciones[contador],command=lambda:activar_pb(0)).grid(row=contador,column=0,sticky=W)
    concepto_contador.append(Entry(concepto_frame_lbl,font=("Helvetica",18),justify=CENTER,bd=1,width=3,state=DISABLED))
    concepto_contador[contador].grid(row=contador,column=1,sticky=W)
    contador += 1

funciones_opciones = list()
funciones_contador = list()
contador = 0
for funciones in funciones_list:

    funciones_opciones.append(IntVar())
    Checkbutton(funciones_frame_lbl,text=funciones,font=("Helvetica",18),onvalue=1,offvalue=0,variable=funciones_opciones[contador],command=lambda:activar_pb(0)).grid(row=contador,column=0,sticky=W)
    funciones_contador.append(Entry(funciones_frame_lbl,font=("Helvetica",18),justify=CENTER,bd=1,width=3,state=DISABLED))
    funciones_contador[contador].grid(row=contador,column=1,sticky=W)
    contador += 1


main.mainloop()