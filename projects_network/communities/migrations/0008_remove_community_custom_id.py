# Generated by Django 4.0.4 on 2022-05-23 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0007_alter_community_custom_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='custom_id',
        ),
    ]
