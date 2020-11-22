from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Korisnik(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ime = models.CharField(max_length=100, blank=False, null=False)
    prezime = models.CharField(max_length=100, blank=False, null=False)
    datum_rodjenja = models.DateField(blank=False, null=False)
    vreme_kreiranja_naloga = models.DateTimeField(default=timezone.now)
    adresa = models.CharField(max_length=200, blank=False, null=False)


