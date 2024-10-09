from django.shortcuts import render
from .models import UserAccount
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    context = { 'title': 'My Account' }
    user = UserAccount.objects.get(user=request.user)
    context['user'] = user
    return render(request, 'index.html', context)

def login(request):
    context = { 'title': 'Login' }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            context['success'] = True
        else:
            context['error'] = 'Invalid username or password'
    return render(request, 'login.html', context)
