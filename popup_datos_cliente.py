#import os
from tkinter import *
import csv

#Abre Pop Up de Datos Cliente
popup_cliente = Tk()

color_primario = "#373737"
color_claro = "#f8f8f8"

# Funciones
## Abre CSV Cliente y lee los datos guardados por defecto
dict_datos_cliente = {}
with open("datos_cliente.csv", "r", encoding="utf-8") as datos_cliente:
    dato = csv.DictReader(datos_cliente)
    for diccionario_en_fila in dato:
        dict_datos_cliente = diccionario_en_fila
#print(dict_datos_cliente)

## Lista de Labels de los Entries de Datos Cliente
datos_clientes = ['Cliente', 'Direccion', 'CP', 'Telefono', 'Email', 'CIF']

## Genera los Entries y muestra los datos guardados por defecto, y recoge los datos de cliente sobreescritos
def guardar_datos_cliente(popup_cliente):
    entries = []
    for datos in datos_clientes:
        #print(dict_datos_cliente[datos])
        row = Frame(popup_cliente)
        lab = Label(row, width=15, text=datos, anchor=W)
        ent = Entry(row)
        ent.insert(END, dict_datos_cliente[datos])
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append((datos, ent))
    return entries


## Al clickar Guardar, recoge los campos Entry, modifica el Dict
## Abre CSV Cliente y sobreescribe los datos nuevos de los entries
def boton_save(entries, dict_datos_cliente, datos_cliente):
    #print(entries)
    for entry in entries:
        dict_datos_cliente[entry[0]] = entry[1].get()
    #print(dict_datos_cliente)
    with open("datos_cliente.csv", "w", encoding="utf-8") as datos_cliente:
        writer = csv.DictWriter(datos_cliente, fieldnames=datos_clientes, lineterminator="\n")
        writer.writeheader()
        writer.writerow(dict_datos_cliente)


# Ventana Principal
popup_cliente.title("Datos de Cliente")
popup_cliente.config(bg=color_primario)
popup_cliente.resizable(1,1)
popup_cliente.minsize(600, 600)
popup_cliente.maxsize(800, 800)

# Frames 
top_frame = Frame(popup_cliente,bd=10,relief=FLAT, bg=color_claro)
top_frame.pack(side=TOP, fill="both", expand=True, padx=20, pady=20)
top_frame.place(in_=popup_cliente, anchor="c", relx=.5, rely=.5)

popup_cliente_frame = Frame(top_frame,bd=0,relief=FLAT, bg=color_claro)
popup_cliente_frame.pack(side=TOP, fill="both", expand=True, padx=10, pady=10)
popup_cliente_frame.place(in_=top_frame, anchor="c", relx=.5, rely=.5)
popup_cliente_frame_lbl = LabelFrame(popup_cliente_frame,font=("Helvetica",18),text="Introducir datos de profesional",fg=color_primario, bg=color_claro)

boton_prof_frame = Frame(popup_cliente_frame, bd=0, bg= color_claro)
boton_prof_frame.grid(row=1, column=0)
boton_prof_frame.pack(side=BOTTOM)


# Genera los botones Guardar y Salir
if __name__ == '__main__':
    ents = guardar_datos_cliente(popup_cliente)
    popup_cliente.bind('<Return>', (lambda e=ents: boton_save(e, dict_datos_cliente, datos_clientes)))   
    guardar = Button(popup_cliente, text='Guardar', font=("Helvetica",18), bd=0, padx=5, pady=5, width=15, relief=FLAT, bg=color_claro, fg=color_primario, command=(lambda e=ents: boton_save(e, dict_datos_cliente, datos_clientes)))
    guardar.pack(side=RIGHT, padx=2, pady=2)
    guardar.place(in_=popup_cliente_frame, anchor='se', relx=-25)
    salir = Button(popup_cliente, text='Salir', font=("Helvetica",18), bd=0, padx=5, pady=5, width=15, relief=FLAT, bg=color_claro, fg=color_primario, command=popup_cliente.quit)
    salir.pack(side=LEFT, padx=2, pady=2)
    salir.place(in_=popup_cliente_frame, anchor='sw', relx=25)


popup_cliente.mainloop()