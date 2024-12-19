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
            return redirect('inventoryStocks')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'my_login.html')

@login_required
def home_view(request):
    return render(request, 'home.html')

@login_required
def stocks_view(request):
    return render(request, 'inventoryStocks.html')

@login_required
def inventory_Requisition_view(request):
    return render(request, 'inventoryRequisition.html')

def logout_view(request):
    logout(request)
    return redirect('login') 



