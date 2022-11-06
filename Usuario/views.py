from django.shortcuts import render, redirect
from Usuario import models, forms
from Aplicativo import views
from django.contrib.auth import authenticate, login as loginSite, logout as desconectar

# ===================================================================
# Sistema de Login
# ===================================================================

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get('username')
        senha    = request.POST.get('password')

        user = authenticate(request, username=username, password=senha)  

        if user:
            loginSite(request, user)
            return redirect('main')
        else:
            erro = {'erro': 'Usuário ou Senha INVÁLIDA'}
            return render(request, "login.html", erro)

def logout(request):
    desconectar(request)
    return views.index(request)

def cadastro(request):
    if request.method == "GET":
        return render(request, "register.html")
    else:
        username    = request.POST.get('username')
        password    = request.POST.get('password')
        telefone    = request.POST.get('telefone')
        email       = request.POST.get('email')

        user        = models.Usuario.objects.filter(usu_nome=username).first()
        user_email  = models.EMAIL_DOS_USU.objects.filter(ema_email=email).first()

        if user:
            erro = {'erro': 'Usuário ou Senha INVÁLIDA'}
            return render(request, "register.html", erro)

        if user_email:
            erro = {'erro': 'E-mail já está sendo utilizado.'}
            return render(request, "register.html", erro)
        
        user        = models.Usuario.objects.create_user(usu_nome=username, password=password)
        user_email  = models.EMAIL_DOS_USU(ema_email=email,ema_usu_id=user)
        user_tel    = models.TEL_DOS_USU(tel_telefone=telefone, tel_usu_id=user)

        user.save()
        user_email.save()
        user_tel.save()

        return redirect('login')

# ===================================================================
# Verificação de Usuário
# ===================================================================

def user_is_authenticated(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
    return user

def user(request):
    user = user_is_authenticated(request)
    if user:
        userTel     = models.TEL_DOS_USU.objects.all()
        userEmail   = models.EMAIL_DOS_USU.objects.all()
        listagem    = {
            'user': user, 
            'user_tel': userTel, 
            'user_email': userEmail
        }
        return render(request, 'user.html', listagem)
    else:
        return render(request, 'index.html')

# ===================================================================
# CRUD de TELEFONE dos Usuários
# ===================================================================

def createTelefone(request):
    user = models.Usuario.objects.get(pk=user_is_authenticated(request).usu_id)
    form = forms.TelUserForm(request.POST or None)
    if form.is_valid():
        user_tel = form['tel_telefone'].value()
        tel = models.TEL_DOS_USU(tel_telefone=user_tel, tel_usu_id=user)
        tel.save()
        return redirect("main")
    Telefone = models.TEL_DOS_USU.objects.all()
    listagem = {'form_Telefone': form, 'Telefone_chave': Telefone}
    return render(request, "ShowTelefone.html", listagem)

def updateTelefone(request, id_telefone):
    Telefone = models.TEL_DOS_USU.objects.get(pk=id_telefone)
    form = forms.TelUserForm(request.POST or None, instance=Telefone)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_Telefone': form}
    return render(request, "ShowTelefone.html", listagem)

def deleteTelefone(request, id_telefone):
    Telefone = models.TEL_DOS_USU.objects.get(pk=id_telefone)
    Telefone.delete()
    return redirect("main")

# ===================================================================
# CRUD de EMAIL dos Usuários
# ===================================================================

def createEmail(request):
    user = models.Usuario.objects.get(pk=user_is_authenticated(request).usu_id)
    form = forms.EmailUserForm(request.POST or None)
    if form.is_valid():
        user_email = form['ema_email'].value()
        email = models.EMAIL_DOS_USU(ema_email=user_email, ema_usu_id=user)
        email.save()
        return redirect("main")
    Email = models.EMAIL_DOS_USU.objects.all()
    listagem = {'form_Email': form, 'Email_chave': Email}
    return render(request, "ShowEmail.html", listagem)

def updateEmail(request, id_email):
    Email = models.EMAIL_DOS_USU.objects.get(pk=id_email)
    form = forms.EmailUserForm(request.POST or None, instance=Email)
    if form.is_valid():
        form.save()
        return redirect("main")
    listagem = {'form_Email': form}
    return render(request, "ShowEmail.html", listagem)

def deleteEmail(request, id_email):
    Email = models.EMAIL_DOS_USU.objects.get(pk=id_email)
    Email.delete()
    return redirect("main")