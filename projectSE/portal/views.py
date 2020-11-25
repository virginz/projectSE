from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views import generic
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if (user.profile.user_type == 'SystemAdministrator'):
                        return redirect('systemadministrator_home')
                    if (user.profile.user_type == 'Planner'):
                        return redirect('planner_home')
                    if (user.profile.user_type == 'Maintainer'):
                        return redirect('maintainer_home')
                else:
                    return HttpResponse('Disabled')
            else:
                print(user)
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'portal/login.html', {'form':form})
    