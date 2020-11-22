from django.urls import path
from korisnici import views

urlpatterns = [
    path("", views.index, name="korisnik_pocetna"),

]