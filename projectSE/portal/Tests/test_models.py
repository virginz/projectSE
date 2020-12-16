from django.test import TestCase
from ..models import Competence, Profile, Procedure, Assignment, Activity
from django.contrib.auth.models import User

class TestModels(TestCase):

    def setUp(self):

        self.user = User.objects.create(
            username = 'paoletto',
            password = 'ingegnere',
            first_name = 'Paolo',
            last_name = 'Colella'
        )
        self.user2 = User.objects.create(
            username = 'fabietto',
            password = 'prova1997',
            first_name = 'Socio',
            last_name = 'Carbone'
        )
        self.profile = Profile.objects.create(
            user = self.user,
            user_type = 'SystemAdministrator'
        )
        self.profile2 = Profile.objects.create(
            user = self.user2,
            user_type = 'Maintainer'
        )
        self.procedure = Procedure.objects.create(
            procedureName = 'cambio olio',
            procedureDescription = 'aprire la bottiglia e cambiare olio'
        )
        self.competence = Competence.objects.create(
            competenceName = 'Verifica Sterzata',
            listProcedure = self.procedure
        )
        self.assignment = Assignment.objects.create(
            minutes = '50',
            time_slot = '14-15',
            day = 'Venerdì',
            week = '2',
            maintainer = self.profile2
        )
        self.activity  = Activity.objects.create(
            activity_type = 'Planned',
            factory_site = 'prova',
            factory_area = 'area',
            activity_typology='Electrical',
            activity_description = 'prova',
            estimation_time = '2',
            interruptible ='True',
            materials = 'acciao',
            week = '2',
            workspace_notes = 'aa',
            assigned_to = 'True'
        )
        self.activity2 = Activity.objects.create(
            activity_type = 'Unplanned',
            factory_site = 'prova',
            factory_area = 'area',
            activity_typology='Electrical',
            activity_description = 'prova',
            estimation_time = '2',
            interruptible ='True',
            materials = 'materiale',
            week = '2',
            workspace_notes = 'aa',
            assigned_to = 'True'
        )

    def test_profile(self):
        self.assertEquals(str(self.profile2), 'Carbone Socio')

    def test_procedure(self):
        self.assertEquals(str(self.procedure), 'cambio olio aprire la bottiglia e cambiare olio')

    def test_competence(self):
        self.assertEquals(str(self.competence), 'Verifica Sterzata')

    def test_assignment(self):
        self.assertEquals(str(self.assignment), 'Venerdì, Settimana 2, Maintainer: Carbone Socio, 50 minuti nello slot 14-15')

    def test_activity(self):
        self.assertEquals(str(self.activity), '1 Planned Electrical, Competenze richieste: ')
    
    def test_activity2(self):
        self.assertEquals(str(self.activity2), '2 Unplanned Electrical, Competenze richieste: ')