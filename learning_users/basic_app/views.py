from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm

#
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in ")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False


    if request.method == 'POST':
        # Grab infor from form
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # cHECK IF BOTH FORMS ARE VALID
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password) #Hashing Passwd
            user.save()

            profile = profile_form.save(commit=False) # Manipulating Data before Commiting to DB
            profile.user = user

            # Check if pic in there
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered =True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/registration.html',
                  {'user_form': user_form ,
                    'profile_form': profile_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("account not active")
        else:
            print("Someone failed to Login")
            print("Username: {} and Password: {}".format(username, password))
            return HttpResponse("Invalid Login Details given")
    else:
        return render(request, 'basic_app/login.html')