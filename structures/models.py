from django.db import models

# Create your models here.

class Client(models.Model):
    pass

    class Meta:
        db_table = 'clients'