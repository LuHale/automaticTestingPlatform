# Generated by Django 2.2.3 on 2019-08-20 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20190817_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='testcase_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testcases.Testcases'),
        ),
    ]
