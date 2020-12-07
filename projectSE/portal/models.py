from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Competence(models.Model):
    competenceName = models.CharField(max_length=30)
    listTask = models.TextField()

    def __str__(self):
        return(self.competenceName + ' ' + self.listTask)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    user_type = models.CharField(max_length=20, choices = [
        ('SystemAdministrator', 'SystemAdministrator'),
        ('Planner', 'Planner'),
        ('Maintainer', 'Maintainer'),
    ])

    competences = models.ManyToManyField(Competence, blank=True, null=True)
    
    def __str__(self):
        return (self.user.last_name + ' ' + self.user.first_name + ', ' + self.user_type)

class Procedure(models.Model):
    procedureName = models.CharField(max_length=30, unique = True)
    procedureDescription = models.TextField()

    def __str__(self):
        return(self.procedureName + ' ' + self.procedureDescription)

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

    def __str__(self):
        return(str(self.pk) + ' ' + self.activity_type + ' ' + self.activity_typology)
