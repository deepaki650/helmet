from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, 'cars.html')


def register(request):
    if request.method == 'post':
        username = request.post["username"]
        first_name = request.post["first_name"]
        last_name = request.post["last_name"]
        email = request.post["email"]
        password = request.post["password"]
        confirm_password = request.post["confirm_password"]
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect("register")
            elif User.objects.filter(email=email).exits():
                messages.info(request, "email taken")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "password not matched")
            return redirect("register")
    return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authentication(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid')
            return redirect('login')
    return render(request, 'login.html')
