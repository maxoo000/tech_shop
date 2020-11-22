from django.shortcuts import render
from prodavnica.models import Proizvod
# Create your views here.
def index(request):
    jedan = Proizvod.objects.all()[0]
    
    
    
    return render(request, "korisnici/korisnici.html", {"pr": jedan})
