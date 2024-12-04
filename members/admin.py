from django.contrib import admin
from .models import RegisterUser

# Register your models here.
# @admin.register(RegisterUser)
# class RegisterUserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'email', 'username', 'password')
#     list_display_links = ('id', 'name')
#     search_fields = ('name', 'email', 'username')
#     list_per_page = 10

admin.site.register(RegisterUser)