from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff',)
    list_filter = ('email', 'is_staff',)
    search_fields = ('username', 'email',)
