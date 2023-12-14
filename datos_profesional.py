#import os
from tkinter import *
import csv

#Abre Pop Up de Datos Profesional
popup_prof = Tk()

color_primario = "#373737"
color_claro = "#f8f8f8"

# Funciones
## Abre CSV Profesional y lee los datos guardados por defecto
dict_datos_profesional = {}
with open("datos_profesional.csv", "r", encoding="utf-8") as datos_profesional:
    dato = csv.DictReader(datos_profesional)
    for diccionario_en_fila in dato:
        dict_datos_profesional = diccionario_en_fila
#print(dict_datos_profesional)

## Lista de Labels de los Entries de Datos Profesionales
datos_profesionales = ['Profesional', 'Direccion', 'CP', 'CIF', 'Telefono', 'Email', 'Portfolio', 'IBAN', 'SWIFT', 'Nuevo']

## Genera los Entries y muestra los datos guardados por defecto, y recoge los datos de profesional sobreescritos. Deja los datos en blanco si existen.
def guardar_datos_prof(popup_prof):
    entries = []
    with open("datos_profesional.csv", "r", encoding="utf-8") as datos_profesional:
        dato = csv.DictReader(datos_profesional)
        dict_datos_profesional = next(dato)  # Lee la primera línea del archivo CSV
        for datos in datos_profesionales:
            row = Frame(popup_prof, bd=0, padx=0, pady=1, width=5, relief=FLAT, bg=color_claro)
            lab = Label(row, width=15, text=datos, anchor=W, bd=0, padx=0, pady=1, relief=FLAT, bg=color_claro, fg=color_primario)
            ent = Entry(row,bg=color_claro,fg=color_primario)
            valor = dict_datos_profesional.get(datos, '')  # Obtiene el valor del diccionario o un string vacío si no existe
            ent.insert(END, valor)
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)
            entries.append((datos, ent))

            # Botón Guardar al final de los Entries
        guardar = Button(popup_prof, text='Guardar', font=("Helvetica", 18), bd=0, padx=5, pady=5,
                         width=15, relief=FLAT, bg=color_claro, fg=color_primario,
                         command=(lambda e=entries: boton_save(e, dict_datos_profesional, datos_profesionales)))
        guardar.pack(side=BOTTOM, padx=5, pady=15)
        
    return entries


## Al clickar Guardar, recoge los campos Entry, modifica el Dict
## Abre CSV Profesional y sobreescribe los datos nuevos de los entries
def boton_save(entries, dict_datos_profesional, datos_profesionales):
    #print(entries)
    for entry in entries:
        dict_datos_profesional[entry[0]] = entry[1].get()
    #print(dict_datos_profesional)
    with open("datos_profesional.csv", "w", encoding="utf-8") as datos_profesional:
        writer = csv.DictWriter(datos_profesional, fieldnames=datos_profesionales, lineterminator="\n")
        writer.writeheader()
        writer.writerow(dict_datos_profesional)


# Ventana Principal
popup_prof.title("Datos de Profesional")
popup_prof.config(bg=color_primario)
popup_prof.resizable(1,1)
popup_prof.minsize(625, 675)
#popup_prof.maxsize(825, 875)

# Frames 
popup_prof_frame = Frame(popup_prof,bd=20,relief=FLAT, bg=color_claro)
popup_prof_frame.pack(side=BOTTOM, fill="both", expand=True, padx=10, pady=10)
popup_prof_frame.place(in_=popup_prof, anchor="c", relx=.5, rely=.5)
popup_prof_frame_lbl = LabelFrame(popup_prof_frame,font=("Helvetica",18),text="Introducir datos de profesional",fg=color_primario, bg=color_claro)


# Botón Guardar guarda
if __name__ == '__main__':
    ents = guardar_datos_prof(popup_prof_frame)
    popup_prof.bind('<Return>', (lambda e=ents: boton_save(e, dict_datos_profesional, datos_profesionales)))   


popup_prof.mainloop()