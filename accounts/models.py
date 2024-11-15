from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
import secrets
from django.contrib.auth.models import PermissionsMixin
from autoslug import AutoSlugField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.conf import settings

User = settings.AUTH_USER_MODEL

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Vous devez entrer un email")
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE = (
        ('Administrateur', 'Administrateur'),
        ('Utilisateur', 'Utilisateur')
    )
    nomcomplet = models.CharField(max_length=100, verbose_name="Nom et Prénom : ")
    slug = AutoSlugField(unique=True, editable=False)
    adresse = models.CharField(max_length=100, verbose_name="Adresse : ")
    telephone = models.CharField(max_length=100, verbose_name="Téléphone : ",blank=True)
    email = models.EmailField(
        unique=True, max_length=255, verbose_name="Email : ")
    image = models.ImageField(upload_to="users/images",
                              verbose_name="Photo : ", blank=True, null=True)
    role = models.CharField(max_length=100, choices=ROLE, verbose_name="Rôle : ")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    active = models.BooleanField(blank=True, default=False)

    USERNAME_FIELD = "email"
    objects = MyUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def imageUrl(self):
        try:
          url = self.image.url
        except:
          url = ''
        return url
    
    def save(self, *args, **kwargs):
       self.slug = secrets.token_hex(16)
       super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.email)
  
    
    class Meta:
        db_table = "customusers"
        verbose_name = "CustomUser"
        verbose_name_plural = "CustomUser"








