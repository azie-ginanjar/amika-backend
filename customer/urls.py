from django.urls import path

from customer.views import CustomerCreate, CustomerList, CustomerDetails

app_name = "customer"
urlpatterns = [
    path("", view=CustomerCreate.as_view(), name="customer-create-list"),
    path("<str:query>/list", view=CustomerList.as_view(), name='customer-list-filter'),
    path("<int:pk>", view=CustomerDetails.as_view(), name='customer-update-details'),
]