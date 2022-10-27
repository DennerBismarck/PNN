from django.shortcuts               import render, redirect
from Aplicativo                     import forms, models
from Usuario.models                 import Usuario
from Localidade.views               import requestDBEstado, requestDBCidade
from Localidade                     import models as modelsL
from django.contrib.auth.decorators import login_required

def user_is_authenticated(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.usu_nome
    return username

# ==================================================================
# INDEX
# ==================================================================

def index(request):
    # Verificando se os ESTADOS e CIDADES já foram ADICIONADOS ao DB
    if (set(modelsL.Estado.objects.filter(est_id=1)) == set(modelsL.Estado.objects.none())):
        requestDBEstado()
    if (set(modelsL.Cidade.objects.filter(cid_id=1)) == set(modelsL.Cidade.objects.none())):
        requestDBCidade()

    # Criar primeiros GÊNEROS
    if not (models.Genero.objects.filter(gen_generos="Masculino").first()):
        model = models.Genero(gen_generos="Masculino")
        model.save()
    if not (models.Genero.objects.filter(gen_generos="Feminino").first()):
        model = models.Genero(gen_generos="Feminino")
        model.save()
    if not (models.Genero.objects.filter(gen_generos="Outro").first()):
        model = models.Genero(gen_generos="Outro")
        model.save()

    necessitados = models.Necessitado.objects.all()
    listagem = {
        'necessitados_chave': necessitados, 
        'user': user_is_authenticated(request),
    }
    return render(request, "index.html", listagem)

# ===================================================================
# CRUD de NECESSITADOS
# ===================================================================

@login_required(login_url="/login")
def createNecessitado(request):
    form = forms.NecessitadoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_necessitado': form, 'request': list}
    return render(request, "necessitado.html", listagem)

@login_required(login_url="/login")
def updateNecessitado(request, id_necessitado):
    necessitado = models.Necessitado.objects.get(pk=id_necessitado)
    form = forms.NecessitadoForm(request.POST or None, instance=necessitado)
    atualizacoes = models.Atualizacao.objects.filter(att_nec_id=necessitado)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_necessitado': form, 'necessitado': necessitado, 'atualizacoes': atualizacoes}
    return render(request, "necessitado.html", listagem)

@login_required(login_url="/login")
def deleteNecessitado(request, id_necessitado):
    necessitado = models.Necessitado.objects.get(pk=id_necessitado)
    necessitado.delete()
    return redirect("main")

# ===================================================================
# CRUD de Atualização
# ===================================================================

@login_required(login_url="/login")
def createAtualizacao(request):
    form = forms.AtualizacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_atualizacao': form, 'request': list}
    return render(request, "atualizacao.html", listagem)

@login_required(login_url="/login")
def updateAtualizacao(request, id_atualizacao):
    Atualizacao = models.Atualizacao.objects.get(pk=id_atualizacao)
    form = forms.AtualizacaoForm(request.POST or None, instance=Atualizacao)


    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_atualizacao': form, 'Atualizacao': Atualizacao}
    return render(request, "atualizacao.html", listagem)

@login_required(login_url="/login")
def deleteAtualizacao(request, id_atualizacao):
    Atualizacao = models.Atualizacao.objects.get(pk=id_atualizacao)
    Atualizacao.delete()
    return redirect("main")

# ===================================================================
# CRUD de Situação
# ===================================================================

@login_required(login_url="/login")
def createSituacao(request):
    form = forms.SituacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_Situacao': form}
    return render(request, "Situacao.html", listagem)

@login_required(login_url="/login")
def updateSituacao(request, id_Situacao):
    Situacao = models.Situacao.objects.get(pk=id_Situacao)
    form = forms.SituacaoForm(request.POST or None, instance=Situacao)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_Situacao': form}
    return render(request, "Situacao.html", listagem)

@login_required(login_url="/login")
def deleteSituacao(request, id_Situacao):
    Situacao = models.Situacao.objects.get(pk=id_Situacao)
    Situacao.delete()
    return redirect("main")

# ===================================================================
# CRUD de Profissão
# ===================================================================

@login_required(login_url="/login")
def createProfissao(request):
    form = forms.ProfissaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_profissao': form}
    return render(request, "profissao.html", listagem)

@login_required(login_url="/login")
def updateProfissao(request, id_profissao):
    Profissao = models.Profissao.objects.get(pk=id_profissao)
    form = forms.ProfissaoForm(request.POST or None, instance=Profissao)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_profissao': form}
    return render(request, "profissao.html", listagem)

@login_required(login_url="/login")
def deleteProfissao(request, id_profissao):
    Profissao = models.Profissao.objects.get(pk=id_profissao)
    Profissao.delete()
    return redirect("main")

# ===================================================================
# TIMELINE
# ===================================================================

@login_required(login_url="/login")
def createTimeline(request, id_necessitado):
    necessitado = models.Necessitado.objects.get(pk=id_necessitado)
    form = forms.NecessitadoForm(request.POST or None, instance=necessitado)
    atualizacoes = models.Atualizacao.objects.filter(att_nec_id=necessitado)
    if form.is_valid():
        user = Usuario.objects.filter(usu_nome=user_is_authenticated(request)).first()
        atualizacao = models.Atualizacao(
            att_nec_id          = necessitado,
            att_usu_id          = user, 
            att_nec_nome        = form['nec_nome'].value(),
            att_nec_idade       = form['nec_idade'].value(),
            att_nec_logradouro  = form['nec_logradouro'].value(),
            att_nec_cpf         = form['nec_cpf'].value(),
            att_nec_sit_id      = models.Situacao.objects.get(sit_id=form['nec_sit_id'].value()),
            att_nec_pro_id      = models.Profissao.objects.get(pro_id=form['nec_pro_id'].value()),
            att_nec_gen_id      = models.Genero.objects.get(gen_id=form['nec_gen_id'].value()),
            att_nec_cid_id      = modelsL.Cidade.objects.get(cid_id=form['nec_cid_id'].value()),
        )
        atualizacao.save()
        return redirect("main")
    listagem = {'form_necessitado': form, 'necessitado': necessitado, 'atualizacoes': atualizacoes}
    return render(request, "necessitado.html", listagem)

@login_required(login_url="/login")
def updateTimeline(request, id_necessitado, id_atualizacao):
    listNumber = int(id_atualizacao)-1
    Necessitado = models.Necessitado.objects.get(pk=id_necessitado)
    Atualizacao = models.Atualizacao.objects.filter(att_nec_id=Necessitado)[listNumber]
    form = forms.AtualizacaoForm(request.POST or None, instance=Atualizacao)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_atualizacao': form, 'Atualizacao': Atualizacao, 'teste': listNumber}
    return render(request, "atualizacao.html", listagem)

@login_required(login_url="/login")
def deleteTimeline(request, id_necessitado, id_atualizacao):
    listNumber = int(id_atualizacao)-1
    Necessitado = models.Necessitado.objects.get(pk=id_necessitado)
    Atualizacao = models.Atualizacao.objects.filter(att_nec_id=Necessitado)[listNumber]
    Atualizacao.delete()
    return redirect("main")