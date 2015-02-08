from django.shortcuts import render
from django.http import HttpResponse
from itineraryapp.models import City

# Create your views here.
def home(request):
    # Do something here
    print("i'm heeeeeeeeeeeeeere")

    return render(request, 'home.html')

def get_itinerary(request):
#     start = request.POST.get('start-date','')
#     end = request.POST.get('end-date','')
#     location = request.POST.get('location','')
#     characteristic = 'adventure'
#    
#     duration = end - start
#     days_duration = duration.days
    
    location = "West Coast_USA"
    characteristic = 'adventure'
   
    days_duration = 14

    relevant_cities = City.objects(region=location, characteristics=characteristic)
    relevant_cities = relevant_cities.order_by('-ranking')

    for city in relevant_cities:
        print(city.title + " " + str(city.characteristics))

    if(days_duration == 14 and characteristic == 'adventure'):
        #we do something here
        print("case 1")
    
    if(days_duration == 14 and characteristic == 'relax'):
        #we do something here
        print("case 2")
    
    if(days_duration == 7 and characteristic == 'adventure'):
        #we do something here
        print("case 3")
    
    
    
    #sort by duration and ranking, then suggest places keeping duration limit 
    result_city_list = relevant_cities
    
    context = {'city_list': result_city_list, 'duration': days_duration}

    return render(request, 'mytrip.html', context)