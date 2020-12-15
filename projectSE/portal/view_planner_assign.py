from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
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
    day_loop = "0123456"
    return render(request, "portal/planner/assign_activity.html", {"list_activity":activity,"list_maintainer":maintainers, "list_assignment":assignment, "day_loop":day_loop})


def ViewAvailabily(request, pkAct, pkMain, day):


    activity = Activity.objects.get(pk=pkAct)
    if day==0:
        availability = Assignment.objects.filter(maintainer=pkMain, day='Lunedì', week=activity.week)
    elif day==1:
        availability = Assignment.objects.filter(maintainer=pkMain, day='Martedì', week=activity.week)
    elif day==2:
        availability = Assignment.objects.filter(maintainer=pkMain, day='Mercoledì', week=activity.week)
    elif day==3:
        availability = Assignment.objects.filter(maintainer=pkMain, day='Giovedì', week=activity.week)
    elif day==4:
        availability = Assignment.objects.filter(maintainer=pkMain, day='Venerdì', week=activity.week)
    elif day==5:
        availability = Assignment.objects.filter(maintainer=pkMain, day='Sabato', week=activity.week)
    else:
        availability = Assignment.objects.filter(maintainer=pkMain, day='Domenica', week=activity.week)
    
    activity = Activity.objects.filter(pk=pkAct)
    maintainer=Profile.objects.filter(pk=pkMain)
    return render(request, "portal/planner/view_slot.html", {"list_activity":activity, "availability":availability, "day":day, "maintainer":maintainer})

def AssignSlot8_9(request, pkAss, pkAct, day, maintainer):
    
    activity = Activity.objects.get(pk=pkAct)
    main = Profile.objects.get(pk=maintainer)
    if pkAss == 0:
        if day==0:
            day = 'Lunedì'
        elif day==1:
            day = 'Martedì'
        elif day==2:
            day = 'Mercoledì'
        elif day==3:
            day = 'Giovedì'
        elif day==4:
            day = 'Venerdì'
        elif day==5:
            day='Sabato'
        else:
            day='Domenica'
        assign = Assignment.objects.update_or_create(
            minutes = 60 - activity.estimation_time,
            time_slot = "8-9",
            day = day,
            week = activity.week,
            maintainer = main
        )
        activity.assigned_to = True
        activity.save()
    else:
        assign = Assignment.objects.get(pk=pkAss)
        assign.minutes = assign.minutes - activity.estimation_time
        activity.assigned_to = True
        assign.save()
        activity.save()
    return HttpResponseRedirect(reverse('planner_home'))

def AssignSlot9_10(request, pkAss, pkAct, day, maintainer):
    
    activity = Activity.objects.get(pk=pkAct)
    main = Profile.objects.get(pk=maintainer)
    if pkAss == 0:
        if day==0:
            day = 'Lunedì'
        elif day==1:
            day = 'Martedì'
        elif day==2:
            day = 'Mercoledì'
        elif day==3:
            day = 'Giovedì'
        elif day==4:
            day = 'Venerdì'
        elif day==5:
            day='Sabato'
        else:
            day='Domenica'
        assign = Assignment.objects.update_or_create(
            minutes = 60 - activity.estimation_time,
            time_slot = "9-10",
            day = day,
            week = activity.week,
            maintainer = main
        )
        activity.assigned_to = True
        activity.save()
    else:
        assign = Assignment.objects.get(pk=pkAss)
        assign.minutes = assign.minutes - activity.estimation_time
        activity.assigned_to = True
        assign.save()
        activity.save()
    return HttpResponseRedirect(reverse('planner_home'))

def AssignSlot10_11(request, pkAss, pkAct, day, maintainer):
    
    activity = Activity.objects.get(pk=pkAct)
    main = Profile.objects.get(pk=maintainer)
    if pkAss == 0:
        if day==0:
            day = 'Lunedì'
        elif day==1:
            day = 'Martedì'
        elif day==2:
            day = 'Mercoledì'
        elif day==3:
            day = 'Giovedì'
        elif day==4:
            day = 'Venerdì'
        elif day==5:
            day='Sabato'
        else:
            day='Domenica'
        assign = Assignment.objects.update_or_create(
            minutes = 60 - activity.estimation_time,
            time_slot = "10-11",
            day = day,
            week = activity.week,
            maintainer = main
        )
        activity.assigned_to = True
        activity.save()
    else:
        assign = Assignment.objects.get(pk=pkAss)
        assign.minutes = assign.minutes - activity.estimation_time
        activity.assigned_to = True
        assign.save()
        activity.save()
    return HttpResponseRedirect(reverse('planner_home'))

