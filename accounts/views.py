from django.shortcuts import render, redirect
from . forms import UserLoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

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
