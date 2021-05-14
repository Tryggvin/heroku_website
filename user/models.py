from django.db import models
from  django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileImage = models.CharField(max_length=9999)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)



class SearchHistory(models.Model):
    url = models.URLField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)