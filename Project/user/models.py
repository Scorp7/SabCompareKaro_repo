from django.db import models

# Create your models here.
# class AmazonDiscountedProducts(models.Model):
#     image = 


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
    phone = models.CharField(null=False, blank=False, unique=True, max_length=10)
    message = models.CharField(max_length=500)
    
    def __str__(self):
        return str(self.name)