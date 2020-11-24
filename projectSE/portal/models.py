from django.db import models
from django.contrib.auth.models import User

class Competences(models.Model):
    competencesName = models.CharField(max_length=30)
    listTask = models.TextField()

    def __str__(self):
        return(self.competencesName + ' ' + self.listTask)

class SystemUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    role = models.CharField(max_length = 20, choices = [
        ('SystemAdministrator', 'SystemAdministrator'),
        ('Planner', 'Planner'),
        ('Maintainer', 'Maintainer'),
    ])

    competences = models.ManyToManyField(Competences, blank=True, null=True)
    
    def __str__(self):
        return (self.user.last_name + ' ' + self.user.first_name)