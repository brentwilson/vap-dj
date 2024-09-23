from django.shortcuts import render
from .models import Page
from forms import UserAccountForm

# Create your views here.

def index(request):
    context = { 'title': 'Home' }
    return render(request, 'index.html', context)

def page(request, slug):
    context = { 'title': slug }
    page_content = Page.objects.get(slug=slug)
    context['page_content'] = page_content
    return render(request, 'page.html', context)

def register(request):
    context = { 'title': 'Register' }
    if request.method == 'POST':
        form = UserAccountForm(request.POST)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = UserAccountForm()
        context['form'] = form
        
    return render(request, 'register.html', context)