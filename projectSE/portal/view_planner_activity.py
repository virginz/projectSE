from django.views import generic
from django.shortcuts import get_object_or_404
from  .forms import selectWeek
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
import csv, io
from django.urls import reverse_lazy
from .models import Activity

class PlannerCheck(UserPassesTestMixin):
    def test_func(self):
        return (self.request.user.profile.user_type=='Planner')

def planner_check(user):
    return user.profile.user_type == 'Planner'

class PlannerView(PlannerCheck, generic.ListView):
    model = Activity
    template_name = 'portal/planner/planner_home.html'
    context_object_name = 'activity_list'

    def get_queryset(self):
        week = self.request.GET.get('week')
        if week == "all" or week == None:
            return super().get_queryset().order_by('pk')
        else:
            return super().get_queryset().order_by('pk').filter(week=week)

@user_passes_test(planner_check)
def select_week(request):
    if request.method == 'POST':
        form = selectWeek(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            week = cd['week']
            return redirect('planner/home?week=' + str(week))
    else:
        form = selectWeek()
        return redirect('planner_home')

class OwnerMixin(object):

    def get_queryset(self):
        return super().get_queryset().order_by('pk')

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
    ]

    success_url = reverse_lazy('planner_home')

class OwnerActivityEditMixin(OwnerActivityMixin):
    template_name = 'portal/planner/create_activity.html'


class ActivityCreateView(OwnerActivityEditMixin, PlannerCheck, generic.CreateView):
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

class PlannerDeleteView(PlannerCheck, generic.DeleteView):
    model = Activity
    success_url = reverse_lazy('planner_home')

class OwnerActivityEditMixin(OwnerActivityMixin):
    template_name = 'portal/planner/modify_activity.html'

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
    ]
