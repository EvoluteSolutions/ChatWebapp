# chat/views.py
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Profile
from django.utils import timezone
from django.shortcuts import render

def home(request):
    return render(request, 'chat/index.html')


def login_view(request):
    if request.method != 'POST':
        # Handle GET request (show login form)
        return render(request, 'login.html')
    username = request.POST.get('username')
    password = request.POST.get('password')

    # Authenticate user
    user = authenticate(username=username, password=password)

    if user is None:
        # Authentication failed
        return HttpResponse('Invalid login credentials')

    # Log the user in
    login(request, user)
    print("Logged in successfully")
    return render(request,'chat/home.html')

def signup(request):
    if request.method != 'POST':
        return render(request, 'chat/signup.html')
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    # Check if username is already taken
    if User.objects.filter(username=username).exists():
        return render(request, 'signup.html', {'error': 'Username is already taken'})

    # Create the user
    user = User.objects.create_user(username=username, email=email, password=password)

    # Create or update the profile
    profile, created = Profile.objects.get_or_create(user=user)
    profile.created_at = timezone.now()
    profile.save()

    return render(request,'chat/index.html')