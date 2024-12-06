from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import PersonnelForm
from .models import Personnel



# Create your views here.
class PersonnelCreateView(CreateView):
    model = Personnel
    form_class = PersonnelForm
    template_name = "personnels/index.html"
    success_url = reverse_lazy('personnels:index')
    
    def form_valid(self, form):
        messages.success(self.request, f"Personnel {self.request.POST.get('nom')} ajouté avec succès !")
        return super().form_valid(form)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["personnels"] = Personnel.objects.order_by('-id')
        return context




class PersonnelUpdateView(UpdateView):
    model = Personnel
    form_class = PersonnelForm
    template_name = "personnels/update.html"
    success_url = reverse_lazy('personnels:index')
   
    
    
    def form_valid(self, form):
        messages.success(self.request, f"Personnel {self.request.POST.get('nom')} modifier avec succès")
        return super().form_valid(form)
    
    

class PersonnelDeleteView(DeleteView):
    model = Personnel
    form_class = PersonnelForm
    template_name = "personnels/index.html"
    success_url = reverse_lazy('personnels:index')
    
    
    def form_valid(self, form):
        obj = self.get_object()
        obj.delete()
        return super().form_valid(form)
      