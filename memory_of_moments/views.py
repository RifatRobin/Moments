from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import moments
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'successfully loged in')
            return redirect('home')
        else:
            messages.error(request, 'invalid credential')
            return redirect("/")
    else:
        messages.error(request, "invalid Credential !!")
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "take another username")
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.error(request, "email already exists")
                return redirect('register')

            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                                username=username, email=email, password=password1)
                user.save()

        else:
            messages.error(request, "password Not macthed")
            return redirect('register')
        messages.success(request, "Registration completed Successfully")
        return redirect('/')

    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    messages.info(request, "Loged out from the site")
    return redirect("/")


@login_required(login_url='login')
def add(request):
    if request.method == 'POST':
        mmnts = request.POST.get('mmnts', '')
        memory = moments(contents=mmnts, user=request.user)
        memory.save()
        messages.success(request, "Your moment saved successfully")
        return redirect('home')
    else:
        return render(request, "add_memory.html")


@login_required(login_url='login')
def home(request):
    log_user = request.user
    m = moments.objects.filter(user=log_user)
    return render(request, "view_memory.html", {'m': m})


@login_required(login_url='login')
def delete(request):
    return render(request, "delete_memory.html")
