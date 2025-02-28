from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Simple Signup View
def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']

        # Check if passwords match
        if password != confirm_password:
            messages.warning(request, 'Password Is Not Matching')
            return render(request, 'signup.html')

        # Check if email already exists
        if User.objects.filter(username=email).exists():
            messages.info(request, 'Username is already taken')
            return render(request, 'signup.html')

        # Create user and log them in directly
        user = User.objects.create_user(username=email, email=email, password=password)
        user.is_active = True  # Set the user as active immediately
        user.save()

        # Automatically log the user in
        login(request, user)
        messages.success(request, "Account created successfully, and you are now logged in!")
        return redirect('/')

    return render(request, "signup.html")

# Simple Login View
def handlelogin(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["pass1"]

        # Fetch the user by email
        user = User.objects.filter(email=email).first()
        if user:
            myuser = authenticate(username=user.username, password=password)  # Use the username for authentication
            if myuser:
                login(request, myuser)
                return redirect("/")  # Redirect to the home page (or any other page)

        messages.error(request, "Invalid Credentials")
        return redirect("/auth/login/")

    return render(request, "login.html")

# Logout View
def handlelogout(request):
    logout(request)
    messages.info(request, "Logout Success")
    return redirect('/auth/login/')
