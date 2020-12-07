from django.views import generic
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
        return super().get_queryset().order_by('pk')

#@user_passes_test(planner_check)
#def week_number(self):

