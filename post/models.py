from django.db import models

# Create your models here.
class Post(models.Model):
    body = models.TextField(max_length=500) #Char chara

    def __str__(self):
        return self.body[:50]