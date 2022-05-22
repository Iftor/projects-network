from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    technologies = models.ManyToManyField(to='base.Technology', related_name='users', verbose_name='Technologies')
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
