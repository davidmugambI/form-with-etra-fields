from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect,HttpResponse
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm,\
    UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.zalegodet.gender = form.cleaned_data.get('gender')
            user.zalegodet.lang = form.cleaned_data.get('lang')
            user.save()
            messages.success(request, 'Account created')
            return redirect('webapp:login')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=user.username, password=raw_password)
            # login(request, user)
            # return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'webapp/form.html', {'form': form})
@login_required
def home(request):
    return render(request,'webapp/profile.html')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST,user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
        else:
            return redirect('/account /')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'webapp/change_password.html', args)