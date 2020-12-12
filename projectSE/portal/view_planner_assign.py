from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from .models import Activity, Availability

class PlannerCheck(UserPassesTestMixin):
    def test_func(self):
        return (self.request.user.profile.user_type=='Planner')

def planner_check(user):
    return user.profile.user_type == 'Planner'

def AssignView(request, pk, week):
    activity = Activity.objects.filter(pk=pk)
    availability = Availability.objects.filter(week=week)
    return render(request, "portal/planner/assign_activity.html", {"list_activity":activity,"list_maintainer":availability})
