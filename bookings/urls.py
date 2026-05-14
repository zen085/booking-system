from django.urls import path
from . import views

app_name = 'bookings'
urlpatterns =[
    # book page
    path('api/book/',views.api,name='api'),
    path('booking/<int:service_id>/',views.booking,name='booking'),
    path('save_slot',views.save_slot,name='save_slot'),
    path('auto_form',views.auto_form,name='auto_form'),
    path('time_slots/',views.time_slots,name='time_slots'),
    path('book_service',views.book_form,name='book_service'),
    path('my_bookings',views.my_bookings,name='my_bookings'),
    path('cancel_service/<int:booking_id>/',views.cancel_booking,name='cancel'),
   

]