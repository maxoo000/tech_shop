from django.db import models
from korisnici.models import Korisnik
from prodavnica.models import Proizvod

# Create your models here.
class Korpa(models.Model):
    naziv_korpe = models.CharField(max_length=100, default="Neimenovana korpa", null=False)

class SadrzajKorpe(models.Model):
    korpa = models.ForeignKey(Korpa, on_delete=models.CASCADE)
    proizvod = models.ForeignKey(Proizvod, on_delete=models.CASCADE)








