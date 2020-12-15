from django.test import TestCase
from ..models import Competence, Profile, Procedure
from django.contrib.auth.models import User

class TestModels(TestCase):

    def setUp(self):

        self.user = User.objects.create(
            username = 'paoletto',
            password = 'ingegnere',
            first_name = 'Paolo',
            last_name = 'Colella'
        )
        self.profile = Profile.objects.create(
            user = self.user,
            user_type = 'SystemAdministrator'
        )
        self.procedure = Procedure.objects.create(
            procedureName = 'cambio olio',
            procedureDescription = 'aprire la bottiglia e cambiare olio'
        )

    def test_profile(self):
        self.assertEquals(str(self.profile), 'Colella Paolo')

    def test_procedure(self):
        self.assertEquals(str(self.procedure), 'cambio olio aprire la bottiglia e cambiare olio')


