from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('login')),  # Redirect root
    path('login/', views.my_login_view, name='login'),  # Login URL
    path('home/', views.home_view, name='home'),  # Home URL after login
    path('logout/', views.logout_view, name='logout'),  # Logout URL (if you have implemented logout)

    path('inventoryRequisition/', views.inventory_Requisition_view, name='inventoryRequisition'),
    path('inventoryStocks/', views.stocks_view, name='inventoryStocks'),
]
#aaron.pinote
#Chellaxxy69