# Generated by Django 2.0.5 on 2018-06-01 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_modules', '0002_auto_20180601_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='students',
            field=models.ManyToManyField(related_name='modules', to='student.Student'),
        ),
    ]
