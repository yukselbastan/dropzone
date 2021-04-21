from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField
from autoslug import AutoSlugField
from django.urls import reverse
from .choices import (
    COUNTRY,
    CITY,
    CAT1,
    CAT2,
    CAT3,
    TOU,
    )

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='user', always_update=True, unique=True)
    image = models.ImageField(upload_to='posts/profile_img/%Y/%m/%d', blank=True, null=True)
    name = models.CharField(max_length=25, default='YourName')
    surname = models.CharField(max_length=25, default='YourSurname')
    email = models.EmailField(max_length=70, blank=True)
    birthday = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)
    mobil = models.CharField(max_length=11, default=0)
    phone = models.CharField(max_length=11, default=0)
    fax = models.CharField(max_length=11, default=0)
    webpage = models.CharField(max_length=100, default='your_www')
    country = models.CharField(choices=COUNTRY, max_length=7)
    city = models.CharField(choices=CITY, max_length=6)
    bio = models.TextField(default='YourBio')
    balance = models.IntegerField(default=0) 
    points = models.IntegerField(default=0)
    vip = models.BooleanField(default=False)
    reference = models.CharField(max_length=40, default=0, blank=True, null=True)
    type_of_user = models.CharField(choices=TOU, max_length=8, default='Standart')

    def __str__(self):
        return str(self.user.username  + ' - ' + self.name  + ' ' + self.surname)


class Post(models.Model):

    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='title', always_update=True, unique=True)
    post_create = models.DateField(auto_now_add=True)
    post_update = models.DateField(auto_now=True)
    notes = models.CharField(max_length=100, blank=True, null=True)
    category_1 = models.CharField(choices=CAT1, max_length=4)
    category_2 = models.CharField(choices=CAT2, max_length=10)
    category_3 = models.CharField(choices=CAT3, max_length=13)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    title_bold = models.BooleanField(default=False)
    title_colored = models.BooleanField(default=False)
    border = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)
    keywords = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return str(self.title)[:30]
