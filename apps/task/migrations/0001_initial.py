# Generated by Django 2.2.3 on 2019-08-20 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(default=None)),
                ('product_id', models.IntegerField(default=None)),
                ('testcases', models.CharField(max_length=2048)),
                ('execute_ways', models.IntegerField(choices=[(1, '单次'), (2, '多次'), (3, '循环')])),
                ('times', models.IntegerField()),
            ],
            options={
                'db_table': 'task',
            },
        ),
    ]
