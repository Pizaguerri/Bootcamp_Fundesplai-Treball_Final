import os
from tkinter import *
main = Tk()

color_primario = "#373737"
color_claro = "#f8f8f8"

#Ventana Principal
main.title("PORSUPUESTAPP")
main.config(bg=color_primario)
main.resizable(1,1)
main.minsize(600, 600)

#Frames 
top_frame = Frame(main,bd=10,relief=FLAT, bg=color_claro)
top_frame.pack(side=TOP, fill="both", expand=True, padx=20, pady=20)
top_frame.place(in_=main, anchor="c", relx=.5, rely=.5)

popup_prof_frame = Frame(top_frame,bd=0,relief=FLAT, bg=color_claro)
popup_prof_frame.pack(side=TOP, fill="both", expand=True, padx=10, pady=10)
popup_prof_frame.place(in_=top_frame, anchor="c", relx=.5, rely=.5)
popup_prof_frame_lbl = LabelFrame(popup_prof_frame,font=("Helvetica",18),text="Introducir datos de profesional",fg=color_primario, bg=color_claro)

boton_prof_frame = Frame(popup_prof_frame, bd=0, bg= color_claro)
boton_prof_frame.grid(row=1, column=0)
boton_prof_frame.pack(side=BOTTOM)



#Guardar Datos Profesionales
datos_profesionales = 'Nombre', 'CIF', 'Email', 'Teléfono', 'Portfolio', 'Dirección'


def save(entries):
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        print('%s: "%s"' % (field, text)) 


def guardar_datos_prof(main, fields):
    entries = []
    for datos in datos_profesionales:
        row = Frame(main)
        lab = Label(row, width=15, text=datos, anchor=W)
        ent = Entry(row)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append((datos, ent))
    return entries


if __name__ == '__main__':
    ents = guardar_datos_prof(main, datos_profesionales)
    main.bind('<Return>', (lambda event, e=ents: save(e)))   
    guardar = Button(main, text='Guardar', font=("Helvetica",18), bd=0, padx=5, pady=5, width=15, relief=FLAT, bg=color_claro, fg=color_primario, command=(lambda e=ents: guardar(e)))
    guardar.pack(side=RIGHT, padx=2, pady=2)
    guardar.place(in_=popup_prof_frame, anchor='c', relx=5)
    salir = Button(main, text='Salir', font=("Helvetica",18), bd=0, padx=5, pady=5, width=15, relief=FLAT, bg=color_claro, fg=color_primario, command=main.quit)
    salir.pack(side=LEFT, padx=2, pady=2)
    salir.place(in_=popup_prof_frame, anchor='c', relx=-5)



main.mainloop()