from django.test import SimpleTestCase
from portal.forms import LoginForm, PasswordForm

class TestForms(SimpleTestCase):

    def test_password_form_valide_data(self):
        form = PasswordForm(data={
            'password' : 'ingegnere'
        })
        self.assertTrue(form.is_valid())
    
    def test_login_form_no_data(self):
        form = LoginForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),2)

    def test_login_form_valide_data(self):
        form = LoginForm(data={
            'username' : 'paolocolella@gmail.com',
            'password': 'ingegnere'
        })
        self.assertTrue(form.is_valid())