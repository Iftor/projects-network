# Generated by Django 4.0.4 on 2022-05-22 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='custom_id',
            field=models.SlugField(null=True, unique=True, verbose_name='Custom id'),
        ),
    ]
