from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import Ad
from .forms import AdForm

User = get_user_model()

# Home Page
def home_view(request):
    query = request.GET.get('q')
    ads = Ad.objects.all()
    if query:
        ads = ads.filter(title__icontains=query)
    return render(request, 'homenix/home.html', {'ads': ads})

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']  # Actually email
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'homenix/login.html')

# Register View
def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('register')
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, "Registration successful! You can now log in.")
        return redirect('login')

    return render(request, 'homenix/register.html')

# Logout View
def logout_view(request):
    logout(request)
    return redirect('home')

# Post Ad View
@login_required
def post_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user
            ad.save()
            messages.success(request, "Ad posted successfully.")
            return redirect('home')
    else:
        form = AdForm()
    return render(request, 'homenix/post_ad.html', {'form': form})

# Delete Ad View
@login_required
def delete_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id, user=request.user)
    ad.delete()
    messages.success(request, "Ad deleted successfully.")
    return redirect('home')

# About Page
def about_view(request):
    return render(request, 'homenix/about.html')

# Properties Page
def properties_view(request):
    return render(request, 'homenix/properties.html')
