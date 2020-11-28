from django.db import models
from django.contrib.auth.models import User

class Competence(models.Model):
    competenceName = models.CharField(max_length=30)
    listTask = models.TextField()

    def __str__(self):
        return(self.competenceName + ' ' + self.listTask)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    user_type = models.CharField(max_length = 20, choices = [
        ('SystemAdministrator', 'SystemAdministrator'),
        ('Planner', 'Planner'),
        ('Maintainer', 'Maintainer'),
    ])

    competences = models.ManyToManyField(Competence, blank=True, null=True)
    
    def __str__(self):
        return (self.user.last_name + ' ' + self.user.first_name + ' ' + self.user_type)

class Procedure(models.Model):
    procedureName = models.CharField(max_length=30, unique = True)
    procedureDescription = models.TextField()

    def __str__(self):
        return(self.procedureName + ' ' + self.procedureDescription)
