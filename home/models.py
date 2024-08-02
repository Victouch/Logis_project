from django.db import models
# from re import search

# Create your models here.

class Search(models.Model):
    searchs = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.searchs