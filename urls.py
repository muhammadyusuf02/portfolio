from unicodedata import category, name
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/<slug:slug>/', views.about, name='about')
]
