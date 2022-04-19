from django.db import models


class Comprobante(models.Model):
    id = models.AutoField(primary_key=True)
    serie = models.CharField(max_length=5, null=False)
    numero = models.CharField(max_length=10, null=False)
    pdf = models.TextField()
    cdr = models.TextField()
    xml = models.TextField()
    tipo = models.CharField(choices=(['BOLETA', 'BOLETA'], [
                            'FACTURA', 'FACTURA']), null=False, max_length=10)

    class Meta:
        db_table = 'comprobantes'
        unique_together = [['serie', 'numero']]


class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()
    total = models.FloatField(null=False)
    numeroDocumentoCliente = models.CharField(max_length=12)
    tipoDocumentoCliente = models.CharField(
        choices=(['RUC', 'RUC'], ['DNI', 'DNI']), max_length=5)
    mesa = models.IntegerField()
    propina = models.FloatField()

    comprobante = models.OneToOneField(
        to=Comprobante, related_name='pedido', on_delete=models.CASCADE, db_column='comprobante_id')

    # hacer la relacion de ForeignKey con el modelo Usuarios
