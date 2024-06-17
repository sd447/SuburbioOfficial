from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Event, User
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt

def index(request):
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})

def cadastrarevento(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')  # Acesse a imagem enviada
        date = request.POST.get('date')

        event = Event(
            title=title,
            description=description,
            image=Event.convert_image_to_base64(image),  # Atribua a imagem ao campo image
            date=date
        )
        event.save()  # Salve a instância do modelo no banco de dados

        return redirect('index')  # Redirecione para a página de índice

    events = Event.objects.all()
    return render(request, 'cadastrarEvento.html', {'events': events})


@csrf_exempt
def cadastro(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        print(request.POST)

        # Verifique se a senha e a confirmação da senha são iguais
        if password == confirm_password:
            # Crie um hash da senha
            password = make_password(password)

            user = User(
                name=name,
                lastname=lastname,
                username=username,
                password=password
            )
            user.save()  # Salve a instância do modelo no banco de dados

            login(request, user)  # Faça login no usuário

            return redirect('index')  # Redirecione para a página de índice
        else:
            # As senhas não correspondem
            return render(request, 'cadastro.html', {'error': 'As senhas não correspondem'})

    return render(request, 'cadastro.html')


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        form = User(request.POST)
        if form.is_valid():
            username = form.username.get('username')
            password = form.password.get('password')
            user = authenticate(username=username, password=password)  # Autentica o usuário
            if user is not None:
                login(request, user)  # Faz login do usuário
                return redirect('home')  # Redireciona para a página inicial
            else:
                return HttpResponse("Invalid login details.")  # Mensagem de erro de login inválido
    else:
        form = User()
    return render(request, 'login.html', {'form': form})