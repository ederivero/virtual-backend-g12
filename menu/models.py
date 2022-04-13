from django.db import models


class Plato(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, null=False)
    foto = models.ImageField()
    disponible = models.BooleanField(default=True, null=False)
    precio = models.FloatField(null=False)

    class Meta:
        db_table = 'platos'
