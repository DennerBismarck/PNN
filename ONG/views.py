from django.shortcuts   import render, redirect
from ONG                import forms, models
from django.contrib.auth.decorators import login_required

# ===================================================================
# CRUD de ONG
# ===================================================================

@login_required(login_url="/login")
def createONG(request):
    form_ONG        = forms.ONGForm(request.POST or None)
    form_tel_ONG    = forms.TelONGForm(request.POST or None)
    form_email_ONG  = forms.EmailONGForm(request.POST or None)

    if form_ONG.is_valid():
        form_ONG.save()

        ong_id    = models.ONG.objects.filter(ong_nome=form_ONG['ong_nome'].value()).first()
        ong_tel  = form_tel_ONG['ton_telefone'].value()
        ong_email    = form_email_ONG['emo_email'].value()

        ong_aux_tel = models.TEL_DAS_ONGS(ton_ong_id=ong_id, ton_telefone=ong_tel)
        ong_aux_ema = models.EMAIL_DAS_ONGS(emo_ong_id=ong_id, emo_email=ong_email)
        ong_aux_tel.save()
        ong_aux_ema.save()
        return redirect("main")

    ONGs = models.ONG.objects.all()
    ONGs_tel = models.TEL_DAS_ONGS.objects.all()
    ONGs_email = models.EMAIL_DAS_ONGS.objects.all()

    listagem = {
        'form_ONG': form_ONG,
        'form_tel_ONG': form_tel_ONG,
        'form_email_ONG': form_email_ONG, 
        'ONG_chave': ONGs,
        'ONG_tel_chave': ONGs_tel,
        'ONG_email_chave': ONGs_email,
    }
    return render(request, "ShowONG.html", listagem)

@login_required(login_url="/login")
def updateONG(request, id_ONG):
    ONG         = models.ONG.objects.get(pk=id_ONG)
    ONGs_tel    = models.TEL_DAS_ONGS.objects.all()
    ONGs_email  = models.EMAIL_DAS_ONGS.objects.all()

    form_ONG        = forms.ONGForm(request.POST or None, instance=ONG)

    if form_ONG.is_valid():
        form_ONG.save()
        redirect("main")

    listagem = {
        'form_ONG': form_ONG,
        'ONG': ONG,
        'ONG_tel_chave': ONGs_tel,
        'ONG_email_chave': ONGs_email,
    }
    return render(request, "ShowONG.html", listagem)

@login_required(login_url="/login")
def deleteONG(request, id_ONG):
    ONG         = models.ONG.objects.get(pk=id_ONG)
    ONG_tel     = models.TEL_DAS_ONGS.objects.get(ton_ong_id=id_ONG)
    ONG_email   = models.EMAIL_DAS_ONGS.objects.get(emo_ong_id=id_ONG)

    ONG_email.delete()
    ONG_tel.delete()
    ONG.delete()
    return redirect("main")

# ===================================================================
# CRUD de telefone
# ===================================================================

@login_required(login_url="/login")
def createTelefone(request, id_ONG):
    ONG = models.ONG.objects.get(pk=id_ONG)
    form = forms.TelONGForm(request.POST or None)
    if form.is_valid():
        ong_tel = form['ton_telefone'].value()
        tel = models.TEL_DAS_ONGS(ton_telefone=ong_tel, ton_ong_id=ONG)
        tel.save()
        return redirect("main")
    Telefone = models.TEL_DAS_ONGS.objects.all()
    listagem = {'form_Telefone': form, 'Telefone_chave': Telefone}
    return render(request, "ShowTelefone.html", listagem)

@login_required(login_url="/login")
def updateTelefone(request, id_telefone, id_ONG):
    Telefone = models.TEL_DAS_ONGS.objects.get(pk=id_telefone)
    form = forms.TelONGForm(request.POST or None, instance=Telefone)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_Telefone': form}
    return render(request, "ShowTelefone.html", listagem)

@login_required(login_url="/login")
def deleteTelefone(request, id_telefone, id_ONG):
    Telefone = models.TEL_DAS_ONGS.objects.get(pk=id_telefone)
    Telefone.delete()
    return redirect("main")

# ===================================================================
# CRUD de email
# ===================================================================

@login_required(login_url="/login")
def createEmail(request, id_ONG):
    ONG = models.ONG.objects.get(pk=id_ONG)
    form = forms.EmailONGForm(request.POST or None)
    if form.is_valid():
        ong_email = form['emo_email'].value()
        email = models.EMAIL_DAS_ONGS(emo_email=ong_email, emo_ong_id=ONG)
        email.save()
        return redirect("main")
    Email = models.EMAIL_DAS_ONGS.objects.all()
    listagem = {'form_Email': form, 'email_chave': Email}
    return render(request, "ShowEmail.html", listagem)

@login_required(login_url="/login")
def updateEmail(request, id_email, id_ONG):
    Email = models.EMAIL_DAS_ONGS.objects.get(pk=id_email)
    form = forms.EmailONGForm(request.POST or None, instance=Email)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_Email': form}
    return render(request, "ShowEmail.html", listagem)

@login_required(login_url="/login")
def deleteEmail(request, id_email, id_ONG):
    Email = models.EMAIL_DAS_ONGS.objects.get(pk=id_email)
    Email.delete()
    return redirect("main")