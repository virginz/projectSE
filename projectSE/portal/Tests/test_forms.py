from django.test import SimpleTestCase
from ..forms import LoginForm
from ..forms import addSingleUserForm

class TestForms(SimpleTestCase):

    def test_login_form_valid_data(self):
        form = LoginForm(data={
            'username' : 'paolocolella@gmail.com',
            'password': 'ds'
        })
        self.assertFalse(form.is_valid())

    def test_login_form_no_data(self):
        form = LoginForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)



    def test_add_single_user_form_validate_data(self):
        form = addSingleUserForm(data={
            'email' : 'paolocolella@gmail.com',
            'password' : 'ds',
            'first_name' : 'paolo',
            'last_name' : 'colella',
            'usertype' : 'Planner'
        })
        self.assertFalse(form.is_valid())

    def test_add_single_user_form_no_data(self):
        form = addSingleUserForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)


