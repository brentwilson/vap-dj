from django.shortcuts import render
from .models import Page

# Create your views here.

def index(request):
    context = { 'title': 'Home' }
    return render(request, 'index.html', context)

def page(request, slug):
    context = { 'title': slug }
    page = Page.objects.get(slug=slug)
    context['page'] = page
    return render(request, 'page.html', context)