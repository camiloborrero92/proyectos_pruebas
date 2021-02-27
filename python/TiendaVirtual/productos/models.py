from django.db import models

# Create your models here.
class Producto(models.Model):
    #Campos del Producto
    id = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=200,null = False)
    proveedor = models.CharField(max_length=200, null = False)
    countries = (
        ('COL', 'Colombia'),
        ('VNZ', 'Venezuela'),
        ('USA', 'Estados Unidos'),
        ('CHN', 'China'),
        ('JPN', 'Japon'),
    )
    PaisProveedor = models.CharField(max_length=3, choices=countries)
    fecha_ingreso = models.DateField()

    #nombre a visualizar
    def __str__(self):
        return self.nombre_producto