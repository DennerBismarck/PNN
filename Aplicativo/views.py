from django.shortcuts import render, redirect
from Aplicativo import forms
from Aplicativo import models

def index(request):
    necessitados = models.Necessitado.objects.all()
    listagem = {'necessitados_chave': necessitados}
    return render(request, "index.html", listagem)

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

# ===================================================================
# CRUD de Situação
# ===================================================================

def createSituacao(request):
    form = forms.SituacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_situacao': form}
    return render(request, "situacao.html", listagem)

def updateSituacao(request, id_situacao):
    Situacao = models.Situacao.objects.get(pk=id_situacao)
    form = forms.SituacaoForm(request.POST or None, instance=Situacao)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_situacao': form}
    return render(request, "situacao.html", listagem)

def deleteSituacao(request, id_situacao):
    Situacao = models.Situacao.objects.get(pk=id_situacao)
    Situacao.delete()
    return redirect("main")

# ===================================================================
# CRUD de Genero
# ===================================================================

def createGenero(request):
    form = forms.GeneroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_genero': form}
    return render(request, "genero.html", listagem)

def updateGenero(request, id_genero):
    Genero = models.Genero.objects.get(pk=id_genero)
    form = forms.GeneroForm(request.POST or None, instance=Genero)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_genero': form}
    return render(request, "genero.html", listagem)

def deleteGenero(request, id_genero):
    Genero = models.Genero.objects.get(pk=id_genero)
    Genero.delete()
    return redirect("main")

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
# CRUD de ATUALIZAÇÕES
# ===================================================================

def createAtualizacao(request):
    form = forms.AtualizacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_atualizacao': form}
    return render(request, "atualizacao.html", listagem)

def updateAtualizacao(request, id_atualizacao):
    Atualizacao = models.Atualizacao.objects.get(pk=id_atualizacao)
    form = forms.AtualizacaoForm(request.POST or None, instance=Atualizacao)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_atualizacao': form}
    return render(request, "atualizacao.html", listagem)

def deleteAtualizacao(request, id_atualizacao):
    Atualizacao = models.Atualizacao.objects.get(pk=id_atualizacao)
    Atualizacao.delete()
    return redirect("main")