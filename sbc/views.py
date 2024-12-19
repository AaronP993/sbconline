from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect

# Login view
def my_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'my_login.html')

# Home view (requires login)
@login_required
def home_view(request):
    return render(request, 'home.html')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login') 

# Success view (after successful account creation)
def success_view(request):
    return render(request, 'createaccount.html')

# Create Account view
def create_account_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different one.')
            return redirect('create_account')  # Redirect back to the create account page to try again

        # Create the new user
        hashed_password = make_password(password)  # Hash the password before saving
        user = User.objects.create(username=username, password=hashed_password)
        
        # You might want to assign the role as well if you're using custom user roles.
        # You can add code to set the user's role here, depending on your model setup.

        # Optionally, you can create a success message after the account is created
        messages.success(request, 'Account created successfully! You can now log in.')

        # Redirect to the login page after successful account creation
        return redirect('login')

    return render(request, 'createaccount.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        # Validation logic here

        # After successful account creation
        messages.success(request, 'Account created successfully! You can now log in.')
        return redirect('login')  # Redirect to login page
