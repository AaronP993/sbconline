from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('login')),  # Redirect root
    path('login/', views.my_login_view, name='login'),  # Login URL
    path('home/', views.home_view, name='home'),  # Home URL after login
    path('logout/', views.logout_view, name='logout'),  # Logout URL (if you have implemented logout)
]
#aaron.pinote
#Chellaxxy69