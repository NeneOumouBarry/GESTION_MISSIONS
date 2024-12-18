# Generated by Django 5.1.3 on 2024-11-25 15:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodeColi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, verbose_name='Code ')),
                ('libelle', models.CharField(max_length=100, verbose_name='Libellé')),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, verbose_name='Code')),
                ('libelle', models.CharField(max_length=100, verbose_name='Libellé')),
            ],
        ),
        migrations.CreateModel(
            name='Flotte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, verbose_name='Code ')),
                ('libelle', models.CharField(max_length=100, verbose_name='Libellé')),
            ],
        ),
        migrations.CreateModel(
            name='LieuLivraison',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texte', models.CharField(max_length=100, verbose_name='Texte ')),
                ('kilometrage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Citerne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, verbose_name='Code')),
                ('libelle', models.CharField(max_length=100, verbose_name='Libellé')),
                ('immatriculation', models.CharField(max_length=50, verbose_name='Immatriculation ')),
                ('flotte', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='structures.flotte', verbose_name='Flotte ')),
            ],
        ),
        migrations.CreateModel(
            name='SebRemorque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, verbose_name='Code')),
                ('libelle', models.CharField(max_length=100, verbose_name='Libellé')),
                ('immatriculation', models.CharField(max_length=50, verbose_name='Immatriculation ')),
                ('flotte', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='structures.flotte', verbose_name='Flotte ')),
            ],
        ),
        migrations.CreateModel(
            name='SebTracteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, verbose_name='Code')),
                ('libelle', models.CharField(max_length=100, verbose_name='Libellé')),
                ('immatriculation', models.CharField(max_length=50, verbose_name='Immatriculation ')),
                ('flotte', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='structures.flotte', verbose_name='Flotte ')),
            ],
        ),
    ]
