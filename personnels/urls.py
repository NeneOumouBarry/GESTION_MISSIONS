from django.urls import path
from personnels import views

app_name='personnels'

urlpatterns = [
    path('', views.PersonnelCreateView.as_view(), name='index'),
    path('edit/<slug:slug>/', views.PersonnelUpdateView.as_view(), name='update'),
    path('delete/<slug:slug>/', views.PersonnelDeleteView.as_view(), name='delete')
]

