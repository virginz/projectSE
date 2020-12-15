from django.test import SimpleTestCase
from ..forms import LoginForm

class TestForms(SimpleTestCase):

    def test_login_form_no_data(self):
        form = LoginForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),2)

    def test_login_form_valide_data(self):
        form = LoginForm(data={
            'username' : 'paolocolella@gmail.com',
            'password': 'ds'
        })
        self.assertFalse(form.is_valid())
