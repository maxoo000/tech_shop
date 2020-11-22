from django.db import models
from django.utils import timezone


# Create your models here.
class Proizvod(models.Model):
    ime = models.CharField(max_length=120, null=False, blank=False)
    naslovna_slika = models.ImageField(blank=False, null=False)
    cena = models.FloatField()
    datum_dodavanja = models.DateField(default=timezone.now)


class GrupaProizvoda(models.Model):
    proizvod = models.ForeignKey(Proizvod, on_delete=models.CASCADE)
    naziv_grupe = models.CharField(max_length=100, blank=False, null=False)


class SpecifikacijeProizvoda(models.Model):
    proizvod = models.ForeignKey(Proizvod, on_delete=models.CASCADE)
    naziv_specifikacije = models.CharField(max_length=60, blank=False, null=False)
    vrednost_specifikacije = models.CharField(max_length=200, blank=False, null=False)


class ProizvodiSlike(models.Model):
    proizvod = models.ForeignKey(Proizvod, on_delete=models.CASCADE)
    slika_proizvoda = models.ImageField(blank=False, null=False)
