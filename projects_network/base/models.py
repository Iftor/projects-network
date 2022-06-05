from django.db import models


class StatusConst:
    IN_PROCESS = "In process"
    DONE = "Done"


class Technology(models.Model):
    name = models.CharField(max_length=30, verbose_name='Name', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Technology'
        verbose_name_plural = 'Technologies'


class Status(models.Model):
    name = models.CharField(max_length=30, verbose_name='Name', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'
