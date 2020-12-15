from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from .models import Activity, Assignment, Profile

class PlannerCheck(UserPassesTestMixin):
    def test_func(self):
        return (self.request.user.profile.user_type=='Planner')

def planner_check(user):
    return user.profile.user_type == 'Planner'

def AssignView(request, pk, week):
    activity = Activity.objects.filter(pk=pk)
    assignment = Assignment.objects.filter(week=week)
    maintainers = Profile.objects.filter(user_type='Maintainer')
    return render(request, "portal/planner/assign_activity.html", {"list_activity":activity,"list_maintainer":maintainers, "list_assignment":assignment})

def ViewAvailabily(request, pkAct, pkAss):
    availability = Assignment.objects.filter(pk=pkAss)
    activity = Activity.objects.filter(pk=pkAct)
    return render(request, "portal/planner/view_slot.html", {"list_activity":activity, "availability":availability})

