from django.shortcuts import render
from .models import Page
from forms import UserAccountForm

# Create your views here.

def index(request):
    context = { 'title': 'Home' }
    return render(request, 'index.html', context)

def page(request, slug):
    context = { 'title': slug }
    page = Page.objects.get(slug=slug)
    context['page'] = page
    return render(request, 'page.html', context)

def register(request):
    context = { 'title': 'Register' }
    return render(request, 'register.html', context)