from django import forms
from .models import Personnel

class PersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        exclude = ['slug']
        widgets = {
            'matricule':forms.TextInput(attrs={'class':'form-control'}),
            'nom':forms.TextInput(attrs={'class':'form-control'}),
            'type':forms.Select(attrs={'class': 'select2 select2-hidden-accessible'}),
            'fonction':forms.TextInput(attrs={'class': 'form-control'}),
            'adresse':forms.TextInput(attrs={'class': 'form-control'}),
            'telephone':forms.TextInput(attrs={'class': 'form-control', 'type':'number'})
        }
    
    