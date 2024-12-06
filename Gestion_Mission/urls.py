
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views



urlpatterns = [
    path('', views.dashboard, name='accueil'),
    path('admin/backend/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('admin/ges-missions/affectations/',include('affectations.urls')),
    path('admin/ges-missions/structures/',include('structures.urls')),
    path('admin/ges-missions/traitements/',include('traitements.urls')),
    path('admin/ges-missions/personnels/',include('personnels.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
