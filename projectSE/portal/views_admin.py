from django.views import generic
from.views import user_login
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin

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
        return super().get_queryset().order_by('-date_joined').exclude(is_superuser=True)