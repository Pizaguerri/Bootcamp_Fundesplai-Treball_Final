import jinja2
import pdfkit
from datetime import datetime

today = datetime.today().strftime('%d de %b de %Y')

#Porsupuestapp
nom_empresa_profesional = "Pablo Izaguerri"
direccion_profesional = "Carrer Sol"
zip_profesional = "07350"
cif_profesional = "43463313-Y"
telefono_profesional = "699 737 453"

nom_empresa_cliente = "Fundesplai"
direccion_cliente = "Carrer Estrella"
zip_cliente = "08009"
cif_cliente = "65756547-A"
telefono_cliente = "699 998 998"

# Trabajo
trabajo_unidades = "5"
trabajo_precio_unitario = "25"
trabajo_total = "125"

# Horas
horas_unidades = "5"
horas_precio_unitario = "25"
horas_total = "125"

# Equipo
equipo_unidades = "5"
equipo_precio_unitario = "25"
equipo_total = "125"

# Material
material_unidades = "5"
material_precio_unitario = "25"
material_total = "125"

# Transporte
transporte_unidades = "5"
transporte_precio_unitario = "25"
transporte_total = "125"

subtotal = "suma_totales"
iva = "subtotal*0,21"
irpf = "subtotal*0,14"
total = "subtotal+iva-irpf"

iban = "ESXX XXXX XXXX XXXX"
swift = "XXXX XX XX XXX"

datos = {
'nom_empresa_profesional' : "Pablo Izaguerri",
'direccion_profesional' : "Carrer Sol",
'zip_profesional' : "07350",
'cif_profesional' : "43463313-Y",
'telefono_profesional' : "699 737 453",
'nom_empresa_cliente' : "Fundesplai",
'direccion_cliente' : "Carrer Estrella",
'zip_cliente' : "08009",
'cif_cliente' : "65756547-A",
'telefono_cliente' : "699 998 998",
'trabajo_unidades' : "5",
'trabajo_precio_unitario' : "25",
'trabajo_total' : "125",
'horas_unidades' : "5",
'horas_precio_unitario' : "25",
'horas_total' : "125",
'equipo_unidades' : "5",
'equipo_precio_unitario' : "25",
'equipo_total' : "125",
'material_unidades' : "5",
'material_precio_unitario' : "25",
'material_total' : "125",
'transporte_unidades' : "5",
'transporte_precio_unitario' : "25",
'transporte_total' : "125",
'subtotal' : "suma_totales",
'iva' : "subtotal*0,21",
'irpf' : "subtotal*0,14",
'total' : "subtotal+iva-irpf",
'iban' : "ESXX XXXX XXXX XXXX",
'swift' : "XXXX XX XX XXX"
}

template_loader = jinja2.FileSystemLoader("")
template_env = jinja2.Environment(loader=template_loader)
plantilla_html = template_env.get_template("./templates/factura.html")

output_text = plantilla_html.render(datos)

config = pdfkit.configuration(wkhtmltopdf = "/usr/local/bin/wkhtmltopdf")
#input which wkhtmltopdf

nombre_pdf = "factura_plantilla.pdf"
pdfkit.from_string(output_text, nombre_pdf, configuration=config, css='./templates/style.css')


