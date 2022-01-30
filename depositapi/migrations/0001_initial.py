# Generated by Django 4.0.1 on 2022-01-29 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField(default='')),
                ('periods', models.SmallIntegerField(default=0)),
                ('amount', models.IntegerField(default=0)),
                ('rate', models.FloatField(default=0)),
                ('deposit', models.JSONField(default={})),
            ],
        ),
    ]
