from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class AmazonData(models.Model):
    title = models.CharField(null=False, max_length=100)
    body  = models.TextField( null=False, max_length=250)
    url = models.CharField(null=False, max_length=1000, default="https://www.amazon.in/")
    image = models.ImageField(null=False, upload_to = "amazon/card" )
    created_on = models.DateTimeField( default=datetime.datetime.now())
    
    def __str__(self):
        return str(self.title)
        
class FlipkartData(models.Model):
    title = models.CharField(null=False, max_length=100)
    body  = models.TextField( null=False, max_length=250)
    url = models.CharField(null=False, max_length=1000, default="https://www.flipkart.com/")
    image = models.ImageField(null=False, upload_to = "flipkart/card")
    created_on = models.DateTimeField( default=datetime.datetime.now())
    
    
    def __str__(self):
        return str(self.title)
        
class SnapdealData(models.Model):
    title = models.CharField(null=False, max_length=250)
    body  = models.TextField( null=False, max_length=250)
    url = models.CharField(null=False, max_length=1000, default="https://www.snapdeal.com/")
    image = models.ImageField(null=False, upload_to = "snapdeal/card")
    created_on = models.DateTimeField( default=datetime.datetime.now())
    
    
    def __str__(self):
        return str(self.title)


# class Pet_list(models.Model):
#     owner = models.CharField(max_length=100)
#     pet_name  = models.CharField(max_length=100)
#     available =  models.CharField(max_length=20)
#     adopt = models.CharField(max_length=10)
#     image = models.ImageField(upload_to = "pet/")
    
#     def __str__(self):
#         return str(self.pet_name)



class ContactDetail(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    email = models.EmailField(null=False, blank=False, max_length=100)
    phone = models.IntegerField(null=False, blank=False, unique=True, max_length=10)
    message = models.CharField(max_length=500)
    
    def __str__(self):
        return str(self.name)