from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(CodeColi)
class CodeColiAdmin(admin.ModelAdmin):
    list_display = ('code', 'libelle')
    
    
@admin.register(Flotte)
class FlotteAdmin(admin.ModelAdmin):
    list_display = ('code', 'libelle')
    
@admin.register(Citerne)    
class CiterneAdmin(admin.ModelAdmin):
    list_display = ('code', 'libelle', 'immatriculation', 'flotte')

@admin.register(SebTracteur)
class SebTracteurAdmin(admin.ModelAdmin):
    list_display = ('code', 'libelle', 'immatriculation', 'flotte')

@admin.register(SebRemorque)
class SebRemorqueAdmin(admin.ModelAdmin):
    list_display = ('code', 'libelle', 'immatriculation', 'flotte')

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('code', 'libelle')
