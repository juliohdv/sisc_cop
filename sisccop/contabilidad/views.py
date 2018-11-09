from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import TipoCuenta, Cuenta, Transaccion, DetalleTransaccion, Periodo
from decimal import *

# Create your views here.
def index(request):
	return render(request,'contabilidad/index.html')

def catalogoCuentas(request):
	tipoCuentasList = TipoCuenta.objects.filter()
	cuentasList = Cuenta.objects.filter().order_by('id')
	return render(request,'contabilidad/catalogoCuentas.html', {'tipoCuentasList':tipoCuentasList, 'cuentasList':cuentasList})

def guardarCuenta(request):
	if request.method == 'POST' and request.POST.get('sbmName', False) == 'sbmGuardarCuenta':
		Cuenta.objects.create(
				codigo = int(request.POST['codigoCuenta']),
				nombre = request.POST['nombreCuenta'],
				descripcion = request.POST['descripcionCuenta'],
				debe = 0.0,
				haber = 0.0,
				idTipoCuenta = TipoCuenta.objects.get(id=request.POST['tipoCuenta'])
			)
		return HttpResponse('Cuenta guardada con éxito')
	return HttpResponse('Error')

def eliminarCuenta(request, idCuenta):
	if request.method == 'POST':
		instancia = Cuenta.objects.get(id=idCuenta)
		instancia.delete()
		return HttpResponse('Borrado');
	return HttpResponse('Error');

def editarCuenta(request):
	if request.method == 'POST':
		i = request.POST['i']
		instancia = Cuenta.objects.get(id=request.POST['idCuenta_'+str(i)])
		instancia.codigo = request.POST['codigoCuenta_'+str(i)]	#id del Tag HTML
		instancia.nombre = request.POST['nombreCuenta_'+str(i)]
		instancia.descripcion = request.POST['descripcionCuenta_'+str(i)]
		instancia.idTipoCuenta = TipoCuenta.objects.get(id=request.POST['tipoCuenta_'+str(i)])
		instancia.save()
		return HttpResponse('Cuenta Actualizada con Éxito')
	return HttpResponse('Error')

def agregarTransaccion(request):

	transaccion = Transaccion.objects.create()
	cuentasList = Cuenta.objects.filter()
	detalles = transaccion.detalle.all()
	return render(request,'contabilidad/agregarTransaccion.html', {'transaccion':transaccion, 'cuentasList':cuentasList})

def agregarDetalle(request):

	if request.method == 'POST' and request.POST.get('sbmNam', False) == 'sbmDetalle':

		detalle1 = DetalleTransaccion.objects.create(
				fecha = request.POST['fechaD'],
				cuenta = Cuenta.objects.get(id=request.POST['cuentaD']),
				descripcion = request.POST['descripcionD'],
				debe = Decimal(request.POST['debeD']),
				haber = Decimal(request.POST['haberD'])
		)
		transaccion = Transaccion.objects.get(id=request.POST['transaccionD'])
		transaccion.detalle.add(detalle1)
		transaccion.save()
		
		return HttpResponse('Detalle Agregado a la Transacción')

	return HttpResponse('Error')