from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def my_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('adminAccounts')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'my_login.html')

@login_required
def adminAccounts_view(request):
    return render(request, 'adminAccounts.html')

def logout_view(request):
    logout(request)
    return redirect('login') 

@login_required
def adminPurchaseOrder_view(request):
    return render(request, 'adminPurchaseOrder.html')

@login_required
def adminRequisitionProduct_view(request):
    return render(request, 'adminRequisitionProduct.html')

@login_required
def adminProductListing_view(request):
    return render(request, 'adminProductListing.html')