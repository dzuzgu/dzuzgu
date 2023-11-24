from django.db import models
# from django.contrib.auth.models import BaseUserManager
# from django.conf import settings


class Coworker(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    profession = models.CharField(max_length=30, null=False)
    salary = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Contact(models.Model):
    name = models.CharField(max_length=30, null=False)
    surname = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=30, null=False)
    message = models.TextField(max_length=500, null=False)

    def __str__(self):
        return f'{self.name} {self.surname}'
