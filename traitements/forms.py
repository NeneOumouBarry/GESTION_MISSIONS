from django import forms
from .models import OrdreTransport
from django.shortcuts import get_list_or_404
from personnels.models import Personnel


class OrdreTransportForm(forms.ModelForm):
    class Meta:
        model = OrdreTransport
        exclude = ['slug']
        widgets = {
            'numero':forms.TextInput(attrs={'class':'form-control'}),
            'client':forms.Select(attrs={'class': 'select2 select2-hidden-accessible'}),
            'numero_fret':forms.TextInput(attrs={'class': 'form-control'}),
            'nature_colds':forms.TextInput(attrs={'class':'form-control'}),
            'code_coli':forms.Select(attrs={'class': 'select2 select2-hidden-accessible'}),
            'quantite_transporte': forms.TextInput(attrs={'class': 'form-control'}),
            'citerne': forms.Select(attrs={'class':'select2 select2-hidden-accessible'}),
            'numero_coli':forms.TextInput(attrs={'class':'form-control'}),
            'numero_bc':forms.TextInput(attrs={'class':'form-control'}),
            'numero_bl':forms.TextInput(attrs={'class':'form-control'}),
            'transpQteTir':forms.TextInput(attrs={'class':'form-control', 'type':'number'}),
            'seb_tracteur':forms.Select(attrs={'class': 'select2 select2-hidden-accessible'}),
            'seb_remorque':forms.Select(attrs={'class': 'select2 select2-hidden-accessible'}),
            'chauffeur':forms.Select(attrs={'class': 'select2 select2-hidden-accessible'}),
            'date_chargement_prevu':forms.TextInput(attrs={'type':'date'}),
            'heure_debut':forms.TextInput(attrs={'type':'time'}),
            'lieu_chargement':forms.TextInput(attrs={'class':'form-control'}),
            'heure_fin':forms.TextInput(attrs={'type':'time'}),
            'destination':forms.Select(attrs={'class': 'select2 select2-hidden-accessible'}),
            'depart':forms.TextInput(attrs={'class':'form-control'}),
            'kilometrage':forms.TextInput(attrs={'class':'form-control'}),
            'date_depart_prevu':forms.TextInput(attrs={'type':'date'}),
            'dure_mission':forms.TextInput(attrs={'class':'form-control'}),
            'lieu_livraison':forms.Select(attrs={'class': 'select2 select2-hidden-accessible'}),
            'date_arive_site':forms.TextInput(attrs={'type':'date'}),
            'date_livraison_site':forms.TextInput(attrs={'type':'date'}),
            'date_depart_site':forms.TextInput(attrs={'type':'date'}),
            'date_sortie_parc':forms.TextInput(attrs={'type':'date'}),
            'date_retour_parc':forms.TextInput(attrs={'type':'date'}),
            'etat_conformite_coli':forms.Textarea(attrs={'rows':3,'cols':3}),
            'fonction_destinateur':forms.TextInput(attrs={'class':'form-control'}),
            'nom_superviseur':forms.Select(attrs={'class': 'select2 select2-hidden-accessible'}),
            'sanction':forms.TextInput(attrs={'class':'form-control'}),
            'nom_responsable':forms.Select(attrs={'class': 'select2 select2-hidden-accessible'}),
            'nom_agent':forms.Select(attrs={'class': 'select2 select2-hidden-accessible'}),
            'nom_destinataire':forms.Select(attrs={'class': 'select2 select2-hidden-accessible'}),
           
        }   

    def __init__(self, *args, **kwargs):
        super(OrdreTransportForm, self).__init__(*args, **kwargs)
        self.fields['chauffeur'].queryset = Personnel.objects.filter(type='CHAUFFEUR')
        self.fields['nom_agent'].queryset  = Personnel.objects.filter(type='AGENT_SECURITE')
        self.fields['nom_responsable'].queryset = Personnel.objects.filter(type='RESP_TRANSPORT')
        self.fields['nom_destinataire'].queryset = Personnel.objects.filter(type='DESTINATAIRE')
        self.fields['nom_superviseur'].queryset = Personnel.objects.filter(type='SUPERVISEUR')
        self.fields['client'].queryset = Personnel.objects.filter(type='CLIENT')
            
     
        
        
        
            
                
        
        