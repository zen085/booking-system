from django.urls import path
from django.contrib.auth.views import LogoutView,LoginView
from . import views

app_name = 'users'
urlpatterns =[
    # book page
    path('Signup/',views.register,name='Sign_up'),
    path('login/',LoginView.as_view(next_page='home_page:home'),name='login'),
    path('logout/',LogoutView.as_view(next_page='home_page:home'),name='logout')
    
   

]