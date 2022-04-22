from .models import Comprobante
from django.db import connection


def generar_comprobante(tipo_de_comprobante: int):
    """Sirve para generar un comprobante electronico ya sea Factura, Boleta o Notas en base a un pedido, https://docs.google.com/document/d/1QWWSILBbjd4MDkJl7vCkL2RZvkPh0IC7Wa67BvoYIhA/edit#"""

    operacion = 'generar_comprobante'
    tipo = ''
    if tipo_de_comprobante == 1:
        # esta serie se deberia de guardar en la bd en una tabla de series para que cuando el contador desee cambiar de serie se modifique en esa tabla
        serie = 'FFF1'  # Serie.objects.filter(tipo='FACTURA').first()
        tipo = 'FACTURA'

    elif tipo_de_comprobante == 2:
        serie = 'BBB1'
        tipo = 'BOLETA'

    elif tipo_de_comprobante == 3 or tipo_de_comprobante == 4:
        serie = '0001'
        tipo = 'NOTA'

    # si queremos hacer uso de una vista, vista materializada, funcion o procedimiento almacenado que no este registrado en el ORM entonces podremos hacer uso de una RAW QUERY de la siguiente manera:
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM vista_prueba')
        print(cursor.fetchall())

    # lo sacaremos del ultimo comprobante almacenado en la base de datos
    # SELECT numero, serie FROM comprobantes WHERE tipo = 'boleta' | 'factura' ORDER BY numero desc LIMIT 1;
    # https://docs.djangoproject.com/en/4.0/ref/models/querysets/#order-by
    ultimoComprobante = Comprobante.objects.values_list('numero', 'serie').filter(
        tipo=tipo).order_by('-numero').first()
    # (1, 'FFF1')

    # if not ultimoComprobante:
    if ultimoComprobante is None:
        numero = 1
    else:
        numero = int(ultimoComprobante[0]) + 1
