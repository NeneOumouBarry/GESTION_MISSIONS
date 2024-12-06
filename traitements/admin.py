from django.contrib import admin
from .models import OrdreTransport


# Register your models here.
@admin.register(OrdreTransport)
class OrdreTransportAdmin(admin.ModelAdmin):
    list_display = ('numero', 'client', 'numero_fret', 'code_coli', 'quantite_transporte', 'citerne', 'numero_coli', 'numero_bc', 'numero_bl')