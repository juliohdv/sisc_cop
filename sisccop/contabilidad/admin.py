from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(TipoCuenta)
admin.site.register(Cuenta)
admin.site.register(Periodo)
admin.site.register(DetalleTransaccion)
admin.site.register(Transaccion)
