from django.urls import path
from .views import *

urlpatterns = [
    path('', showmain, name='main'),
    path('aboutapp/', aboutapp, name='aboutapp'),
    path('aboutsite/', aboutsite, name='aboutsite'),
    path('aboutdevel/', aboutdevel, name='aboutdevel'),
]