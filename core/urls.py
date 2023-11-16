from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),

    # User Application
    path('api/v1/', include('user_app.urls'), name='user-app'),
]
