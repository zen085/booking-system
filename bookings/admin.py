from django.contrib import admin
from .models import Order
from notifications.services import confirmed_order


# Register your models here.

@admin.register(Order)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id","user","email","phone","service","time","date","notes","created_at","status")
    list_filter = ("user","service","date","email","phone","time","status")
    list_editable = ("status",)

    def save_model(self, request, obj, form, change):

        status_change = False

        if change:
            old_obj = Order.objects.get(pk=obj.pk)
            status_change = (old_obj.status != "CONFIRMED" and obj.status == "CONFIRMED")

        super().save_model(request, obj, form, change)

        if change and status_change:
            confirmed_order(obj)