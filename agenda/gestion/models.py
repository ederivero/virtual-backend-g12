from django.db import models

class Etiqueta(models.Model):
    # Tipos de Columnas > https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types
    # Opciones de las columnas > https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-options
    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.CharField(max_length=20, unique=True, null=False)
    # Columnas de auditoria
    # son columnas que podran ayudar al seguimiento de la creacion de registros
    # createdAt > es la fecha en la cual se creo el registro
    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')
    # updatedAt > es la fecha en la cual se modifico algun campo del registro
    updatedAt = models.DateTimeField(auto_now=True, db_column='updated_at')

    # todas las configuraciones propias de la tabla se haran mediante la definicion de sus atributos en la clase Meta
    # https://docs.djangoproject.com/en/4.0/ref/models/options/
    class Meta:
        # cambiar el nombre de la tabla en la bd (a diferencia del nombre de la clase)
        db_table = 'etiquetas'
        # modificar el ordernamiento natural (por el id) e imponinendo el propio que sea ASC del nombre, solamente funcionara para cuando hagamos el get usando el ORM
        ordering = ['-nombre']


class Tareas(models.Model):

    class CategoriaOpciones(models.TextChoices):
        # cada opcion le podemos pasar dos parametros en la cual el primero sera su abreviatura para que se guarde en la bd y el segundo el nombre completo
        TODO = 'TODO', 'TO_DO'
        IN_PROGRESS = 'IP', 'IN_PROGRESS'
        DONE = 'DONE', 'DONE'
        CANCELLED = 'CANCELLED', 'CANCELLED'

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, null=False)
    # Forma 1 usando una subclase que herede de TextChoices
    categoria = models.CharField(max_length=45, choices=CategoriaOpciones.choices, default=CategoriaOpciones.TODO)
    
    fechaCaducidad=
    importancia=

    # Forma 2 usando una lista de tuplas
    # categoria = models.CharField(max_length=45, choices=[
    #     ('TODO','TO_DO'), 
    #     ('IP', 'IN_PROGRESS'),
    #     ('DONE', 'DONE'),
    #     ('CANCELLED', 'CANCELLED')
    #     ], default='TODO')