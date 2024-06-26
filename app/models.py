from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    registration = models.DateField(auto_now=True)


class UserCopy(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.IntegerField()
    address = models.TextField()
    status = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    profile_img = models.ImageField(upload_to="user_image")
