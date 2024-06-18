from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Event, User
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def index(request):
    if request.user.is_authenticated:
        return redirect('index_logged_in')
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})


@login_required
def index_logged_in(request):
    events = Event.objects.all()
    return render(request, 'index_logged_in.html', {'events': events})


@login_required
def cadastrarevento(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        date = request.POST.get('date')

        event = Event(
            title=title,
            description=description,
            image=Event.convert_image_to_base64(image),
            date=date
        )
        event.save()

        return redirect('index')

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

        # Verificar se o nome de usuário já existe
        if AuthUser.objects.filter(username=username).exists():
            return render(request, 'cadastro.html', {'error': 'O nome de usuário já existe'})

        if password == confirm_password:
            user = AuthUser.objects.create_user(username=username, password=password, first_name=name, last_name=lastname)
            user.save()

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse("Invalid login details.")
        else:
            # As senhas não correspondem
            return render(request, 'cadastro.html', {'error': 'As senhas não correspondem'})

    return render(request, 'cadastro.html')


@csrf_exempt
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                return redirect('index_logged_in')  # Redirecionar para 'index_logged_in' após o login
            except Exception as e:
                return HttpResponse(f"Error during redirection: {e}")
        else:
            return HttpResponse("Invalid login details.")
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('index')
