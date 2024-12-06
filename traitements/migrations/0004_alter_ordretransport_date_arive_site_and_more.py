# Generated by Django 5.1.3 on 2024-11-26 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traitements', '0003_alter_ordretransport_date_chargement_prevu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordretransport',
            name='date_arive_site',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date/heure arrivée site '),
        ),
        migrations.AlterField(
            model_name='ordretransport',
            name='date_depart_prevu',
            field=models.DateField(blank=True, null=True, verbose_name='Date de depart prevue '),
        ),
        migrations.AlterField(
            model_name='ordretransport',
            name='date_depart_site',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date/heure départ site '),
        ),
        migrations.AlterField(
            model_name='ordretransport',
            name='date_livraison_site',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date/heure livraison site '),
        ),
        migrations.AlterField(
            model_name='ordretransport',
            name='date_retour_parc',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date/heure retour parc '),
        ),
        migrations.AlterField(
            model_name='ordretransport',
            name='date_sortie_parc',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date/heure sortie parc '),
        ),
    ]
