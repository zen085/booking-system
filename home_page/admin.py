from django.contrib import admin
from .models import Service


# Register your models here.

@admin.register(Service)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id","name","description",)
    

    