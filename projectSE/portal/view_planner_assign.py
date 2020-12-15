from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from .models import Activity, Availability
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse

class PlannerCheck(UserPassesTestMixin):
    def test_func(self):
        return (self.request.user.profile.user_type=='Planner')

def planner_check(user):
    return user.profile.user_type == 'Planner'

def AssignView(request, pk, week):
    activity = Activity.objects.filter(pk=pk)
    availability = Availability.objects.filter(week=week)
    return render(request, "portal/planner/assign_activity.html", {"list_activity":activity,"list_maintainer":availability})

def ViewAvailabily(request, pkAct, pkAva):
    availability = Availability.objects.filter(pk=pkAva)
    activity = Activity.objects.filter(pk=pkAct)
    return render(request, "portal/planner/view_slot.html", {"list_activity":activity, "availability":availability})

def AssignSlot8_9(request, pkAct, pkAva):
    availability = Availability.objects.get(pk=pkAva)
    activity = Activity.objects.get(pk=pkAct)
    availability.slot8_9 = availability.slot8_9 + activity.estimation_time
    activity.assigned_to = True
    availability.save()
    activity.save()
    return HttpResponseRedirect(reverse('planner_home'))

def AssignSlot9_10(request, pkAct, pkAva):
    availability = Availability.objects.get(pk=pkAva)
    activity = Activity.objects.get(pk=pkAct)
    availability.slot9_10 = availability.slot9_10 + activity.estimation_time
    activity.assigned_to = True
    availability.save()
    activity.save()
    return HttpResponseRedirect(reverse('planner_home'))

def AssignSlot10_11(request, pkAct, pkAva):
    availability = Availability.objects.get(pk=pkAva)
    activity = Activity.objects.get(pk=pkAct)
    availability.slot10_11 = availability.slot10_11 + activity.estimation_time
    activity.assigned_to = True
    availability.save()
    activity.save()
    return HttpResponseRedirect(reverse('planner_home'))

def AssignSlot11_12(request, pkAct, pkAva):
    availability = Availability.objects.get(pk=pkAva)
    activity = Activity.objects.get(pk=pkAct)
    availability.slot11_12 = availability.slot11_12 + activity.estimation_time
    activity.assigned_to = True
    availability.save()
    activity.save()
    return HttpResponseRedirect(reverse('planner_home'))

def AssignSlot14_15(request, pkAct, pkAva):
    availability = Availability.objects.get(pk=pkAva)
    activity = Activity.objects.get(pk=pkAct)
    availability.slot14_15 = availability.slot14_15 + activity.estimation_time
    activity.assigned_to = True
    availability.save()
    activity.save()
    return HttpResponseRedirect(reverse('planner_home'))

def AssignSlot15_16(request, pkAct, pkAva):
    availability = Availability.objects.get(pk=pkAva)
    activity = Activity.objects.get(pk=pkAct)
    availability.slot15_16 = availability.slot15_16 + activity.estimation_time
    activity.assigned_to = True
    availability.save()
    activity.save()
    return HttpResponseRedirect(reverse('planner_home'))

def AssignSlot16_17(request, pkAct, pkAva):
    availability = Availability.objects.get(pk=pkAva)
    activity = Activity.objects.get(pk=pkAct)
    availability.slot16_17 = availability.slot16_17 + activity.estimation_time
    activity.assigned_to = True
    availability.save()
    activity.save()
    return HttpResponseRedirect(reverse('planner_home'))


