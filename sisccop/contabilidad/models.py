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