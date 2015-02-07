from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    #pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.name
    
class ThingsToDo(models.Model):
    city = models.ForeignKey(City)
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name