from django.shortcuts import render
from django.http import HttpResponse
from itineraryapp.models import City, ThingsToDo
import itinerary

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

#     adventure_cities = City.objects(region=location, characteristics="adventure").order_by('-ranking')
#  
#     for city in adventure_cities:
#         print(city.title + " " + str(city.characteristics))


    sf = City.objects(title="San Francisco").first()
    big_sur = City.objects(title="Big Sur").first()
    la = City.objects(title="Los Angeles").first()
    lv = City.objects(title="Las Vegas").first()
    gc = City.objects(title="Grand Canyon National Park").first()
    
    sb = City.objects(title="Santa Barbara").first()
    sm = City.objects(title="Santa Monica").first()
    sd = City.objects(title="San Diego").first()

    sf.duration = 4
    big_sur.duration = 1
    la.duration = 3
    lv.duration = 3
    gc.duration = 3
    
    sb.duration = 5
    sm.duration = 4
    sd.duration = 5

    sf.activities = ThingsToDo.objects(city=sf.id)
    big_sur.activities = ThingsToDo.objects(city=big_sur.id)
    la.activities = ThingsToDo.objects(city=la.id)
    lv.activities = ThingsToDo.objects(city=lv.id)
    gc.activities = ThingsToDo.objects(city=gc.id)
    
    sb.activities = ThingsToDo.objects(city=sb.id)
    sm.activities = ThingsToDo.objects(city=sm.id)
    sd.activities = ThingsToDo.objects(city=sd.id)

    adventure_cities = [sf, big_sur, la, lv, gc]
    relax_cities = [sb, sm, sd]
    
    if(days_duration == 7):
        sf.duration = 3
        big_sur.duration = 1
        la.duration = 3
        adventure_cities = [sf, big_sur, la]
        
        sb.duration = 5
        sm.duration = 2
        relax_cities = [sb, sm]
    
    #sort by duration and ranking, then suggest places keeping duration limit 
    itinerary_list = [adventure_cities, relax_cities]
    context = {'itinerary_list': itinerary_list, 'duration': days_duration}

    return render(request, 'mytrip.html', context)