from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms


def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():

            email = form['email'].value()
            senha = form['senha'].value()

            usuario = auth.authenticate(
                request,
                username=email,
                password=senha
            )

            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, F"{usuario} logado com sucesso!")
                return redirect('index')
            else:
                messages.error(request, "Erro ao tentar logar!")
                return redirect('login')

    return render(request, 'usuarios/login.html', {"form": form})


def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            if form['senha_2'].value() != form['senha_1'].value():
                messages.error(request, "As senhas precisam ser iguais!")
                return redirect('cadastro')

            nome = form['nome_usuario'].value()
            email = form['email'].value()
            senha = form['senha_1'].value()

            if User.objects.filter(username=email):
                messages.error(request, "Usuário já cadastrado!")
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=email,
                password=senha,
                first_name=nome
            )
            usuario.save()

            messages.success(request, "Usuário cadastrado com sucesso!")
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form': form})


def logout(request):
    if auth.get_user(request).is_authenticated:
        auth.logout(request)
        messages.success(request, "Logout efetuado com sucesso!")
    return redirect('login')
