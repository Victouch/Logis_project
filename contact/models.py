from django.db import models
# Create your models here.

class Contact(models.Model):

    your_name = models.CharField(max_length=500)
    your_email = models.EmailField(max_length=500)
    subject = models.CharField(max_length=500)
    message = models.TextField()

    def __str__(self) -> str:
        return self.your_name


