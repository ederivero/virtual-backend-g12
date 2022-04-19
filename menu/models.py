from django.db import models
from cloudinary import models as modelsCloudinary


class Plato(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, null=False)
    foto = modelsCloudinary.CloudinaryField(
        folder='plato')  # models.ImageField()
    disponible = models.BooleanField(default=True, null=False)
    precio = models.FloatField(null=False)

    class Meta:
        db_table = 'platos'


class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(null=False)
    cantidad = models.IntegerField(null=False)
    precio_diario = models.FloatField(null=False)

    # related_name > servira para ingresar desde el modelo del cual se esta creando la relacion (en este caso desde platos podremos ingresar a todos sus stocks)
    # on_delete > que accion tomara cuando se desee eliminar el padre (la PK)
    #   CASCADE > eliminara el registro del plato y todos los stocks que tengan ese registro tbn seran eliminados en cascada
    #   PROTECT > impedira que se realice la eliminacion del Plato si tiene stocks
    #   SET_NULL > eliminara el plato y todos sus stocks colocara en su FK el valor de NULL
    #   DO_NOTHING > eliminara el plato y no cambiara nada de los stocks (seguiran con el mismo valor ya eliminado)
    #   RESTRICT > no permite la eliminacion y lanzara un error de tipo RestrictedError (hara un raise)
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.ForeignKey.on_delete
    platoId = models.ForeignKey(
        to=Plato, related_name='stocks', on_delete=models.CASCADE, db_column='plato_id')

    class Meta:
        db_table = 'stocks'
        # unique_together > crea un indice de dos o mas columnas en el cual no se podran repetir los mismos valores de esas columnas
        # https://docs.djangoproject.com/en/4.0/ref/models/options/#unique-together
        #   fecha    | plato_id
        # 2022-04-18 |   1      ✅
        # 2022-04-18 |   1      ❌
        # 2022-04-18 |   2      ✅
        # 2022-04-19 |   1      ✅
        unique_together = [['fecha', 'platoId']]
