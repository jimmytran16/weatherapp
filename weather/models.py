from django.db import models

# Create your models here.

# NEED TO FINISH 
class WeatherForecast(models.Model):
    weather = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
