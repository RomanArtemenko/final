from django.db import models

# Create your models here.

class Article(models.Model):
    avatar = models.URLField()
    name = models.CharField(max_length=512)
    description = models.CharField(max_length=1024)
    keywords = models.CharField(max_length=256)
    url = models.URLField()
    date = models.DateTimeField(auto_now_add=True, blank=True) 

    def __str__(self):
        return self.name

class Period(models.Model):
    begin_time = models.CharField(max_length=5)
    end_time = models.CharField(max_length=5)