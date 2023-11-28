""" Generador de Presupuestos """

import os
from tkinter import *

main = Tk()

color_primario = "#373737"
color_claro = "#f8f8f8"
color_secundario = "#1183b8"
color_terciario = "#f48d24"

# estilos = (font("Helvetica",18), bg=color_claro, fg=color_primario)

#Precio Base o unitario por defecto (pb)
def activar_pb(list_n):
    pb_lists = [concepto_opciones]
    contador_pb_lists = [concepto_contador]

    for contador_pb in range(0,len(pb_lists[list_n])):
        if pb_lists[list_n][contador_pb].get() == 1:
            contador_pb_lists[list_n][contador_pb].configure(state=NORMAL)
        else:
            contador_pb_lists[list_n][contador_pb].configure(state=DISABLED)


#Valor horas trabajadas (h)
def activar_h(list_n):
    h_lists = [[concepto_opciones]]
    contador_h_lists = [concepto_contador]

    for contador_h in range(0,len(h_lists[list_n])):
        if h_lists[list_n][contador_h].get() == 1:
            contador_h_lists[list_n][contador_h].configure(state=NORMAL)
        else:
            contador_h_lists[list_n][contador_h].configure(state=DISABLED)


#Ventana Principal
main.title("Generador de Presupuestos")
main.config(bg=color_primario) #Color del fondo de la ventana
main.resizable(1,1)


#Frames 
top_frame = Frame(main,bd=10,relief=FLAT, bg=color_claro)
left_frame = Frame(main,bd=10,relief=FLAT, bg=color_claro)
right_frame = Frame(main,bd=10,relief=FLAT, bg=color_claro)
bottom_frame = Frame(main,bd=10,relief=FLAT, bg=color_claro)

top_frame.pack(side=TOP)
left_frame.pack(side=LEFT)
right_frame.pack(side=RIGHT)
bottom_frame.pack(side=BOTTOM)

#Labels
concepto_frame = Frame(top_frame,bd=0,relief=FLAT, bg=color_claro)
concepto_frame_lbl = LabelFrame(concepto_frame,font=("Helvetica",18),text="Conceptos",fg=color_primario, bg=color_claro)
botones_frame = Frame(top_frame,bd=0,relief=FLAT, bg=color_claro)
botones_frame_lbl = LabelFrame(botones_frame,font=("Helvetica",18),text="Opciones",fg=color_primario, bg=color_claro)

concepto_frame.grid(row=0,column=0)
concepto_frame_lbl.pack(side=TOP)
botones_frame.grid(row=1,column=0)
botones_frame_lbl.pack(side=TOP)



#Listas de conceptos y opciones
concepto_list = ["Trabajo", "Extra", "Equipo", "Material", "Transporte", "Subtotal", "IVA", "IRPF", "Total"]
botones_list = ["Calcular Presupuesto", "Generar Factura", "Registro Histórico", "Enviar email"]
totales_list = ["Subtotal", "Total"]

#Checkbuttons de los conceptos con caja de entrada de valores
concepto_opciones = list()
concepto_contador = list()
contador = 0
for concepto in concepto_list:
    concepto_opciones.append(IntVar())
    #cajas_texto = Checkbutton(concepto_frame_lbl, text=concepto, bg=color_claro, fg=color_primario, font=("Helvetica",18), onvalue=1, offvalue=0, variable=concepto_opciones[contador], command=lambda:activar_pb(0))
    cajas_texto = Checkbutton(concepto_frame_lbl, text=concepto, bg=color_claro, fg=color_primario, font=("Helvetica",18), variable=concepto_opciones[contador], command=lambda:activar_pb(0))
    cajas_texto.grid(row=contador,column=0,sticky=W)
    concepto_contador.append(Entry(concepto_frame_lbl, font=("Helvetica",18), justify=CENTER, bd=1, width=7, state=DISABLED, fg=color_primario, bg=color_claro))
    concepto_contador[contador].grid(row=contador,column=1,sticky=W)
    #2 cajas de entry extra
    # concepto_contador.append(Entry(concepto_frame_lbl, font=("Helvetica",18), justify=CENTER, bd=1, width=7, state=DISABLED, fg=color_primario, bg=color_claro))
    # concepto_contador[contador].grid(row=contador,column=contador,sticky=W)
    # concepto_contador.append(Entry(concepto_frame_lbl, font=("Helvetica",18), justify=CENTER, bd=1, width=7, state=DISABLED, fg=color_primario, bg=color_claro))
    # concepto_contador[contador].grid(row=contador,column=3,sticky=W)
    contador += 1


#Botones de funciones
botones_opciones = list()
botones_contador = list()
contador = 0
for botones in botones_list:
    botones_opciones.append(IntVar())
    botones = Button(botones_frame_lbl, text=botones, font=("Helvetica",18), bd=0, padx=2, pady=2, width=16, relief=FLAT, bg=color_claro, fg=color_primario)
    botones.grid(row=contador+1, column=0, sticky=W)
    contador += 1


main.mainloop()