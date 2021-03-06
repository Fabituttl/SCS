from django.shortcuts import render, redirect
from django.urls import reverse
import pprint

from accounts.forms import (
    RegistrationForm,
    EditProfileForm
)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import sensormeasure
from .models import UserProfile
from .models import sensor, sensor_state

def index(request):
    return render(request, 'index.html')

def home(request):
    numbers = [1,2,3,4,5]
    name = 'Fabian Stadler'
    user = request.user

    args = {'myName': name, 'numbers': numbers, 'user':user}
    return render(request, 'accounts/home.html', args)

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:home'))
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)

def view_profile(request):
    user = request.user
    sensors = sensor.objects.filter(user=request.user.id)
    args = {'user': user, 'sensors': sensors}
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:view_profile'))
        else:
            return redirect(reverse('accounts:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)

def sensor_measures(request):
    user = request.user
    sensors = sensor.objects.filter(user=request.user.id)
    sensormeasures = sensormeasure.objects.all()
    args = {'user': user,'sensors': sensors, 'sensormeasures': sensormeasures }#'sensormeasures':sensormeasures
    return render(request, 'accounts/sensor_measure.html', args)
