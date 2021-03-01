from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.


def main(request):
    context = {}
    return render(request, 'tracker/main.html', context)


def account(request):
    context = {}
    return render(request, 'tracker/account.html', context)


def register(request):
    if request.method == 'POST':
        if 'signup' in request.POST:
            first_name = request.POST['firstname']
            last_name = request.POST['lastname']
            username = request.POST['username']
            password = request.POST['password']

            if not first_name or not last_name or not username or not password:
                print("empty field")
            elif User.objects.filter(username=username).exists():
                print("user exist")
            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, password=password,)
                user.save()
                print("User created")
                return redirect('account')
            return redirect('main')
        elif 'login' in request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(
                request, username=username, password=password)
            if not username or not password:
                print("empty field")
            elif user is not None:
                auth.login(request, user)
                print("successfull login")
                return redirect('account')
            else:
                print('invalid username or password')
    return redirect('main')


@login_required
def logout(request):
    django_logout(request)
    return redirect('main')