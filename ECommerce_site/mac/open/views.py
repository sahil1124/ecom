from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .  import forms
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.

class Signup(CreateView):
    form_class=forms.UserCreateForm
    success_url=reverse_lazy('login')
    template_name='open/signup.html'

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return  HttpResponseRedirect('password_change_done')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'open/password_change.html', {
        'form': form
    })


def change_password_done(request):
    return render(request,'open/password_change_done.html',{})
