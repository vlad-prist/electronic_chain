from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin:
    list_display = ('id', 'username', 'email', 'is_staff',)
    list_filter = ('username', 'email', 'is_staff',)
    search_fields = ('username', 'email',)

