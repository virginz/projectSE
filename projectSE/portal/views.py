from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views import generic
from .forms import LoginForm


#Login access
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
                    form = LoginForm()
                    context = {
                        'form' : form,
                        'error' : 'Account inattivo:'
                    }
                return render(request,'portal/login.html',context)
            else:
                form = LoginForm()
                context = {
                    'form' : form,
                    'error' : 'Mail e/o password errate:'
                }
                return render(request,'portal/login.html',context)
    else:
        form = LoginForm()
    return render(request, 'portal/login.html', {'form':form})
