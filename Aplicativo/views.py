from django.shortcuts import render, redirect
from Aplicativo import forms, models
import folium, requests, json, urllib
import pandas as pd
    
# API PARA CIDADES E ESTADOS
def requestAPI():
    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/distritos'
    r = requests.get(url)
    rlist = r.json()
    return rlist

def requestDBEstado():
    rlist = requestAPI()
    for municipio in rlist:
        estado = municipio['municipio']['regiao-imediata']['regiao-intermediaria']['UF']['nome']
        EstadoList = models.Estado(est_estado=estado)
        estadoVerify = models.Estado.objects.filter(est_estado=estado)
        if (set(estadoVerify) == set(models.Estado.objects.none())):
            EstadoList.save()

def requestDBCidade():
    rlist = requestAPI()
    for municipio in rlist:
        estado = municipio['municipio']['regiao-imediata']['regiao-intermediaria']['UF']['nome']
        cidade = municipio['municipio']['nome']
        CidadeList = models.Cidade(cid_cidade=cidade, cid_est_id=models.Estado.objects.get(est_estado=estado))
        cidadeVerify = models.Cidade.objects.filter(cid_cidade=cidade)
        if (set(cidadeVerify) == set(models.Cidade.objects.none())):
            CidadeList.save()

def index(request):
    # Verificando se os ESTADOS e CIDADES já foram ADICIONADOS ao DB
    if (set(models.Estado.objects.filter(est_id=1)) == set(models.Estado.objects.none())):
        requestDBEstado()
        if (set(models.Cidade.objects.filter(cid_id=1)) == set(models.Cidade.objects.none())):
            requestDBCidade()

    necessitados = models.Necessitado.objects.all()
    listagem = {
        'necessitados_chave': necessitados, 
    }
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
    listagem = {'form_necessitado': form, 'request': list}
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
# CRUD de Situação
# ===================================================================

def createSituacao(request):
    form = forms.SituacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_Situacao': form}
    return render(request, "Situacao.html", listagem)

def updateSituacao(request, id_Situacao):
    Situacao = models.Situacao.objects.get(pk=id_Situacao)
    form = forms.SituacaoForm(request.POST or None, instance=Situacao)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_Situacao': form}
    return render(request, "Situacao.html", listagem)

def deleteSituacao(request, id_Situacao):
    Situacao = models.Situacao.objects.get(pk=id_Situacao)
    Situacao.delete()
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
    listagem = {'form_profissao': form}
    return render(request, "profissao.html", listagem)

def updateProfissao(request, id_profissao):
    Profissao = models.Profissao.objects.get(pk=id_profissao)
    form = forms.ProfissaoForm(request.POST or None, instance=Profissao)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_profissao': form}
    return render(request, "profissao.html", listagem)

def deleteProfissao(request, id_profissao):
    Profissao = models.Profissao.objects.get(pk=id_profissao)
    Profissao.delete()
    return redirect("main")

# ===================================================================
# CRUD de ONG
# ===================================================================

def createONG(request):
    form = forms.ONGForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_ONG': form}
    return render(request, "ONG.html", listagem)

def updateONG(request, id_ONG):
    ONG = models.ONG.objects.get(pk=id_ONG)
    form = forms.ONGForm(request.POST or None, instance=ONG)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_ONG': form}
    return render(request, "ONG.html", listagem)

def deleteONG(request, id_ONG):
    ONG = models.ONG.objects.get(pk=id_ONG)
    ONG.delete()
    return redirect("main")