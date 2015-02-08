#from django.db import models
from mongoengine import *

# Create your models here.
class City():
    name = StringField(max_length=100, required=True)
    description = StringField(max_length=400)

    tags = ListField(StringField(max_length=30))
    #pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.name
    
#class ThingsToDo(models.Model):
 #   city = ReferenceField(City)
  #  name = models.CharField(max_length=100)
   # description = models.TextField()
    
    #def __str__(self):
     #   return self.name