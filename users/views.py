from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, decorators, get_user_model
from django.conf import settings

from .forms import UserRegistrationForm

User = settings.AUTH_USER_MODEL


def register_view(request):
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('email')
            # username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            new_user = authenticate(request, username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'])
            # new_user = authenticate(username=username, password=password)
            login(request, new_user)
            messages.success(request, f"user {username} creates successfully .")
            return redirect("index")
    else:
        form = UserRegistrationForm()

    return render(request, "users/sign_up.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = get_user_model().objects.filter(email=email)
        except:
            messages.warning(request, "User not found")

        user_authenticated = authenticate(request, email=email, password=password)

        if user_authenticated is not None:
            login(request, user_authenticated)
            messages.success(request, "you are now logged in")
            return redirect("index")
        else:
            messages.warning(request, "does not match your email or password")
            return render(request, "users/login.html", {"message": messages})
    else:
        return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    messages.success(request, "you are now logged out")
    return redirect("index")


def show_subscribtions(request, user_id):
    # user = get_object_or_404(User, id=user_id)
    # user = User.objects.get(id=user_id)
    user = request.user
    subscribers = user.channel.subscribers.all()
    context = {
        'user': user,
        'subscribers': subscribers
    }

    return render(request, "users/profile/subscribtion.html", context)
