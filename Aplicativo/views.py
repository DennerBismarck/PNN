from django.shortcuts import render, redirect
from Aplicativo import forms, models
import folium, requests, json, urllib

def index(request):
    m = folium.Map()
    m = m._repr_html_()

    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/33/municipios'
    r = requests.get(url)
    list = r.json()

    print(r)
    necessitados = models.Necessitado.objects.all()
    listagem = {'necessitados_chave': necessitados, 'map': m, 'request': list[1]}
    return render(request, "index.html", listagem)

# ===================================================================
# SISTEMA DE AUTENTICAÇÃO
# ===================================================================

def login(request):
    return render(request, "authentication/login.html")

def cadastro(request):
    return render(request, "authentication/cadastro.html")

# ===================================================================
# CRUD de NECESSITADOS
# ===================================================================

def createNecessitado(request):
    form = forms.NecessitadoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_necessitado': form}
    return render(request, "necessitado.html", listagem)

def updateNecessitado(request, id_necessitado):
    necessitado = models.Necessitado.objects.get(pk=id_necessitado)
    form = forms.NecessitadoForm(request.POST or None, instance=necessitado)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_necessitado': form}
    return render(request, "necessitado.html", listagem)

def deleteNecessitado(request, id_necessitado):
    necessitado = models.Necessitado.objects.get(pk=id_necessitado)
    necessitado.delete()
    return redirect("main")

# ===================================================================
# CRUD de ESTADO
# ===================================================================

def createEstado(request):
    form = forms.EstadoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_estado': form}
    return render(request, "estado.html", listagem)

def updateEstado(request, id_estado):
    Estado = models.Estado.objects.get(pk=id_estado)
    form = forms.EstadoForm(request.POST or None, instance=Estado)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_estado': form}
    return render(request, "estado.html", listagem)

def deleteEstado(request, id_estado):
    Estado = models.Estado.objects.get(pk=id_estado)
    Estado.delete()
    return redirect("main")


# ===================================================================
# CRUD de CIDADE
# ===================================================================

def createCidade(request):
    form = forms.CidadeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_cidade': form}
    return render(request, "cidade.html", listagem)

def updateCidade(request, id_cidade):
    cidade = models.Cidade.objects.get(pk=id_cidade)
    form = forms.CidadeForm(request.POST or None, instance=cidade)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_cidade': form}
    return render(request, "cidade.html", listagem)

def deleteCidade(request, id_cidade):
    Cidade = models.Cidade.objects.get(pk=id_cidade)
    Cidade.delete()
    return redirect("main")

# ===================================================================
# CRUD de Profissão
# ===================================================================

def createProfissao(request):
    form = forms.ProfissaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_Profissao': form}
    return render(request, "profissao.html", listagem)

def updateProfissao(request, id_profissao):
    Profissao = models.Profissao.objects.get(pk=id_profissao)
    form = forms.ProfissaoForm(request.POST or None, instance=Profissao)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_Profissao': form}
    return render(request, "profissao.html", listagem)

def deleteProfissao(request, id_profissao):
    Profissao = models.Profissao.objects.get(pk=id_profissao)
    Profissao.delete()
    return redirect("main")