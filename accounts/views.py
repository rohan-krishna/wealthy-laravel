from django.shortcuts import render, redirect
from . forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from social_django.models import UserSocialAuth


# Create your views here.
def user_login(request):
    
    if request.method == 'GET':
        form = UserLoginForm()
        return render(request, 'accounts/login.html', { 'form' : form })
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('journal:index')
        else:
            messages.add_message(request, messages.INFO, 'Sorry. Wrong username and password combo. Please try again with correct details')
            return redirect('accounts:login')

@login_required
def settings(request):
    user =request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'accounts/settings.html', {
        'github_login' : github_login,
        'can_disconnect' : can_disconnect
    })

@login_required
def set_password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password has been successfully updated!')
            return redirect('accounts:set_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'accounts/set_password.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('/')