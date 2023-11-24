import os
from tkinter import *

main = Tk()

# entry

datos = 'Nombre Empresa', 'CIF', 'Dirección', 'País', 'Fecha'

main.Label(main, text="Nombre").grid(row=0)
main.Label(main, text="CIF").grid(row=1)
main.Label(main, text="Dirección").grid(row=2)
main.Label(main, text="Pais").grid(row=3)
main.Label(main, text="Fecha").grid(row=4)
#Otro que haga un número de recibo (contador) automático para cada FACTURA generada

dato1 = main.Entry(main)
dato2 = main.Entry(main)

dato1.grid(row=0, column=1)
dato2.grid(row=1, column=1)


def campos_entrada():
    print("Nombre: %s\nLast Name: %s" % (dato1.get(), dato2.get()))
    dato1.delete(0, main.END)
    dato2.delete(0, main.END)

main.Label(main, text="Nombre").grid(row=0)
main.Label(main, text="CIF").grid(row=1)
main.Label(main, text="Dirección").grid(row=2)
main.Label(main, text="Pais").grid(row=3)
main.Label(main, text="Fecha").grid(row=4)

dato1 = main.Entry(master)
dato2 = main.Entry(master)
e1.insert(10, "Miller")
e2.insert(10, "Jill")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, text='Show', command=show_entry_fields).grid(row=3, 
                                                               column=1, 
                                                               sticky=tk.W, 
                                                               pady=4)



def fetch(entries):
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        print('%s: "%s"' % (field, text)) 

def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries

if __name__ == '__main__':
    root = tk.Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
    b1 = tk.Button(root, text='Show',
                  command=(lambda e=ents: fetch(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()

main.mainloop()