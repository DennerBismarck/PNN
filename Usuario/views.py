from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from Usuario import models, forms
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
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = models.Usuario.objects.filter(usu_nome=username).first()

        if user:
            erro = {'erro': 'Usuário ou Senha INVÁLIDA'}
            return render(request, "cadastro.html", erro)
        
        user = models.Usuario.objects.create_user(usu_nome=username, password=password)
        user.save()

        return redirect('login')