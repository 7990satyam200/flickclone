from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    """
    Model representing a User Profile by extending User Model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    website = models.URLField(blank= True)
    picture = models.ImageField(upload_to='profile_image', blank=True)
    def __str__(self):
        return self.user.username


class Our_User(models.Model):
    """
    Model representing a User Profile by extending User Model
    """
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    address = models.TextField(max_length=500, blank=True)
    city = models.CharField(max_length = 50, blank = True)
    picture = models.ImageField(upload_to='profile_image', blank=True)
    user_types =[
    ('FARMER', 'FARMER'),
    ('WHOLESELLER', 'WHOLESELLER')]
    user_type = models.CharField(
    max_length = 20,
    choices = user_types,
    default = 'FARMER',
    blank = True
    )
    def __str__(self):
        return self.address
