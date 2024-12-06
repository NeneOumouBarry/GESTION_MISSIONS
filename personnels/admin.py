from django.contrib import admin
from .models import Personnel

# Register your models here.
@admin.register(Personnel)
class PersonnelAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type', 'fonction', 'adresse', 'telephone')
