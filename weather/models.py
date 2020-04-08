from django.db import models

# Create your models here.

# NEED TO FINISH
class WeatherForecast(models.Model):
    weather = models.CharField(max_length=100) #initialize the fields that corresponds to the database
    img = models.ImageField(blank=True,null=True)

    def __str__(self):
        return f'{self.weather},{self.img}'
