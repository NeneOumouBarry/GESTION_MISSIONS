from django.urls import path
from traitements import views

app_name='traitements'

urlpatterns = [
    path('listes/', views.OrdreTransportListView.as_view(), name='index'),
    path('create/', views.OrdreTransportCreateView.as_view(), name='create'),
    path('update/<slug:slug>/', views.OrdreTransportUpdateView.as_view(), name='update'),
    path('imprimer-ordre-transport/', views.render_to_pdf, name='render_to_pdf')
   
    
]
