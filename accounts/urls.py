from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import register, profile

urlpatterns = [
    path('register/', register, name='register'),

    # LOGIN (JWT)
    path('login/', TokenObtainPairView.as_view(), name='login'),

    # REFRESH TOKEN
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('profile/', profile, name='profile'),
]
