from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def register_view(request):
    form = CreateUserForm()

    if request.method == 'Post':  # S'il s'agit d'une requête POST
        form = CreateUserForm(request.Post)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)
            return redirect("login_url")

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def login_url(request):
    if request.method == 'Post':
        username = request.Post.get('username')
        password = request.Post.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('shop')

    context = {}
    return render(request, 'registration/login.html', context)




