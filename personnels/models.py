
from django.db import models
import secrets



class Personnel(models.Model):
    
    TYPES = [
        ('CHAUFFEUR', 'CHAUFFEUR'),
        ('RESP_TRANSPORT', 'RESPONSABLE TRANSPORT'),
        ('RESP_FLOTTE', 'RESPONSABLE fLOTTE'),
        ('CLIENT', 'CLIENT')
    ]
    
    matricule = models.CharField(max_length=10, verbose_name='Matricule ')
    nom = models.CharField(max_length=200, verbose_name='Nom complet ')
    type = models.CharField(max_length=100, choices=TYPES, verbose_name='Type ')
    fonction = models.CharField(max_length=200, verbose_name='Fonction ', blank=True)
    adresse = models.CharField(max_length=100, verbose_name='Adresse ')
    telephone = models.CharField(max_length=9, verbose_name='Téléphone ', unique=True, error_messages={'unique':'Le numéro de téléphone existe déjà'})
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return f"{self.nom} - {self.matricule}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = str(secrets.token_hex(7))
        super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'personnel'
        verbose_name = 'personnel'
        verbose_name_plural = 'personnels'
