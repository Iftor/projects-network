# Generated by Django 4.0.4 on 2022-05-13 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('communities', '0002_communityparticipant_community_participants_and_more'),
        ('base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Name')),
                ('description', models.TextField(default=None, null=True, verbose_name='Description')),
                ('beginning_date', models.DateField(auto_now_add=True, verbose_name='Beginning date')),
                ('deadline', models.DateField(default=None, null=True, verbose_name='Deadline')),
                ('end_date', models.DateField(default=None, null=True, verbose_name='End date')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='communities.community', verbose_name='Community')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='ProjectRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Project role',
                'verbose_name_plural': 'Project roles',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Title')),
                ('description', models.TextField(default=None, null=True, verbose_name='Description')),
                ('creating_date', models.DateTimeField(auto_now_add=True, verbose_name='Creating date')),
                ('deadline', models.DateField(default=None, null=True, verbose_name='Deadline')),
                ('end_date', models.DateField(default=None, null=True, verbose_name='End date')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_tasks', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('executor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='received_tasks', to=settings.AUTH_USER_MODEL, verbose_name='Executor')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='projects.project', verbose_name='Project')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to='base.status', verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
        migrations.CreateModel(
            name='ProjectParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField(auto_now_add=True, verbose_name='Entry date')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Participant')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project', verbose_name='Project')),
                ('project_role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.projectrole', verbose_name='Project role')),
            ],
            options={
                'verbose_name': 'Project participant',
                'verbose_name_plural': 'Project participants',
                'unique_together': {('project', 'participant')},
            },
        ),
        migrations.AddField(
            model_name='project',
            name='participants',
            field=models.ManyToManyField(related_name='projects', through='projects.ProjectParticipant', to=settings.AUTH_USER_MODEL, verbose_name='Participants'),
        ),
        migrations.AddField(
            model_name='project',
            name='supervisor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='driven_projects', to=settings.AUTH_USER_MODEL, verbose_name='Supervisor'),
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(related_name='projects', to='base.technology', verbose_name='Technologies'),
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together={('community', 'supervisor')},
        ),
    ]