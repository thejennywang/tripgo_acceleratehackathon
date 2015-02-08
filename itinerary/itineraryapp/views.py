from django.shortcuts import render
from django.http import HttpResponse
from itineraryapp.models import City

# Create your views here.
def home(request):
    # Do something here
    print("i'm heeeeeeeeeeeeeere")
    
    new_city = City(name='San Francisco', description='Beautiful fun city')
    new_city.save()

    return render(request, 'home.html')