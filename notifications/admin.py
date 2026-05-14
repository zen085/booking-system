from django.contrib import admin
from .models import Notifications


# Register your models here.

@admin.register(Notifications)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id","notifications_type","recipient","recipient_email","message","order","created_at","status")
    list_filter = ("notifications_type","status")
    list_editable = ('notifications_type',)
    