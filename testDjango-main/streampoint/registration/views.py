from django.shortcuts import render, HttpResponsePermanentRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from registration.forms import UserLoginForm
from django.urls import reverse
from registration.forms import UserRegistrationForm

def reg_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponsePermanentRedirect(reverse('/'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render (request, 'registration/regist.html', context)
def login(requst):
    if requst.method == 'POST':
        form = UserLoginForm(data=requst.POST)
        if form.is_valid():
            username = requst.POST['username']
            password = requst.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(requst, user)
                return HttpResponsePermanentRedirect('/')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(requst, 'registration/login.html', context)