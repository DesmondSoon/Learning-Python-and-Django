from django.db import models
from django.urls import reverse


# Create your models here.

class Articles (models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=20)
    active = models.BooleanField(default=True)
    # publish_date = models.DateField()


    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs = {"id":self.id})

class Popsticle (models.Model):
    title = models.CharField(max_length=200)
