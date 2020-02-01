from django.urls import path
from rango import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'about/', views.about, name='about'),
]