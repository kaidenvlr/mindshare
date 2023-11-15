from django.contrib import admin

from user_app.models import Customer


@admin.register(Customer)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'is_verified']
    list_filter = ['is_verified']
    search_fields = ['user']
    ordering = ['id']
