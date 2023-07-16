from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from users.forms import UserCreationForm, UserChangeForm
from users.models import User


# User register view
def user_register(request):
    # GET method
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'user_register.html', {'form': form})
    
    # POST method
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        # If form is valid, return to home
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('home')
        
        # Else, keep on this page
        else:
            messages.error(request, 'Erro ao criar o usuário! Verifique se todos os campos foram preenchidos corretamente.')


# Login view
def user_login(request):
    # GET method
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    
    # POST method
    elif request.method == 'POST':
        # Get user
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        # If user is not none, login user
        if user is not None:
            login(request, user)
            if request.GET.get('next') is not None:
                return redirect(request.GET.get('next'))
            return redirect('home')
        

# Logout view
def user_logout(request):
    logout(request)
    return redirect('home')


# Edit profile
@login_required(login_url='login')
def user_update(request):
    if request.method == 'GET':
        form = UserChangeForm(instance=request.user)
        return render(request, 'user_update.html', {'form': form})
