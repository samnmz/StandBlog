from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Account Register
def user_register(request):
    if request.user.is_authenticated:
        return redirect('home:home')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        user = User.objects.create(email=email, username=username, password=password)
        login(request, user)
        return redirect('home:home')
    return render(request, 'account/register.html')

# Account Login
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home:home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
    return render(request, 'account/login.html')

# Account Logout
def user_logout(request):
    logout(request)
    return redirect('home:home')