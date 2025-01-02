from django.db import models

class Responsable(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Sector(models.Model):
    nombre = models.CharField(max_length=255)
    color = models.CharField(max_length=7, help_text="Color en formato HEX (ej: #FF0000)", default="#000000")

    def __str__(self):
        return self.nombre

class Partido(models.Model):
    nombre = models.CharField(max_length=255)
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True, blank=True)
    imagen = models.ImageField(upload_to='partidos/', null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    fecha_fundacion = models.DateField(null=True, blank=True)
    sitio_web = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class CasoCorrupcion(models.Model):

    ESTADO_CHOICES = (
        ('En Proceso', 'En Proceso'),
        ('Resuelto', 'Resuelto'), 
        ('Cerrado', 'Cerrado'),
        ('En Investigación', 'En Investigación'),
        ('Formalizado', 'Formalizado'),
        ('Sentenciado', 'Sentenciado'),
        ('Condenado', 'Condenado')
    )
    caso = models.CharField(max_length=255)
    monto = models.BigIntegerField(null=True, blank=True)
    año = models.IntegerField()
    responsables = models.ManyToManyField(Responsable, blank=True)  
    partido = models.ForeignKey(Partido, on_delete=models.SET_NULL, null=True, blank=True)
    ano_inicio = models.IntegerField(null=True, blank=True)
    ano_fin = models.IntegerField(null=True, blank=True)
    comuna = models.ForeignKey('ComunaChileCUT', on_delete=models.SET_NULL, null=True, blank=True)
    posicion = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(
        max_length=255,
        choices=ESTADO_CHOICES,
        default='En Proceso'
    )
    sentencia = models.CharField(max_length=255, null=True, blank=True)
    condena = models.CharField(max_length=255, null=True, blank=True)
    conclusiones = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.caso

class RegionChileCUT(models.Model):
    cut_region = models.IntegerField(primary_key=True)
    region = models.CharField(max_length=255)

    def __str__(self):
        return self.region

class ProvinciaChileCUT(models.Model):
    cut_provincia = models.IntegerField(primary_key=True)
    provincia = models.CharField(max_length=255)
    region = models.ForeignKey(RegionChileCUT, on_delete=models.CASCADE)

    def __str__(self):
        return self.provincia

class ComunaChileCUT(models.Model):
    cut_comuna = models.IntegerField(primary_key=True)
    comuna = models.CharField(max_length=255)
    provincia = models.ForeignKey(ProvinciaChileCUT, on_delete=models.CASCADE)

    def __str__(self):
        return self.comuna

class CorruptionPerceptionIndexChile(models.Model):
    año = models.IntegerField()
    pais = models.CharField(max_length=100)
    cpi = models.IntegerField()

    def __str__(self):
        return f'{self.año} - {self.pais}'

class Encuesta(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class CEPDatosPercepcion(models.Model):
    año = models.IntegerField()
    mes = models.IntegerField()
    fecha = models.DateField()
    encuesta = models.IntegerField()
    detalle_encuesta = models.CharField(max_length=255)
    grupo = models.CharField(max_length=50)
    variable = models.CharField(max_length=255)
    porcentaje = models.FloatField()
    porcentaje_ic_inferior = models.FloatField()
    porcentaje_ic_superior = models.FloatField()

    def __str__(self):
        return f'{self.fecha} - {self.variable}'
