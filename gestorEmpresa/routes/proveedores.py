from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from gestorEmpresa.models import Proveedor


def index(request):
    proveedor = Proveedor.objects.create(
        nombre_proveedor= "Empresa 1",
        telefono_proveedor = "987654321",
        direccion_proveedor = "Calle Nombre, 1, 2ºB",
        cif_proveedor = "12345678A",
        facturacion_proveedor = 1500.5,
    )
    proveedor.save()

    query_proveedor = Proveedor.objects.get(id=1)
    query_proveedor
    context = {
        'proveedor' : query_proveedor
    }

    return render(request, 'index.html', context)