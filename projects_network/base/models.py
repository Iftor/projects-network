from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='Name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Technology'
        verbose_name_plural = 'Technologies'
