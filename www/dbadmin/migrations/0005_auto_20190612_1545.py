# Generated by Django 2.2.2 on 2019-06-12 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbadmin', '0004_outcomes_reviewer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Outcomes',
            new_name='Outcome',
        ),
    ]
