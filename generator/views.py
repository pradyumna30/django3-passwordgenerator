from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password' : 'Nopass'})

def password(request):

    characters = list('abcdefghijklmnopqrstuvxwxyz')

    lenght = int(request.GET.get('length', 14))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('$@%^&*()'))

    if request.GET.get('number'):
        characters.extend(list('1234567890'))
    thepassword = ''

    for x in range(lenght):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')

