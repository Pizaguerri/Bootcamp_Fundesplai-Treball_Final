#import os
from tkinter import *
import csv

#Abre Pop Up de Datos Cliente
popup_cliente = Tk()

COLOR_OSCURO = "#373737"
COLOR_CLARO = "#f8f8f8"

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
        try:
            dict_datos_cliente = next(dato)  # Intenta leer la primera línea del archivo CSV
        except StopIteration:
            # Si el archivo está vacío, inicializa dict_datos_cliente como un diccionario vacío
            dict_datos_cliente = {}
        for datos in datos_clientes:
            row = Frame(popup_cliente, bd=0, padx=0, pady=1, width=5, relief=FLAT, bg=COLOR_CLARO)
            lab = Label(row, width=15, text=datos, anchor=W, bd=0, padx=0, pady=1, relief=FLAT, bg=COLOR_CLARO, fg=COLOR_OSCURO)
            ent = Entry(row, bg=COLOR_CLARO, fg=COLOR_OSCURO)
            valor = dict_datos_cliente.get(datos, '')  # Obtiene el valor del diccionario o un string vacío si no existe
            ent.insert(END, valor)
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)
            entries.append((datos, ent))
        # Botón Guardar al final de los Entries
        guardar = Button(popup_cliente, text='Guardar', font=("Helvetica", 18), bd=0, padx=5, pady=5,
                         width=15, relief=FLAT, bg=COLOR_CLARO, fg=COLOR_OSCURO,
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
popup_cliente.config(bg=COLOR_OSCURO)
popup_cliente.resizable(1,1)
popup_cliente.minsize(625, 675)
#popup_cliente.maxsize(825, 875)

# Frames 
popup_cliente_frame = Frame(popup_cliente,bd=20,relief=FLAT, bg=COLOR_CLARO)
popup_cliente_frame.pack(side=BOTTOM, fill="both", expand=True, padx=10, pady=10)
popup_cliente_frame.place(in_=popup_cliente, anchor="c", relx=.5, rely=.5)
popup_cliente_frame_lbl = LabelFrame(popup_cliente_frame,font=("Helvetica",18),text="Introducir datos de profesional",fg=COLOR_OSCURO, bg=COLOR_CLARO)


# Botón Guardar guarda
if __name__ == '__main__':
    ents = guardar_datos_cliente(popup_cliente_frame)
    def on_return_pressed(event, ents=ents):
        boton_save(ents, dict_datos_cliente, datos_clientes)
    popup_cliente.bind('<Return>', on_return_pressed)



popup_cliente.mainloop()