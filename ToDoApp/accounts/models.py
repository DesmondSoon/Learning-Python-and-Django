from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class accounts (models.Model):
    name = models.CharField(max_length=20)


class UserProfile (models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default='')
    description = models.CharField(max_length=200, default='')
    website = models.URLField(default='')
    phone_number = models.IntegerField(default=0)

def __str__(self):
    return self.user


def create_profile(sender,**kwargs):

    if kwargs ['created']:
            user_profile= UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
