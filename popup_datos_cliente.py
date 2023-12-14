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
    with open("datos_cliente.csv", "r", encoding="utf-8") as datos_cliente:
        dato = csv.DictReader(datos_cliente)
        dict_datos_cliente = next(dato)  # Lee la primera línea del archivo CSV
        for datos in datos_clientes:
            row = Frame(popup_cliente, bd=0, padx=0, pady=1, width=5, relief=FLAT, bg=color_claro)
            lab = Label(row, width=15, text=datos, anchor=W, bd=0, padx=0, pady=1, relief=FLAT, bg=color_claro, fg=color_primario)
            ent = Entry(row,bg=color_claro,fg=color_primario)
            valor = dict_datos_cliente.get(datos, '')  # Obtiene el valor del diccionario o un string vacío si no existe
            ent.insert(END, valor)
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)
            entries.append((datos, ent))

            # Botón Guardar al final de los Entries
        guardar = Button(popup_cliente, text='Guardar', font=("Helvetica", 18), bd=0, padx=5, pady=5,
                         width=15, relief=FLAT, bg=color_claro, fg=color_primario,
                         command=(lambda e=entries: boton_save(e, dict_datos_cliente, datos_clientes)))
        guardar.pack(side=BOTTOM, padx=5, pady=15)
        
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
popup_cliente.minsize(625, 675)
#popup_cliente.maxsize(825, 875)

# Frames 
popup_cliente_frame = Frame(popup_cliente,bd=20,relief=FLAT, bg=color_claro)
popup_cliente_frame.pack(side=BOTTOM, fill="both", expand=True, padx=10, pady=10)
popup_cliente_frame.place(in_=popup_cliente, anchor="c", relx=.5, rely=.5)
popup_cliente_frame_lbl = LabelFrame(popup_cliente_frame,font=("Helvetica",18),text="Introducir datos de profesional",fg=color_primario, bg=color_claro)


# Botón Guardar guarda
if __name__ == '__main__':
    ents = guardar_datos_cliente(popup_cliente_frame)
    popup_cliente.bind('<Return>', (lambda e=ents: boton_save(e, dict_datos_cliente, datos_clientes)))   


popup_cliente.mainloop()