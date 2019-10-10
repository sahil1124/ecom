from django.shortcuts import render,redirect
from .forms import UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from face.models import Profile
from django.contrib.auth.models import User
# Create your views here.
def profile(request):
     users_without_profile = User.objects.filter(profile__isnull=True)
     for user in users_without_profile:
         Profile.objects.create(user=user)
     return render(request,'profile.html')


def update_profile(request):
    if request.method == 'POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return  redirect('profile')
            messages.success(request,('Your account has benn updated!'))
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)

    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'update_profile.html' ,context)
