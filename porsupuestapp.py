""" Generador de Presupuestos """

import os
from tkinter import *

main = Tk()

color_primario = "#373737"
color_claro = "#f8f8f8"
color_secundario = "#1183b8"
color_terciario = "#f48d24"


#Precio Base o unitario por defecto (pb)
def activar_textos(list_n):
    texto_lists = [concepto_opciones]
    contador_textos_lists = [concepto_contador_ent_1, concepto_contador_ent_2, concepto_contador_ent_3]
    for contador_textos in range(0,len(texto_lists[list_n])):
        if texto_lists[list_n][contador_textos].get() == 1:
            contador_textos_lists[0][contador_textos].configure(state=NORMAL)
            contador_textos_lists[1][contador_textos].configure(state=NORMAL)
            contador_textos_lists[2][contador_textos].configure(state=NORMAL)
        else:
            contador_textos_lists[0][contador_textos].configure(state=DISABLED)
            contador_textos_lists[1][contador_textos].configure(state=DISABLED)
            contador_textos_lists[2][contador_textos].configure(state=DISABLED)



#Ventana Principal
main.title("PORSUPUESTAPP")
main.config(bg=color_primario) #Color del fondo de la ventana
main.resizable(1,1)
main.minsize(625, 675)


#Frames 
top_frame = Frame(main,bd=10,relief=FLAT, bg=color_claro)
left_frame = Frame(main,bd=10,relief=FLAT, bg=color_claro)
right_frame = Frame(main,bd=10,relief=FLAT, bg=color_claro)
bottom_frame = Frame(main,bd=10,relief=FLAT, bg=color_claro)

top_frame.pack(side=TOP, fill="both", expand=True, padx=20, pady=20)
top_frame.place(in_=main, anchor="c", relx=.5, rely=.5)
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
concepto_contador_ent_1 = list()
concepto_contador_ent_2 = list()
concepto_contador_ent_3 = list()
contador = 0
for concepto in concepto_list:
    concepto_opciones.append(IntVar())
    #cajas_texto = Checkbutton(concepto_frame_lbl, text=concepto, bg=color_claro, fg=color_primario, font=("Helvetica",18), onvalue=1, offvalue=0, variable=concepto_opciones[contador], command=lambda:activar_pb(0))
    cajas_texto = Checkbutton(concepto_frame_lbl, text=concepto, bd=2, bg=color_claro, fg=color_primario, font=("Helvetica",18), relief=FLAT, variable=concepto_opciones[contador], command=lambda:activar_textos(0))
    cajas_texto.grid(row=contador,column=0,sticky=W, padx=30, pady=5)
    concepto_contador_ent_1.append(Entry(concepto_frame_lbl, font=("Helvetica",18), relief=FLAT, justify=CENTER, bd=2, width=7, state=DISABLED, fg=color_primario, bg=color_claro))
    concepto_contador_ent_1[contador].grid(row=contador,column=1,sticky=W)
    #2 cajas de entry extra
    concepto_contador_ent_2.append(Entry(concepto_frame_lbl, font=("Helvetica",18), relief=FLAT, justify=CENTER, bd=2, width=7, state=DISABLED, fg=color_primario, bg=color_claro))
    concepto_contador_ent_2[contador].grid(row=contador,column=2,sticky=W)
    concepto_contador_ent_3.append(Entry(concepto_frame_lbl, font=("Helvetica",18), relief=FLAT, justify=CENTER, bd=2, width=7, state=DISABLED, fg=color_primario, bg=color_claro))
    concepto_contador_ent_3[contador].grid(row=contador,column=3,sticky=W)
    contador += 1


#Botones de funciones
botones_opciones = list()
botones_contador = list()
contador = 0
for botones in botones_list:
    botones_opciones.append(IntVar())
    botones = Button(botones_frame_lbl, text=botones, font=("Helvetica",18), bd=1, padx=5, pady=5, width=36, relief=FLAT, bg=color_claro, fg=color_primario)
    botones.grid(row=contador+1, column=0, sticky=W)
    contador += 1


main.mainloop()