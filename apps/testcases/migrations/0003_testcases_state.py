# Generated by Django 2.2.3 on 2019-07-10 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testcases', '0002_testcases_object_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcases',
            name='state',
            field=models.BooleanField(default=1),
        ),
    ]
