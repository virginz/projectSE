from django.views import generic
from  .forms import addSingleUserForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
import csv, io
from .models import Profile
from django.urls import reverse_lazy

#Classe utilizzata dalle classi per il controllo del tipo di utente (SystemAdministrator)
class AdminCheck(UserPassesTestMixin):
    def test_func(self):
        return (self.request.user.profile.user_type=='SystemAdministrator')

#Metodo utilizzato per il controllo del tipo di utente (SystemAdministrator)
def admin_check(user):
    return user.profile.user_type == 'SystemAdministrator'

#Classe che restituisce il model alla homepage dell'admin
class AdminView(AdminCheck, generic.ListView):
    model = User
    template_name = 'portal/admin/admin_home.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        return super().get_queryset().order_by('username').exclude(username=self.request.user.profile.user.username).exclude(is_superuser=True)

#Creazione utente tramite file
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

#Creazione singolo utente tramite form
@user_passes_test(admin_check)
def create_single_user(request):
    template = 'portal/admin/create_single_user.html'

    if request.method == 'POST':
        form = addSingleUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            email = cd['email']
            usertype = cd['usertype']
            first_name = cd['first_name']
            last_name = cd['last_name']
            password = cd['password']
            user, created = User.objects.update_or_create(
                username=email,
                email=email,
                last_name=last_name,
                first_name=first_name,
            )
            if created:
                user.is_active = True
                user.set_password(password)
                user.save()
                profile, profilecreated = Profile.objects.update_or_create(user=user, user_type=usertype)
                return redirect('systemadministrator_home')
    else:
        form = addSingleUserForm()
        return render(request, template)

#Cancellazione di un utente
class UserDeleteView(AdminCheck, generic.DeleteView):
    model = User
    success_url = reverse_lazy('systemadministrator_home')

#Query al db per recuperare gli utenti ordinati per date_joined
class OwnerMixin(object):

    def get_queryset(self):
        return super().get_queryset().order_by('date_joined')

#Definizione degli attributi del modello da restituire
class OwnerUserMixin(OwnerMixin): 
    model = User
    fields = [
        'first_name',
        'last_name',
        'username',
        'email'
    ]

    success_url = reverse_lazy('systemadministrator_home')

#Definizione del template per la modifica dell'utente
class OwnerUserEditMixin(OwnerUserMixin):
    template_name = 'portal/admin/modify_form.html'

#Definizione degli attributi da modificare nel template fornito
class UserEditView(OwnerUserEditMixin, AdminCheck, generic.UpdateView):
    fields = [
        'first_name',
        'last_name',
        'username',
        'email'
    ]
