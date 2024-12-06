from django.db import models
import secrets

# Create your models here.
        
class CodeColi(models.Model):
   code = models.CharField( max_length=50, verbose_name='Code ')
   libelle = models.CharField( max_length=100, verbose_name='Libellé' )
   
   def __str__(self):
        return self.libelle
   
class Flotte(models.Model):
    code = models.CharField( max_length=50, verbose_name='Code ')
    libelle = models.CharField( max_length=100, verbose_name='Libellé' )
    
    
    def __str__(self):
        return self.libelle

class Citerne(models.Model):
    code = models.CharField( max_length=50, verbose_name='Code' )
    libelle = models.CharField( max_length=100, verbose_name='Libellé' )
    immatriculation = models.CharField( max_length=50, verbose_name='Immatriculation ')
    flotte = models.ForeignKey(Flotte, on_delete=models.SET_NULL, null=True, verbose_name='Flotte ')
    
    def __str__(self):
        return f"{self.code} - {self.libelle}"
    

class SebTracteur(models.Model):
    code = models.CharField( max_length=50, verbose_name='Code' )
    libelle = models.CharField( max_length=100, verbose_name='Libellé' )
    immatriculation = models.CharField( max_length=50, verbose_name='Immatriculation ')
    flotte = models.ForeignKey(Flotte, on_delete=models.SET_NULL, null=True, verbose_name='Flotte ')
    
    def __str__(self):
        return f"{self.code} - {self.libelle}"

class SebRemorque(models.Model):
    code = models.CharField( max_length=50, verbose_name='Code' )
    libelle = models.CharField( max_length=100, verbose_name='Libellé' )
    immatriculation = models.CharField( max_length=50, verbose_name='Immatriculation ')
    flotte = models.ForeignKey(Flotte, on_delete=models.SET_NULL, null=True, verbose_name='Flotte ')
    
    def __str__(self):
        return f"{self.code} - {self.libelle}"

class Destination(models.Model):
    code = models.CharField( max_length=50, verbose_name='Code' )
    libelle = models.CharField( max_length=100, verbose_name='Libellé' )
    
    def __str__(self):
        return self.libelle
    

class LieuLivraison(models.Model):
    texte = models.CharField(max_length=100, verbose_name='Texte ')
    kilometrage = models.IntegerField()
    
    
    def __str__(self):
        return self.libelle
