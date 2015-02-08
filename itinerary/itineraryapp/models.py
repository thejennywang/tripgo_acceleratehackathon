from mongoengine import *

# Create your models here.
class City(Document):
    title = StringField(max_length=100)
    description = StringField(max_length=400)
    region = StringField(max_length=400)
    minimum_stay_duration = IntField(max_value=10)
    ranking = IntField(min_value =0, max_value=10)
    image_url = StringField(max_length=400)
    characteristics = ListField(StringField(max_length=30))
    
    def __str__(self):
        return self.title
     
    def __unicode__(self):
        return self.title
    
class ThingsToDo(Document):
    city = ReferenceField(City)
    title = StringField(max_length=400)
    description = StringField(max_length=400)
    image_url = StringField(max_length=400)
    characteristics = ListField(StringField(max_length=30))
  
    #active_hours = IntField
    #cost = IntField
    #suggestions = StringField(max_length=400)
    
    def __str__(self):
        return self.title
    
    def __unicode__(self):
        return self.title