from django.test import SimpleTestCase
from django.urls import resolve, reverse
from ..views import user_login
from ..views_admin_users import *
from ..view_admin_procedures import *
import re

class TestUrls(SimpleTestCase):

    def test_login_urls_is_resolved(self):
        url=reverse('login')
        self.assertEquals(resolve(url).func,user_login)

    def test_create_user_is_resolved(self):
        url = reverse('add_user')
        self.assertEquals(resolve(url).func, create_user)

    def test_create_procedures_is_resolved(self):
        url = reverse('add_procedure')
        self.assertEquals(resolve(url).func, create_procedure)

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















