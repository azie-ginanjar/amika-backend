from django.urls import path

from material.views import MaterialCreate, StockIn

app_name = "material"
urlpatterns = [
    path("", view=MaterialCreate.as_view(), name="material-create-list"),
    path("stockin", view=StockIn.as_view(), name='material-stock-in'),
]