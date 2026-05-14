from django.contrib import admin
from .models import UserProfile


# Register your models here.

@admin.register(UserProfile)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id","user","notify_via_email","created_at",)
    list_filter = ("user",)

    