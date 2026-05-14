from django.urls import path
from . import views

app_name = 'home_page'
urlpatterns =[
    # home page
    # path('home/',views.home,name='page'),
    path('',views.home_page,name='home')

]