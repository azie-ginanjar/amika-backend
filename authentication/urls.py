from django.urls import path

from rest_framework_simplejwt import views as jwt_views

from authentication.views import CustomTokenObtainPairView

app_name = "authentication"
urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh')
]