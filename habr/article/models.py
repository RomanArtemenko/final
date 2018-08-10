from django.db import models

# Create your models here.

class Article(models.Model):
    avatar = models.URLField()
    name = models.CharField(max_length=512)
    description = models.CharField(max_length=1024)
    keywords = models.CharField(max_length=256)
    url = models.URLField()

    