def AssignSlot11_12(request, pkAss, pkAct, day, maintainer):
    
    activity = Activity.objects.get(pk=pkAct)
    main = Profile.objects.get(pk=maintainer)
    if pkAss == 0:
        if day==0:
            day = 'Lunedì'
        elif day==1:
            day = 'Martedì'
        elif day==2:
            day = 'Mercoledì'
        elif day==3:
            day = 'Giovedì'
        elif day==4:
            day = 'Venerdì'
        elif day==5:
            day='Sabato'
        else:
            day='Domenica'
        assign = Assignment.objects.update_or_create(
            minutes = 60 - activity.estimation_time,
            time_slot = "11-12",
            day = day,
            week = activity.week,
            maintainer = main
        )
        activity.assigned_to = True
        activity.save()
    else:
        assign = Assignment.objects.get(pk=pkAss)
        assign.minutes = assign.minutes - activity.estimation_time
        activity.assigned_to = True
        assign.save()
        activity.save()
    return HttpResponseRedirect(reverse('planner_home'))

def AssignSlot14_15(request, pkAss, pkAct, day, maintainer):
    
    activity = Activity.objects.get(pk=pkAct)
    main = Profile.objects.get(pk=maintainer)
    if pkAss == 0:
        if day==0:
            day = 'Lunedì'
        elif day==1:
            day = 'Martedì'
        elif day==2:
            day = 'Mercoledì'
        elif day==3:
            day = 'Giovedì'
        elif day==4:
            day = 'Venerdì'
        elif day==5:
            day='Sabato'
        else:
            day='Domenica'
        assign = Assignment.objects.update_or_create(
            minutes = 60 - activity.estimation_time,
            time_slot = "14-15",
            day = day,
            week = activity.week,
            maintainer = main
        )
        activity.assigned_to = True
        activity.save()
    else:
        assign = Assignment.objects.get(pk=pkAss)
        assign.minutes = assign.minutes - activity.estimation_time
        activity.assigned_to = True
        assign.save()
        activity.save()
    return HttpResponseRedirect(reverse('planner_home'))

def AssignSlot15_16(request, pkAss, pkAct, day, maintainer):
    
    activity = Activity.objects.get(pk=pkAct)
    main = Profile.objects.get(pk=maintainer)
    if pkAss == 0:
        if day==0:
            day = 'Lunedì'
        elif day==1:
            day = 'Martedì'
        elif day==2:
            day = 'Mercoledì'
        elif day==3:
            day = 'Giovedì'
        elif day==4:
            day = 'Venerdì'
        elif day==5:
            day='Sabato'
        else:
            day='Domenica'
        assign = Assignment.objects.update_or_create(
            minutes = 60 - activity.estimation_time,
            time_slot = "15_16",
            day = day,
            week = activity.week,
            maintainer = main
        )
        activity.assigned_to = True
        activity.save()
    else:
        assign = Assignment.objects.get(pk=pkAss)
        assign.minutes = assign.minutes - activity.estimation_time
        activity.assigned_to = True
        assign.save()
        activity.save()
    return HttpResponseRedirect(reverse('planner_home'))

def AssignSlot16_17(request, pkAss, pkAct, day, maintainer):
    
    activity = Activity.objects.get(pk=pkAct)
    main = Profile.objects.get(pk=maintainer)
    if pkAss == 0:
        if day==0:
            day = 'Lunedì'
        elif day==1:
            day = 'Martedì'
        elif day==2:
            day = 'Mercoledì'
        elif day==3:
            day = 'Giovedì'
        elif day==4:
            day = 'Venerdì'
        elif day==5:
            day='Sabato'
        else:
            day='Domenica'
        assign = Assignment.objects.update_or_create(
            minutes = 60 - activity.estimation_time,
            time_slot = "16-17",
            day = day,
            week = activity.week,
            maintainer = main
        )
        activity.assigned_to = True
        activity.save()
    else:
        assign = Assignment.objects.get(pk=pkAss)
        assign.minutes = assign.minutes - activity.estimation_time
        activity.assigned_to = True
        assign.save()
        activity.save()
    return HttpResponseRedirect(reverse('planner_home'))
