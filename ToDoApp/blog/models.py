from django.db import models



# Create your models here.

class Articles (models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=20)
    active = models.BooleanField(default=True)
    # publish_date = models.DateField()
