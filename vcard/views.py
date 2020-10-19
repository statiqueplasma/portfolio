from django.shortcuts import render
from django.views.generic import ListView
from .models import vcard
class vcard(ListView):
    model = vcard
    template_name= "vcard.html"

# Create your views here.
#def vcard(request):
#    vcard = vcard.
#    return render(request, 'vcard.html', {'vcard':vcard})