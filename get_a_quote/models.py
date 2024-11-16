from django.db import models

# Create your models here.
class Quote(models.Model):
    city_of_departure = models.CharField(max_length=500)
    delivery_city = models.CharField(max_length=500)
    total_weight = models.FloatField()
    dimension = models.CharField(max_length=500)
    your_name = models.CharField(max_length=500)
    your_email = models.EmailField(max_length=500)
    phone = models.IntegerField()
    message = models.TextField()

    def __str__(self) -> str:
        return self.your_name