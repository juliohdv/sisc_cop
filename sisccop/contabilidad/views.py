from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import TipoCuenta, Cuenta

# Create your views here.
def index(request):
	return render(request,'contabilidad/index.html')

def catalogoCuentas(request):
	tipoCuentasList = TipoCuenta.objects.filter()
	cuentasList = Cuenta.objects.filter()
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
