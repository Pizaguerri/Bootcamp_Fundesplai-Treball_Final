import pdfkit
import jinja2
import os
from datetime import datetime
import csv
#from porsupuestapp import dict_totals

def generar_factura(dict_totals):
        # print("pdf")
        # print(dict_totals)
        today = datetime.today().strftime('%d de %b de %Y')


        dict_datos_profesional = {}
        with open("datos_profesional.csv", "r", encoding="utf-8") as datos_profesional:
                dato = csv.DictReader(datos_profesional)
                for diccionario_en_fila in dato:
                        dict_datos_profesional = diccionario_en_fila
                #print(dict_datos_profesional)

        ## Abre CSV Cliente y lee los datos guardados por defecto
        dict_datos_cliente = {}
        with open("datos_cliente.csv", "r", encoding="utf-8") as datos_cliente:
                dato = csv.DictReader(datos_cliente)
                for diccionario_en_fila in dato:
                        dict_datos_cliente = diccionario_en_fila
                #print(dict_datos_cliente)



        # Recoge datos de HTML para el PDF

        ## Profesional
        # logo = "icono_camara.png"
        nom_empresa_profesional = dict_datos_profesional['Profesional']
        direccion_profesional = dict_datos_profesional['Direccion']
        zip_profesional = dict_datos_profesional['CP']
        telefono_profesional = dict_datos_profesional['Telefono']
        email_profesional = dict_datos_profesional['Email']
        portfolio_profesional = dict_datos_profesional['Portfolio']
        cif_profesional = dict_datos_profesional['CIF']

        ## Cliente
        nom_empresa_cliente = dict_datos_cliente['Cliente']
        direccion_cliente = dict_datos_cliente['Direccion']
        zip_cliente = dict_datos_cliente['CP']
        telefono_cliente = dict_datos_cliente['Telefono']
        email_cliente = dict_datos_cliente['Email']
        cif_cliente = dict_datos_cliente['CIF']

        ## Trabajo
        trabajo_unidades = "5"
        trabajo_precio_unitario = "25"
        trabajo_total = dict_totals['Trabajo']

        ## Horas
        horas_unidades = "5"
        horas_precio_unitario = "25"
        horas_total = dict_totals['Horas']

        ## Material
        material_unidades = "5"
        material_precio_unitario = "25"
        material_total = dict_totals['Material']

        ## Transporte
        transporte_unidades = "5"
        transporte_precio_unitario = "25"
        transporte_total = dict_totals['Transporte']

        ## Extra
        extra_unidades = "5"
        extra_precio_unitario = "25"
        extra_total = dict_totals['Extra']

        ## Totales
        subtotal = dict_totals['Trabajo']+dict_totals['Horas']+dict_totals['Material']+dict_totals['Transporte']+dict_totals['Extra']
        iva = subtotal*0.21
        irpf = subtotal*0.14
        print(type(subtotal), type(iva), type(irpf))
        total = f"{(subtotal+iva-irpf):.2f}"
        
        ## Pago
        iban = dict_datos_profesional['IBAN']
        swift = dict_datos_profesional['SWIFT']

        datos = {
                # 'logo' : logo,
                'nom_empresa_profesional' : nom_empresa_profesional,
                'direccion_profesional' : direccion_profesional,
                'zip_profesional' : zip_profesional,
                'telefono_profesional' : telefono_profesional,
                'email_profesional' : email_profesional,
                'portfolio_profesional' : portfolio_profesional,
                'cif_profesional' : cif_profesional,
                'nom_empresa_cliente' : nom_empresa_cliente,
                'direccion_cliente' : direccion_cliente,
                'zip_cliente' : zip_cliente,
                'telefono_cliente' : telefono_cliente,
                'email_cliente' : email_cliente,
                'cif_cliente' : cif_cliente,
                'trabajo_unidades' : trabajo_unidades,
                'trabajo_precio_unitario' : trabajo_precio_unitario,
                'trabajo_total' : trabajo_total,
                'horas_unidades' : horas_unidades,
                'horas_precio_unitario' : horas_precio_unitario,
                'horas_total' : horas_total,
                'material_unidades' : material_unidades,
                'material_precio_unitario' : material_precio_unitario,
                'material_total' : material_total,
                'transporte_unidades' : transporte_unidades,
                'transporte_precio_unitario' : transporte_precio_unitario,
                'transporte_total' : transporte_total,
                'extra_unidades' : extra_unidades,
                'extra_precio_unitario' : extra_precio_unitario,
                'extra_total' : extra_total,
                'subtotal' : f"{subtotal:.2f}",
                'iva' : f"{iva:.2f}",
                'irpf' : f"{irpf:.2f}",
                'total' : total,
                'iban' : iban,
                'swift' : swift
                }



        # Generador de PDF según los datos que recoge
        ## Ruta HTML y CSS
        ruta = "/Users/pabloizaguerri/Documents/Python_2023/Treball Final/"
        ## Carga las plantillas
        template_loader = jinja2.FileSystemLoader(searchpath=ruta)
        template_env = jinja2.Environment(loader=template_loader)
        plantilla_html = template_env.get_template("factura.html")

        #datos = {}

        output_text = plantilla_html.render(datos)
        config = pdfkit.configuration(wkhtmltopdf="/usr/local/bin/wkhtmltopdf") #which wkhtmltopdf
        ultima_factura_generada = 1
        num_factura = ultima_factura_generada + 1
        nombre_pdf = f"factura_{num_factura:03}.pdf"  #3 números a la factura
        css = f"{ruta}style.css"
        pdfkit.from_string(output_text, nombre_pdf, configuration=config, css=css)



# dict_totals = {'Trabajo': 12.0, 'Horas': 0.0, 'Material': 0.0, 'Transporte': 0.0, 'Extra': 0.0}
# generar_factura(dict_totals)