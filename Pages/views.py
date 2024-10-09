from django.shortcuts import render
from .models import Page

# Create your views here.

def index(request):
    context = { 'title': 'Home' }
    return render(request, 'index.html', context)

def page(request, slug):
    context = { 'title': slug }
    page_content = Page.objects.get(slug=slug)
    context['page_content'] = page_content
    return render(request, 'contentPage.html', context)

