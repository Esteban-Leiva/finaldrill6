from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from web.forms import MainForm
from web.models import *
# Create your views here.

def catalogo(request):
    autos = []
    autos = Autos.objects.values('marca', 'modelo', 'carroceria', 'motor', 'categoria', 'precio')
    context = {'autos': autos}
    return render(request, 'catalogo.html', context)

def anadir(request):
    if request.method == "POST":
        form = MainForm(request.POST)
        if form.is_valid():
            m = form.cleaned_data["marca"]
            mo = form.cleaned_data["modelo"]
            c = form.cleaned_data["carroceria"]
            mot = form.cleaned_data["motor"]
            ca = form.cleaned_data["categoria"]
            p = form.cleaned_data["precio"]
            auto = Autos(marca=m, modelo=mo, carroceria=c, motor=mot, categoria=ca, precio=p)
            auto.save()
        context = {'form': form}
    else:
        context = {'form': MainForm()}
    return render(request, 'forms.html', context)