from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime as dt


from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from location_field.models.spatial import LocationField

Gender=(
    ('Male','Male'),
    ('Female','Female'),
)
# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.location

    class Meta:
        ordering = ['location']


class Post(models.Model):
    caption = models.CharField(max_length=3000)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ImageField(upload_to='posts/')
    likes = models.IntegerField()

    # city = models.CharField(max_length=255)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    # objects = models.GeoManager()

    post_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='profilepics/')
    bio = models.CharField(max_length=350)
    name = models.CharField(max_length=255)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    email= models.EmailField()
    phonenumber = models.IntegerField()
    gender = models.CharField(max_length=15,choices=Gender,default="Male")

    def __str__(self):
        return self.username


class Comment(models.Model):
    comment = models.CharField(max_length=300)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.username
