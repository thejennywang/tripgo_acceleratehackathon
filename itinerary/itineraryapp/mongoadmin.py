# Import the MongoAdmin base class
from mongonaut.sites import MongoAdmin

# Import your custom models
from itineraryapp.models import City, ThingsToDo

# # Subclass MongoAdmin and add a customization
class CityAdmin(MongoAdmin):
    search_fields = ('title',)
#     
#     # provide following fields for view in the DocumentListView
    list_fields = ('title', )
 
class ThingsToDoAdmin(MongoAdmin):
    search_fields = ('title',)
     
    list_fields = ('title', )
    

# Instantiate the MongoAdmin class
# Then attach the mongoadmin to your model
City.mongoadmin = MongoAdmin()
ThingsToDo.mongoadmin = MongoAdmin()