from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Shop


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['email', 'username', 'haveshop']
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Shop)