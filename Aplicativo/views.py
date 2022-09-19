from django.shortcuts import render, redirect
from Aplicativo.forms import NecessitadoForm
from Aplicativo.models import Necessitado

def index(request):
    necessitados = Necessitado.objects.all()
    listagem = {'necessitados_chave': necessitados}
    return render(request, "index.html", listagem)

# ===================================================================
# CRUD de NECESSITADOS
# ===================================================================

def createNecessitado(request):
    form = NecessitadoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_necessitado': form}
    return render(request, "necessitado.html", listagem)

def updateNecessitado(request, id_necessitado):
    necessitado = Necessitado.objects.get(pk=id_necessitado)
    form = NecessitadoForm(request.POST or None, instance=necessitado)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_necessitado': form}
    return render(request, "necessitado.html", listagem)

def deleteNecessitado(request, id_necessitado):
    necessitado = Necessitado.objects.get(pk=id_necessitado)
    necessitado.delete()
    return redirect("main")