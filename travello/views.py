from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib import messages
from .models import Destination
# Create your views here.

@login_required
def index(request):

    dests = Destination.objects.all()

    return render(request, "index.html", {'dests': dests})

# def login(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         # user = User.objects.create_user(username=username)
#         return redirect("/")
#     else:
#         form = UserCreationForm()
#         return render(request, 'temp_login.html',{'form':form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def about(request):
    return render(request,'about.html')

