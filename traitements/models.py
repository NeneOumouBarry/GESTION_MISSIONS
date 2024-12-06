from django.db import models
import secrets


from structures.models import SebTracteur, SebRemorque,Citerne,CodeColi,LieuLivraison,Destination
from personnels.models import Personnel


# Create your models here.


    
    
class OrdreTransport(models.Model):
    numero = models.CharField(max_length=150, verbose_name='Numero Ordre Transport ',blank=True, unique=True, error_messages={'unique': 'Ordre Transport existe déjà'})
    client = models.ForeignKey(Personnel, on_delete=models.SET_NULL, null=True,blank=True, verbose_name='Client ', related_name='ordre_transport_client')
    numero_fret = models.CharField(max_length=100,blank=True, verbose_name='Numéro Fret ')
    nature_colds = models.CharField(max_length=100,blank=True, verbose_name='Nature Colds ')
    code_coli = models.ForeignKey(CodeColi,blank=True, on_delete=models.SET_NULL, null=True, verbose_name='Code type Colis ')
    quantite_transporte = models.CharField(max_length=150,blank=True, verbose_name='Quantité transportée ')
    citerne = models.ForeignKey(Citerne,blank=True, on_delete=models.SET_NULL, null=True, verbose_name='Citerne ')
    numero_coli = models.CharField(max_length=150,blank=True, verbose_name='N° Colis ')
    numero_bc = models.CharField(max_length=100,blank=True, verbose_name='N° BC ')
    numero_bl = models.CharField(max_length=100,blank=True, verbose_name='N° BL ')
    transpQteTir = models.IntegerField(verbose_name='Transport Quantité ',blank=True,)
    seb_tracteur = models.ForeignKey(SebTracteur,blank=True, on_delete=models.SET_NULL, null=True, verbose_name='Seb Tracteur ')
    seb_remorque = models.ForeignKey(SebRemorque,blank=True, on_delete=models.SET_NULL, null=True, verbose_name='Seb Remorque ')
    chauffeur = models.ForeignKey(Personnel,blank=True, on_delete=models.SET_NULL, null=True, verbose_name='Chauffeur ', related_name='ordre_transport_chauffeur')
    date_chargement_prevu = models.DateField(blank=True,null=True,verbose_name='Date de chargement prévu ')
    heure_debut = models.CharField(max_length=100,blank=True, verbose_name='Heur début chargement ')
    lieu_chargement = models.CharField(max_length=100,blank=True, verbose_name='Lieu Chargement ')
    heure_fin = models.CharField(max_length=100,blank=True, verbose_name='Heure fin chargement ')
    destination = models.ForeignKey(Destination,blank=True, on_delete=models.SET_NULL, null=True, verbose_name='Destination ')
    depart = models.CharField(max_length=100,blank=True, verbose_name='Km Départ ')
    kilometrage = models.CharField(max_length=100,blank=True,verbose_name='Kilometrage prévu A/R ')
    date_depart_prevu = models.DateField(blank=True,verbose_name='Date de depart prevue ',null=True)
    dure_mission = models.CharField(max_length=150,blank=True, verbose_name='Estimation de durée de la mission ')
    lieu_livraison = models.ForeignKey(LieuLivraison,blank=True, on_delete=models.SET_NULL, null=True, verbose_name='Lieu Livraison ')
    date_arive_site = models.DateTimeField(blank=True,null=True,verbose_name='Date/heure arrivée site ')
    date_livraison_site = models.DateTimeField(auto_now=False,blank=True,null=True, auto_now_add=False, verbose_name='Date/heure livraison site ')
    date_depart_site = models.DateTimeField(auto_now=False,blank=True,null=True, auto_now_add=False, verbose_name='Date/heure départ site ')
    date_sortie_parc = models.DateTimeField(auto_now=False,blank=True,null=True, auto_now_add=False, verbose_name='Date/heure sortie parc ')
    date_retour_parc = models.DateTimeField(blank=True,null=True,verbose_name='Date/heure retour parc ')
    etat_conformite_coli = models.TextField(blank=True,verbose_name='Etat de conformité des colis livré ')
    nom_superviseur = models.ForeignKey(Personnel,blank=True, on_delete=models.SET_NULL, null=True, verbose_name='Superviseur UMS sur site ', related_name='ordre_transport_superviseur')
    sanction = models.CharField(max_length=150,blank=True, verbose_name='Sanction ')
    nom_responsable = models.ForeignKey(Personnel,blank=True, on_delete=models.SET_NULL, null=True, verbose_name='Responsable transport ', related_name='ordre_transport_responsable')
    nom_agent = models.ForeignKey(Personnel,blank=True, on_delete=models.SET_NULL, null=True, verbose_name='Agent sécurité ', related_name='ordre_transport_agent')
    nom_destinataire = models.ForeignKey(Personnel,blank=True, on_delete=models.SET_NULL, null=True, verbose_name='Destinaire ', related_name='ordre_transport_destinataire')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"Ordre Transport {self.numero}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = str(secrets.token_hex(7))
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'ordre_transport'
        verbose_name = 'ordre_transport'
        verbose_name_plural = 'ordre_transports'

    
    
    

