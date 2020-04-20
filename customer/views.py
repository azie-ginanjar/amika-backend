from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from customer.models import Customer
from customer.serializers import CustomerSerializer


class CustomerCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    # permission_classes = (AdminRequired, )
    serializer_class = CustomerSerializer


class CustomerList(generics.ListAPIView):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        query = self.kwargs['query']

        return Customer.objects.filter(Q(name=query) | Q(phone_number=query))


class CustomerDetails(generics.RetrieveUpdateAPIView):
    queryset = Customer.objects.all()
    # permission_classes = (AdminRequired, )
    serializer_class = CustomerSerializer
