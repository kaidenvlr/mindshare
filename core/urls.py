from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views

urlpatterns = [
    # DRF Token
    path('api-token-auth/', views.obtain_auth_token),

    # Admin Panel
    path('admin/', admin.site.urls),
]
