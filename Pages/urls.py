from django.urls import path
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('page/<slug:slug>/', views.page, name='page'),
    path('register/', views.register, name='register'),
] 