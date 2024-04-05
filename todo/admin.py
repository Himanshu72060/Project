from django.contrib import admin
from .models import FirstTodo

# Register your models here.


@admin.register(FirstTodo)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description',
                    'status', 'deadline', 'created_at']
