from django.urls import path

from customer.views import CustomerView

app_name = "customer"
urlpatterns = [
    path("", view=CustomerView.as_view(), name="customer-create-list"),
]