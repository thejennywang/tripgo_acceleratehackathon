from django.shortcuts import render
from django.http import HttpResponse
from models import City

# Create your views here.
def home(request):
    # Do something here

    new_city = (name='San Francisco', description='Beautiful fun city')
    new_city.save()

    return render(request, 'home.html')