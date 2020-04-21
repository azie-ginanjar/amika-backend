from django.db import models


# Create your models here.

class Material(models.Model):
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MaterialHistory(models.Model):
    type = models.CharField(max_length=5, null=False)
    source = models.CharField(max_length=25, null=False)
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name="material_histories")
    quantity = models.FloatField(max_length=4, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
