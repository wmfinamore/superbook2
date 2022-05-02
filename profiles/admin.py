from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile
from django.contrib.auth.models import User


class UserProfileInLine(admin.StackedInline):
    model = Profile


class NewUserAdmin(UserAdmin):
    inlines = [UserProfileInLine]


admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)
