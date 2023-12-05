import os
from tkinter import *
popup_cliente = Tk()

color_primario = "#373737"
color_claro = "#f8f8f8"

#Ventana Principal
popup_cliente.title("Datos de Cliente")
popup_cliente.config(bg=color_primario)
popup_cliente.resizable(1,1)
popup_cliente.minsize(600, 600)

#Frames 
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



#Guardar Datos Profesionales
datos_profesionales = 'Cliente', 'Dirección', 'ZIP', 'Teléfono', 'CIF'


def save(entries):
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        print('%s: "%s"' % (field, text)) 


def guardar_datos_prof(popup_cliente, fields):
    entries = []
    for datos in datos_profesionales:
        row = Frame(popup_cliente)
        lab = Label(row, width=15, text=datos, anchor=W)
        ent = Entry(row)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append((datos, ent))
    return entries


if __name__ == '__main__':
    ents = guardar_datos_prof(popup_cliente, datos_profesionales)
    popup_cliente.bind('<Return>', (lambda event, e=ents: save(e)))   
    guardar = Button(popup_cliente, text='Guardar', font=("Helvetica",18), bd=0, padx=5, pady=5, width=15, relief=FLAT, bg=color_claro, fg=color_primario, command=(lambda e=ents: guardar(e)))
    guardar.pack(side=RIGHT, padx=2, pady=2)
    guardar.place(in_=popup_cliente_frame, anchor='se', relx=-25)
    salir = Button(popup_cliente, text='Salir', font=("Helvetica",18), bd=0, padx=5, pady=5, width=15, relief=FLAT, bg=color_claro, fg=color_primario, command=popup_cliente.quit)
    salir.pack(side=LEFT, padx=2, pady=2)
    salir.place(in_=popup_cliente_frame, anchor='sw', relx=25)



popup_cliente.mainloop()