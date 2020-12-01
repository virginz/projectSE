from django.views import generic
from.views import user_login
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
import csv, io
from .models import Profile, Procedure
from django.urls import reverse_lazy

class AdminCheck(UserPassesTestMixin):
    def test_func(self):
        return (self.request.user.profile.user_type=='SystemAdministrator')

def admin_check(user):
    return user.profile.user_type == 'SystemAdministrator'

class AdminView(AdminCheck, generic.ListView):
    model = User
    template_name = 'portal/admin/admin_home.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        return super().get_queryset().order_by('username').exclude(is_superuser=True)

@user_passes_test(admin_check)
def create_user(request):
    template = 'portal/admin/create_user.html'

    prompt = {'order': 'Scegli un file .csv con il seguente formato: Email,Cognome,Nome'}

    if request.method == 'GET':
        return render(request, template, prompt)
    else:
        try:
            csv_file = request.FILES['file']
        except :
            prompt = {'order': 'Seleziona prima un file .csv da caricare!'}
            return render(request, template, prompt)
        else:
            if not csv_file.name.endswith('.csv'):
                prompt = {'order': 'Formato errato!'}
                return render(request, template, prompt)
            else:
                data_set = csv_file.read().decode('UTF-8')
                io_string = io.StringIO(data_set)
                form = request.POST
                usertype = form['usertype']
                num_user = 0
                new_users= []
                for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                    user, created = User.objects.update_or_create(
                        username=column[0],
                        email=column[0],
                        last_name=column[2],
                        first_name=column[3],
                         
                    )
                    if created:
                        user.is_active = True
                        user.set_password(column[1])
                        user.save()
                        profile, profilecreated = Profile.objects.update_or_create(user=user, user_type=usertype)
                        num_user = num_user+1
                        new_users.append(user)
                        

                context = { 'new_users': new_users,
                            'num_user': num_user
                            }
                return render(request, template, context)

class UserDeleteView(AdminCheck, generic.DeleteView):
    model = User
    success_url = reverse_lazy('systemadministrator_home')