from django.shortcuts               import render, redirect
from Localidade                     import models, forms
from django.contrib.auth.decorators import login_required
import requests, folium

# ==================================================================
# API e REQUESTS para DATABASE de CIDADE e ESTADO
# ==================================================================

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

# ===================================================================
# CRUD de CIDADE
# ===================================================================

@login_required(login_url="/login")
def createCidade(request):
    form = forms.CidadeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("main")
    Cidades = models.Cidade.objects.all()
    listagem = {'form_cidade': form, 'cidades_chave': Cidades}
    return render(request, "ShowCidade.html", listagem)

@login_required(login_url="/login")
def updateCidade(request, id_cidade):
    cidade = models.Cidade.objects.get(pk=id_cidade)
    form = forms.CidadeForm(request.POST or None, instance=cidade)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_cidade': form}
    return render(request, "ShowCidade.html", listagem)

@login_required(login_url="/login")
def deleteCidade(request, id_cidade):
    Cidade = models.Cidade.objects.get(pk=id_cidade)
    Cidade.delete()
    return redirect("main")

# ===================================================================
# CONFIGURAÇÃO DE MAPA
# ===================================================================

def map(request):
    figure = folium.Figure()
    url = ("PNN/static")
    state_geo = f"{url}/br_states.json"
    m = folium.Map(location=[-15.77972, -47.92972], zoom_start=4.1)
    folium.Choropleth(
        geo_data=state_geo,
        name="choropleth",
        fill_color="green",
        fill_opacity=0.7,
        line_opacity=0.2,
    ).add_to(m)
    folium.LayerControl().add_to(m)
    m.add_to(figure)
    figure.render()
    return render(request,'map.html',{"map":figure})