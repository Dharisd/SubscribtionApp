# Generated by Django 3.2.4 on 2021-06-11 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SubscribtionService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('billing_cycle', models.IntegerField()),
                ('subscribers', models.ManyToManyField(to='core.Subscriber')),
            ],
        ),
        migrations.CreateModel(
            name='Subscribtion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_at', models.DateField(blank=True, null=True)),
                ('cancelled_at', models.DateField(blank=True, null=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subscribtionservice')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subscriber')),
            ],
            options={
                'unique_together': {('subscriber', 'service')},
            },
        ),
    ]