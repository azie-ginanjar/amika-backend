from django.db.models import Q
from django.shortcuts import render


# Create your views here.
from rest_framework import generics

from customer.models import Customer
from customer.serializers import CustomerSerializer


class CustomerView(generics.ListCreateAPIView):
    """
        query -- customer name / phone number
    """
    queryset = Customer.objects.all()
    # permission_classes = (AdminRequired, )
    serializer_class = CustomerSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', None)

        queryset = Customer.objects.all()
        if query:
            queryset = queryset.filter(Q(name=query) | Q(phone_number=query))

        return queryset
