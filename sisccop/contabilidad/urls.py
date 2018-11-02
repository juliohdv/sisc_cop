from django.conf.urls import include, url


from . import views

urlpatterns=[
	url(r'^$',views.index,name='index'),
	url(r'^catalogoCuentas/$',views.catalogoCuentas,name='catalogoCuentas'),
	url(r'^guardarCuenta/$',views.guardarCuenta,name='guardarCuenta'),
	url(r'^eliminarCuenta/(?P<idCuenta>\d+)$',views.eliminarCuenta, name='eliminarCuenta'),
]