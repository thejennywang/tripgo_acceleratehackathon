from mongoengine import *

# Create your models here.
class City(Document):
    name = StringField(max_length=100)
    description = StringField()
    #pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.name
    
class ThingsToDo():
    city = ReferenceField(City)
    name = StringField(max_length=100)
    
    def __str__(self):
        return self.name