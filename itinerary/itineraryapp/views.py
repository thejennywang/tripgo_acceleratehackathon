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
   
    days_duration = 14

    adventure_cities = City.objects(region=location, characteristics="adventure").order_by('-ranking')
    relax_cities = City.objects(region=location, characteristics="relax").order_by('-ranking')

    for city in relevant_cities:
        print(city.title + " " + str(city.characteristics))

    if(days_duration == 14):
        #we do something here
        print("case 1")
        sf = City.objects(title="San Francisco")
        big_sur = City.objects(title="Big Sur")
        la = City.objects(title="Los Angeles")
        lv = City.objects(title="Las Vegas")
    
    if(days_duration == 7):
        #we do something here
        print("case 3")
    
    
    
    #sort by duration and ranking, then suggest places keeping duration limit 
    result_city_list = relevant_cities
    
    context = {'itinerary_list': result_itinerary_list, 'duration': days_duration}

    return render(request, 'mytrip.html', context)