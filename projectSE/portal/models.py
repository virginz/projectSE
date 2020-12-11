from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Procedure(models.Model):
    procedureName = models.CharField(max_length=30, unique = True)
    procedureDescription = models.TextField()

    def __str__(self):
        return(self.procedureName + ' ' + self.procedureDescription)

class Availability(models.Model):
    slot8_9 = models.IntegerField(default=0, validators=[MaxValueValidator(60), MinValueValidator(0)])
    slot9_10 = models.IntegerField(default=0, validators=[MaxValueValidator(60), MinValueValidator(0)])
    slot10_11 = models.IntegerField(default=0, validators=[MaxValueValidator(60), MinValueValidator(0)])
    slot11_12 = models.IntegerField(default=0, validators=[MaxValueValidator(60), MinValueValidator(0)])
    slot14_15 = models.IntegerField(default=0, validators=[MaxValueValidator(60), MinValueValidator(0)])
    slot15_16 = models.IntegerField(default=0, validators=[MaxValueValidator(60), MinValueValidator(0)])
    slot16_17 = models.IntegerField(default=0, validators=[MaxValueValidator(60), MinValueValidator(0)])
    day = models.CharField(max_length=20, choices = [
        ('Lunedì', 'Lunedì'),
        ('Martedì', 'Martedì'),
        ('Mercoledì', 'Mercoledì'),
        ('Giovedì', 'Giovedì'),
        ('Venerdì', 'Venerdì'),
        ('Sabato', 'Sabato'),
        ('Domenica', 'Domenica'),
    ])
    week = models.IntegerField(default=1, validators=[MaxValueValidator(52), MinValueValidator(1)])

    def __str__(self):

        return('Disponibilità giorno ' + str(self.day))

class Competence(models.Model):
    competenceName = models.CharField(max_length=30)
    listProcedure = models.ManyToManyField(Procedure, blank=True, null=True)

    def __str__(self):
        return(self.competenceName + ' ' + self.listTask)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    user_type = models.CharField(max_length=20, choices = [
        ('SystemAdministrator', 'SystemAdministrator'),
        ('Planner', 'Planner'),
        ('Maintainer', 'Maintainer'),
    ])

    disponibilita = models.ManyToManyField(Availability, blank= True, null=True)
    competences = models.ManyToManyField(Competence, blank=True, null=True)
    
    def __str__(self):
        return (self.user.last_name + ' ' + self.user.first_name + ', ' + self.user_type)

class Activity(models.Model):
    activity_type = models.CharField(max_length=20, choices = [
        ('Planned', 'Planned'),
        ('Unplanned', 'Unplanned'),
        ('Extra', 'Extra'),
    ])
    factory_site = models.CharField(max_length=20)
    factory_area = models.CharField(max_length=20)
    activity_typology = models.CharField(max_length=20, choices = [
        ('Electrical', 'Electrical'),
        ('Electronic', 'Electronic'),
        ('Hydraulic', 'Hydraulic'),
        ('Mechanical', 'Mechanical'),
    ])
    activity_description = models.TextField()
    estimation_time = models.PositiveIntegerField()
    interruptible = models.BooleanField(default=False)
    materials = models.TextField(blank=True, null=True)
    week = models.IntegerField(default=1, validators=[MaxValueValidator(52), MinValueValidator(1)])
    workspace_notes = models.TextField(blank=True, null=True)

    assigned_to = models.BooleanField(default=False)

    def __str__(self):
        return(str(self.pk) + ' ' + self.activity_type + ' ' + self.activity_typology)

class Assignment(models.Model):
    maintainer = models.ForeignKey(Profile, on_delete = models.CASCADE, limit_choices_to={'user_type': 'Maintainer'})
    attivita = models.ForeignKey(Activity, on_delete = models.CASCADE, unique=True)
   
