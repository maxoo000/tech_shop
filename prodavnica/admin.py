from django.contrib import admin
from prodavnica.models import Proizvod, ProizvodiSlike, GrupaProizvoda, SpecifikacijeProizvoda

# Register your models here.
admin.site.register(Proizvod)
admin.site.register(ProizvodiSlike)
admin.site.register(GrupaProizvoda)
admin.site.register(SpecifikacijeProizvoda)
