from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from material.models import Material, MaterialHistory
from material.serializers import MaterialSerializer, MaterialHistorySerializer


class MaterialCreate(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    # permission_classes = (AdminRequired, )
    serializer_class = MaterialSerializer


class StockIn(generics.CreateAPIView):
    queryset = MaterialHistory.objects.all()
    # permission_classes = (AdminRequired, )
    serializer_class = MaterialHistorySerializer
