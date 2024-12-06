from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa



from .models import *
from .forms import *

# Create your views here.

class OrdreTransportListView(ListView):
    model = OrdreTransport
    template_name = "traitements/index.html"
    context_object_name = 'listes'
    


class OrdreTransportCreateView(CreateView):
    model = OrdreTransport
    form_class = OrdreTransportForm
    template_name = "traitements/create.html"
    success_url = reverse_lazy('traitements:create')



class OrdreTransportUpdateView(UpdateView):
    model = OrdreTransport
    form_class = OrdreTransportForm
    template_name = "traitements/update.html"
    success_url = reverse_lazy('traitements:index')
    context_object_name = "traitement" 
    
    
    def form_valid(self, form):
        messages.success(self.request, f"Modification effectuée avec succès !")
        return super().form_valid(form)
    
    


def render_to_pdf(request):
    idgesbl = request.POST.get('idgesbl')
    data = get_object_or_404(OrdreTransport, id=idgesbl)
    template_path = "traitements/imprimer.html"
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="liste_ecoles.pdf"'
    template = get_template(template_path)
    html = template.render({'data':data})
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response