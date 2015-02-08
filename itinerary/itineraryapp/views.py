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

def getitinerary(request):
    start = request.POST.get('start-date','')
    end = request.POST.get('end-date','')
    location = request.POST.get('location','')
    characteristic = 'adventure'
   
    duration = end - start
    days_duration = duration.days
    
    relevant_cities = City.objects(region=location, characteristic = characteristic).sort('-ranking','-stay_duration')

    #sort by duration and ranking, then suggest places keeping duration limit 
    result_city_list = relevant_cities
    
    context = {'city_list': result_city_list, 'duration': days_duration}

    return render(request, 'mytrip.html', context)