from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<slug:slug>/', views.product, name='product'),
    path('products/<str:category>', views.productsByCategory, name='productsByCategory'),
]
