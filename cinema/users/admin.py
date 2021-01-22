"""User models admin"""

#django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#Models
from cinema.users.models import User

class CustomUserAdmin(UserAdmin):
    """
    User model admin
    """
    list_display = ('email', 'username', 'first_name' , 'last_name', 'is_staff')
    list_filter = ('is_admin', 'is_staff', 'created', 'modified')
    search_fields = ('username', 'first_name','last_name')


    actions = ['make_admin']

    def make_admin(self, request, queryset):
        """makes a user admin"""
        queryset.update(is_staff=True)
    make_admin.short_description = 'Makeing a user Admin'

admin.site.register(User, CustomUserAdmin)