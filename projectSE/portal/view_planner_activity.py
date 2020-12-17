from django.views import generic
from django.shortcuts import get_object_or_404
from  .forms import selectWeek
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
import csv, io
from django.urls import reverse_lazy
from .models import Activity, Assignment

#Classe utilizzata dalle classi per il controllo del tipo di utente (Planner)
class PlannerCheck(UserPassesTestMixin):
    def test_func(self):
        return (self.request.user.profile.user_type=='Planner')

#Metodo utilizzato per il controllo del tipo di utente (Planner)
def planner_check(user):
    return user.profile.user_type == 'Planner'

#Classe che restituisce il model alla homepage del planner
class PlannerView(PlannerCheck, generic.ListView):
    model = Activity
    template_name = 'portal/planner/planner_home.html'
    context_object_name = 'activity_list'

    def get_queryset(self):
        week = self.request.GET.get('week')
        if week == "all" or week == None:
            return super().get_queryset().order_by('pk').filter(assigned_to = None)
        else:
            return super().get_queryset().order_by('pk').filter(week=week, assigned_to = None)

#Query al db per recuperare le attività ordinati per chiave primaria
class OwnerMixin(object):
    
    def get_queryset(self):
        return super().get_queryset().order_by('pk')

#Definizione degli attributi del modello da restituire
class OwnerActivityMixin(OwnerMixin):
    model = Activity
    fields = [
        'activity_type',
        'factory_site',
        'factory_area',
        'activity_typology',
        'activity_description',
        'estimation_time',
        'interruptible',
        'materials',
        'week',
        'workspace_notes',
        'competences_needed'
    ]

    success_url = reverse_lazy('planner_home')

#Definizione del template per la creazione dell'utente
class OwnerActivityCreatetMixin(OwnerActivityMixin):
    template_name = 'portal/planner/create_activity.html'

#Definizione degli attributi per la creazione di un'attività tramite il template fornito
class ActivityCreateView(OwnerActivityCreatetMixin, PlannerCheck, generic.CreateView):
    fields = [
        'activity_type',
        'factory_site',
        'factory_area',
        'activity_typology',
        'activity_description',
        'estimation_time',
        'interruptible',
        'materials',
        'week',
        'workspace_notes',
        'competences_needed'
    ]

#Cancellazione di un'attività
class PlannerDeleteView(PlannerCheck, generic.DeleteView):
    model = Activity
    success_url = reverse_lazy('planner_home')

#Definizione del template per la modifica dell'attività
class OwnerActivityEditMixin(OwnerActivityMixin):
    template_name = 'portal/planner/modify_activity.html'

#Definizione degli attributi da modificare nel template fornito
class ActivityEditView(OwnerActivityEditMixin, PlannerCheck, generic.UpdateView):
    fields = [
        'activity_type',
        'factory_site',
        'factory_area',
        'activity_typology',
        'activity_description',
        'estimation_time',
        'interruptible',
        'materials',
        'week',
        'workspace_notes',
        'competences_needed'
    ]

#Query al db per recuperare le attività ordinati per chiave primaria, definizione del modello da modificare e del template da utilizzare
class OwnerVerifyActivityMixin(object):
    context_object_name = 'view_information'

    def get_queryset(self):
        return super().get_queryset().order_by('pk')
    
    model = Activity
    fields = [
        'activity_type',
        'factory_site',
        'factory_area',
        'activity_typology',
        'activity_description',
        'estimation_time',
        'interruptible',
        'materials',
        'week',
        'workspace_notes',
    ]

    template_name = 'portal/planner/verify_information_activity.html'
    success_url = reverse_lazy('planner_home')
    
#Definizione degli attributi da modificare 
class VerifyActivityView(OwnerVerifyActivityMixin, PlannerCheck, generic.UpdateView):
    fields = [
        'workspace_notes',
    ]

#Classe che restituisce il model alla page delle Attività assegnate filtrate per settimana
class ActivityAssigned(PlannerCheck, generic.ListView):
    model = Activity
    template_name = 'portal/planner/activity_assigned.html'
    context_object_name = 'activity_list'

    def get_queryset(self):
        week = self.request.GET.get('week')
        if week == "all" or week == None:
            return super().get_queryset().order_by('pk').exclude(assigned_to = None)
        else:
            return super().get_queryset().order_by('pk').filter(week=week).exclude(assigned_to = None)
        
