from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Name')
    description = models.TextField(null=True, default=None, verbose_name='Description')
    beginning_date = models.DateField(auto_now_add=True, blank=True, verbose_name='Beginning date')
    deadline = models.DateField(null=True, default=None, verbose_name='Deadline')
    end_date = models.DateField(null=True, default=None, blank=True, verbose_name='End date')
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
    participants = models.ManyToManyField(
        to='users.User',
        through='projects.ProjectParticipant',
        through_fields=('project', 'participant'),
        related_name='projects',
        verbose_name='Participants',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        unique_together = ['community', 'supervisor']


class ProjectParticipant(models.Model):
    project = models.ForeignKey(to='projects.Project', on_delete=models.CASCADE, verbose_name='Project')
    participant = models.ForeignKey(to='users.User', on_delete=models.CASCADE, verbose_name='Participant')
    project_role = models.ForeignKey(
        to='projects.ProjectRole',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Project role',
    )
    entry_date = models.DateField(auto_now_add=True, verbose_name='Entry date')

    def __str__(self):
        return f'{self.participant} in {self.project}'

    class Meta:
        verbose_name = 'Project participant'
        verbose_name_plural = 'Project participants'
        unique_together = ['project', 'participant']


class ProjectRole(models.Model):
    name = models.CharField(max_length=30, verbose_name='Name', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project role'
        verbose_name_plural = 'Project roles'


class Task(models.Model):
    title = models.TextField(verbose_name='Title')
    description = models.TextField(null=True, default=None, verbose_name='Description')
    creating_date = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Creating date')
    deadline = models.DateField(null=True, default=None, verbose_name='Deadline')
    end_date = models.DateField(null=True, default=None, blank=True, verbose_name='End date')
    status = models.ForeignKey(
        to='base.Status',
        on_delete=models.SET_NULL,
        null=True,
        related_name='tasks',
        verbose_name='Status',
    )
    project = models.ForeignKey(
        to='projects.Project',
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='Project',
    )
    executor = models.ForeignKey(
        to='users.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='received_tasks',
        verbose_name='Executor',
    )
    creator = models.ForeignKey(
        to='users.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_tasks',
        verbose_name='Creator',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
