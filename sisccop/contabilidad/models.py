from django.db import models

# Create your models here.
class TipoCuenta(models.Model):
	id = models.AutoField(primary_key=True)
	tipoCuenta = models.CharField(max_length=200)
	def __str__(self):
		return '{}'.format(self.tipoCuenta)

class Cuenta(models.Model):
	id = models.AutoField(primary_key=True)
	codigo = models.IntegerField()
	nombre = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=200)
	debe = models.FloatField()
	haber = models.FloatField()
	idTipoCuenta = models.ForeignKey('TipoCuenta', on_delete=models.CASCADE, default='0000000')
	def __str__(self):
		return '{}'.format(self.nombre)

class Periodo(models.Model):
	id = models.AutoField(primary_key=True)
	descripcion = models.TextField(max_length=200)
	fechaInicio = models.DateField()
	fechaFin = models.DateField()
	periodo = models.CharField(max_length=50)

class DetalleTransaccion(models.Model):
	id = models.AutoField(primary_key=True)
	cuenta = models.ForeignKey('Cuenta', on_delete=models.CASCADE)
	debe = models.FloatField()
	haber = models.FloatField()
	descripcion= models.TextField(max_length=200)
	fecha = models.DateField()
	fechaRegistro = models.DateField(auto_now=True)

	def __str__(self):
		return '{}'.format(self.descripcion)

class Transaccion(models.Model):
	id = models.AutoField(primary_key=True)
	descripcion = models.TextField(max_length=200)
	detalle = models.ManyToManyField('DetalleTransaccion')
	debe = models.FloatField(default=0)
	haber = models.FloatField(default=0)
	periodo = models.ForeignKey('Periodo', on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return '{}'.format(self.id)