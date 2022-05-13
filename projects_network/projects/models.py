from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=30, verbose_name='Name', unique=True)
    description = models.TextField(null=True, default=None, verbose_name='Description')
    beginning_date = models.DateField(auto_now_add=True, verbose_name='Beginning date')
    deadline = models.DateField(null=True, default=None, verbose_name='Deadline')
    end_date = models.DateField(null=True, default=None, verbose_name='End date')
    community = models.ForeignKey(
        to='communities.Community',
        on_delete=models.CASCADE,
        related_name='projects',
        verbose_name='Community',
    )
    supervisor = models.ForeignKey(
        to='users.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='driven_projects',
        verbose_name='Supervisor',
    )
    technologies = models.ManyToManyField(to='base.Technology', related_name='projects', verbose_name='Technologies')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        unique_together = ['community', 'supervisor']
