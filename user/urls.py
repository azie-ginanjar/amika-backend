from django.urls import path

from user.views import UserView, UserDetailsView, UserRegister

app_name = "user"
urlpatterns = [
    path("", view=UserView.as_view(), name="user-list"),
    path("register/", view=UserRegister.as_view(), name="user-register"),
    path('<str:pk>/', view=UserDetailsView.as_view(), name='user-details-update-delete')
]