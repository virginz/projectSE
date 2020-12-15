from django.test import SimpleTestCase
from django.urls import resolve, reverse
from ..views import user_login
from ..views_admin_users import *
from ..view_admin_procedures import *
from ..view_planner_activity import *
from ..view_planner_assign import *
from django.contrib.auth import views as auth_views
import re

class TestUrls(SimpleTestCase):

    def test_login_urls_is_resolved(self):
        url=reverse('login')
        self.assertEquals(resolve(url).func,user_login)

    def test_logout_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, auth_views.LogoutView)

    def test_create_user_is_resolved(self):
        url = reverse('add_user')
        self.assertEquals(resolve(url).func, create_user)

    def test_create_single_user_is_resolved(self):
        url = reverse('add_single_user')
        self.assertEquals(resolve(url).func, create_single_user)

    def test_create_procedures_is_resolved(self):
        url = reverse('add_procedure')
        self.assertEquals(resolve(url).func, create_procedure)

    def test_create_single_procedures_is_resolved(self):
        url = reverse('add_one_procedure')
        self.assertEquals(resolve(url).func.view_class, ProcedureCreateView)


    def test_admin_home_is_resolved(self):
        url = reverse('systemadministrator_home')
        self.assertEquals(resolve(url).func.view_class, AdminView)

    def test_admin_home_procedures_is_resolved(self):
        url = reverse('systemadministrator_procedures')
        self.assertEquals(resolve(url).func.view_class, ProcedureView)

    def test_user_edit_is_resolved(self):
        expected_url_pattern = 'admin/home/\d+/edit/'
        the_url_being_tested = 'admin/home/59/edit/'
        self.assertTrue(re.match(expected_url_pattern, the_url_being_tested))

    def test_procedures_edit_is_resolved(self):
        expected_url_pattern = 'admin/home/\d+/edit/'
        the_url_being_tested = 'admin/home/11/edit/'
        self.assertTrue(re.match(expected_url_pattern, the_url_being_tested))

    def test_user_delete_is_resolved(self):
        expected_url_pattern = 'admin/home/\d+/delete/'
        the_url_being_tested = 'admin/home/89/delete/'
        self.assertTrue(re.match(expected_url_pattern, the_url_being_tested))

    def test_procedures_delete_is_resolved(self):
            expected_url_pattern = 'admin/home/\d+/delete-procedure/'
            the_url_being_tested = 'admin/home/69/delete-procedure/'
            self.assertTrue(re.match(expected_url_pattern, the_url_being_tested))

    def test_planner_is_resolved(self):
        url = reverse('planner_home')
        self.assertEquals(resolve(url).func.view_class, PlannerView)

    def test_add_activity_is_resolved(self):
        url = reverse('add_activity')
        self.assertEquals(resolve(url).func.view_class, ActivityCreateView)

    def test_activity_delete_is_resolved(self):
            expected_url_pattern = 'planner/home/\d+/delete-activity/'
            the_url_being_tested = 'planner/home/39/delete-activity/'
            self.assertTrue(re.match(expected_url_pattern, the_url_being_tested))

    def test_activity_edit_is_resolved(self):
            expected_url_pattern = 'planner/home/\d+/edit-activity/'
            the_url_being_tested = 'planner/home/96/edit-activity/'
            self.assertTrue(re.match(expected_url_pattern, the_url_being_tested))

    def test_verify_information_activity_is_resolved(self):
            expected_url_pattern = 'planner/home/\d+/verify-information-activity/'
            the_url_being_tested = 'planner/home/61/verify-information-activity/'
            self.assertTrue(re.match(expected_url_pattern, the_url_being_tested))

    def test_assign_activity_is_resolved(self):
        url=reverse('assign_activity')
        self.assertEquals(resolve(url).func,AssignView)

    def test_availability_is_resolved(self):
        url=reverse('availability_slot')
        self.assertEquals(resolve(url).func,ViewAvailabily)

    def test_activity_assigned_is_resolved(self):
        url = reverse('activity_assigned')
        self.assertEquals(resolve(url).func.view_class,ActivityAssigned)

















