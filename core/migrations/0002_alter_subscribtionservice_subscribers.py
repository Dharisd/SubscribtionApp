# Generated by Django 3.2.4 on 2021-06-11 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribtionservice',
            name='subscribers',
            field=models.ManyToManyField(blank=True, null=True, to='core.Subscriber'),
        ),
    ]
