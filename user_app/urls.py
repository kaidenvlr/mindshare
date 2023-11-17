from django.urls import path

from user_app.views import RegisterAPIView, CustomerViewSet, LoginAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('customers/', CustomerViewSet.as_view({'get': 'list'}), name='customer-list'),
    path('customer/<int:pk>/', CustomerViewSet.as_view({'get': 'retrieve'}), name='customer-retrieve'),
    path('follow/<int:pk>/', CustomerViewSet.as_view({'post': 'create'}), name='customer-follow'),
]
