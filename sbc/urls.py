from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('login')),  # Redirect root
    path('login/', views.my_login_view, name='login'),  # Login URL
    path('adminAccounts/', views.adminAccounts_view, name='adminAccounts'),  # Home URL after login
    path('logout/', views.logout_view, name='logout'),  # Logout URL (if you have implemented logout)
    path('adminPurchaseOrder', views.adminPurchaseOrder_view, name='adminPurchaseOrder'),
    path('adminRequisitionProduct', views.adminRequisitionProduct_view, name='adminRequisitionProduct'),
    path('adminProductListing', views.adminProductListing_view, name='adminProductListing'),
    path('adminCreateAccount', views.adminCreateAccount_view, name='adminCreateAccount'),
    
]
#aaron.pinote
#Chellaxxy69