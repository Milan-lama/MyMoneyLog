from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('login/', views.login_api, name='login_api'),
    path('register/', views.register_api, name='register_api'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]