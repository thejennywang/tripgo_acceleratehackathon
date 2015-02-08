# Import the MongoAdmin base class
from mongonaut.sites import MongoAdmin

# Import your custom models
from itineraryapp.models import City, ThingsToDo

# Subclass MongoAdmin and add a customization
class CityAdmin(MongoAdmin):
    search_fields = ('name',)
    
    # provide following fields for view in the DocumentListView
    list_fields = ('name', "description")

class ThingsToDoAdmin(MongoAdmin):
    search_fields = ('name',)
    
    list_fields = ('name', )
    

# Instantiate the MongoAdmin class
# Then attach the mongoadmin to your model
City.mongoadmin = MongoAdmin()
ThingsToDo.mongoadmin = MongoAdmin()