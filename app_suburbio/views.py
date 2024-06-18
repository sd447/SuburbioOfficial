from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Event, User
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def index(request):
    if request.user.is_authenticated:
        return redirect('index_logged_in')
    else:
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
        print(request.POST)

        if password == confirm_password:
            password = make_password(password)

            user = User(
                name=name,
                lastname=lastname,
                username=username,
                password=password
            )
            user.save()

            login(request, user)

            return redirect('index')
        else:
            # As senhas não correspondem
            return render(request, 'cadastro.html', {'error': 'As senhas não correspondem'})

    return render(request, 'cadastro.html')


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)  # Autentica o usuário
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse("Invalid login details.")
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('index')
