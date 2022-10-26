from django.shortcuts import render, redirect
from Usuario import models
from django.contrib.auth import authenticate, login as loginSite

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get('username')
        senha = request.POST.get('password')

        user = authenticate(request, username=username, password=senha)  

        if user:
            loginSite(request, user)
            return redirect('main')
        else:
            erro = {'erro': 'Usuário ou Senha INVÁLIDA'}
            return render(request, "login.html", erro)

def cadastro(request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    else:
        username    = request.POST.get('username')
        password    = request.POST.get('password')
        telefone    = request.POST.get('telefone')
        email       = request.POST.get('email')

        user        = models.Usuario.objects.filter(usu_nome=username).first()
        user_email  = models.EMAIL_DOS_USU.objects.filter(ema_email=email).first()

        if user:
            erro = {'erro': 'Usuário ou Senha INVÁLIDA'}
            return render(request, "cadastro.html", erro)

        if user_email:
            erro = {'erro': 'E-mail já está sendo utilizado.'}
            return render(request, "cadastro.html", erro)
        
        user        = models.Usuario.objects.create_user(usu_nome=username, password=password)
        user_email  = models.EMAIL_DOS_USU(ema_email=email,ema_usu_id=user)
        user_tel    = models.TEL_DOS_USU(tel_telefone=telefone, tel_usu_id=user)

        user.save()
        user_email.save()
        user_tel.save()

        return redirect('login')