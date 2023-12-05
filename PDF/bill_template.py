import pdfkit
import jinja2
import os
from datetime import datetime

today = datetime.today().strftime('%d de %b de %Y')
num_factura = ""

#Porsupuestapp

## Profesional
logo = "icono_camara.png"
nom_empresa_profesional = "Pablo Izaguerri"
direccion_profesional = "Calle Roma, 155"
zip_profesional = "08011"
telefono_profesional = "699 657 4554"
email_profesional = "mailto@gmail.com"
portfolio_profesional = "www.pabloizaguerri.com"
cif_profesional = "5555555-Y"

## Cliente
nom_empresa_cliente = "Fundesplai"
direccion_cliente = "Carrer Estrella"
zip_cliente = "08009"
telefono_cliente = "699 998 998"
cif_cliente = "65756547-A"

## Trabajo
trabajo_unidades = "5"
trabajo_precio_unitario = "25"
trabajo_total = "125"

## Horas
horas_unidades = "5"
horas_precio_unitario = "25"
horas_total = "125"

## Material
material_unidades = "5"
material_precio_unitario = "25"
material_total = "125"

## Transporte
transporte_unidades = "5"
transporte_precio_unitario = "25"
transporte_total = "125"

## Extra
extra_unidades = "5"
extra_precio_unitario = "25"
extra_total = "125"

## Totales
subtotal = "suma_totales"
iva = "subtotal*0,21"
irpf = "subtotal*0,14"
total = "subtotal+iva-irpf"

## Pago
iban = "ESXX XXXX XXXX XXXX"
swift = "XXXX XX XX XXX"

datos = {
        'logo' : logo,
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
        'subtotal' : subtotal,
        'iva' : iva,
        'irpf' : irpf,
        'total' : total,
        'iban' : iban,
        'swift' : swift
        }


template_loader = jinja2.FileSystemLoader("")
template_env = jinja2.Environment(loader=template_loader)
plantilla_html = template_env.get_template("./factura.html")

output_text = plantilla_html.render(datos)

config = pdfkit.configuration(wkhtmltopdf = "/usr/local/bin/wkhtmltopdf")
# input which wkhtmltopdf

nombre_pdf = (f"factura_{num_factura}.pdf")
pdfkit.from_string(output_text, nombre_pdf, configuration=config, css='./style.css')


