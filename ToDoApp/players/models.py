from django.db import models
from django.urls import reverse



# Create your models here.
class players(models.Model):
    name = models.CharField(max_length=200)
    player_div = models.IntegerField()
    player_club = models.CharField(max_length=100)


    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return f"/players/{self.id}/"

    def get_absolute_url(self):
        return reverse("players:player-view", kwargs = {"player_id":self.id})
