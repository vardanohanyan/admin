from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
def home(request):
    return render(request, 'myfirstapp/home.html')


def about(request):
    return render(request, 'myfirstapp/about.html')


def pers(request):
    p1 = Person.objects.get(id=1)
    return render(request, 'myfirstapp/home.html', {'context': p1})