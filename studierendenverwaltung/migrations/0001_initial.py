# Generated by Django 3.0.5 on 2020-05-03 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lehrveranstaltungen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Studierende',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vorname', models.CharField(max_length=30)),
                ('nachname', models.CharField(max_length=30)),
                ('matrikelNummer', models.CharField(max_length=12)),
                ('bereich', models.CharField(max_length=30)),
                ('lehrveranstaltung', models.ManyToManyField(to='studierendenverwaltung.Lehrveranstaltungen')),
            ],
        ),
    ]
