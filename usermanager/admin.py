from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class UserManager(UserAdmin):
    def get_list_display(self, request):
        return *super(UserManager, self).get_list_display(request), 'role', 'centre'


@admin.register(Centre)
class CentreAdmin(admin.ModelAdmin):
    list_display = ['nom','district','type']


class CentreTabularInline(admin.TabularInline):
    model = Centre
    fields = ['nom','emplacement','longitude','latitude']


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['region', 'nom']
    inlines = [CentreTabularInline]

