from django.contrib import admin
from .models import Country

# Register your models here.
class CountryAdmin(admin.ModelAdmin):
    list_filter = ['code']
    list_display = ['name', 'code']


admin.site.register(Country, CountryAdmin)
