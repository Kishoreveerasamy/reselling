from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib import messages



def home_view(request):
    ads = Ad.objects.all()
    return render(request, 'Homenix/home.html', {'ads': ads})


def login_view(request):
    if request.method == 'POST':
        email = request.POST['username']  # form field is still "username"
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'Homenix/login.html')


def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists. Please use a different one.")
            return redirect('register')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1
            )
            user.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Something went wrong: {e}")
            return redirect('register')

    return render(request, 'Homenix/register.html')




from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()
from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib import messages
from django.shortcuts import render, redirect

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

      
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        user.save()
        messages.success(request, "Registration successful! You can now log in.")
        return redirect('login')

    return render(request, 'Homenix/register.html')  





from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AdForm
from .models import Ad

@login_required
def post_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user
            ad.save()
            return redirect('home')  
    else:
        form = AdForm()
    return render(request, 'Homenix/post_ad.html', {'form': form})

@login_required
def delete_ad(request, ad_id):
    ad = Ad.objects.get(id=ad_id)
    if ad.user == request.user:
        ad.delete()
    return redirect('home')




from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'Homenix/login.html')

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

      
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        user.save()
        messages.success(request, "Registration successful! You can now log in.")
        return redirect('login')

    return render(request, 'Homenix/register.html') 



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'Homenix/login.html')

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('home')

from django.shortcuts import render
from .models import Ad

def home_view(request):
    ads = Ad.objects.all().order_by('-id')  
    return render(request, 'Homenix/home.html', {'ads': ads})