from django.shortcuts   import render, redirect
from ONG                import forms, models

# ===================================================================
# CRUD de ONG
# ===================================================================

def createONG(request):
    form = forms.ONGForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("main")
    ONGs = models.ONG.objects.all()
    listagem = {'form_ONG': form, 'ONG_chave': ONGs}
    return render(request, "ShowONG.html", listagem)

def updateONG(request, id_ONG):
    ONG = models.ONG.objects.get(pk=id_ONG)
    form = forms.ONGForm(request.POST or None, instance=ONG)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_ONG': form}
    return render(request, "ShowONG.html", listagem)

def deleteONG(request, id_ONG):
    ONG = models.ONG.objects.get(pk=id_ONG)
    ONG.delete()
    return redirect("main")