from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255, null=False)
    phone_number = models.CharField(max_length=30, null=False)
    province = models.CharField(max_length=25, null=False)
    city = models.CharField(max_length=25, null=False)
    districts = models.CharField(max_length=35, null=False)
    zip_code = models.CharField(max_length=10, null=False)
    address = models.TextField(null=False)
