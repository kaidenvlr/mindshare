from django.urls import path

from user_app.views import RegisterAPIView, CustomerAPIView, LoginAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('customers/', CustomerAPIView.as_view(), name='customer-list'),
]