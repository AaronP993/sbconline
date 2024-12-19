from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('login')),  # Redirect root to login page
    path('login/', views.my_login_view, name='login'),  # Login URL
    path('home/', views.home_view, name='home'),  # Home URL after login
    path('logout/', views.logout_view, name='logout'),  # Logout URL
    path('create-account/', views.create_account_view, name='create_account'),  # Account creation URL
    path('success/', views.success_view, name='success'),  # Redirect to success after account creation
]
