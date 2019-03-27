from django.db import models
from datetime import datetime


class Zamestnanec(models.Model):
    idZam = models.IntegerField()
    jmeno = models.CharField(max_length=30)
    prijmeni = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    datum_narozeni = models.DateField()

    def __str__(self):
        return self.jmeno + " " + self.prijmeni + " " + self.email


class Zakaznik(models.Model):
    idZak = models.IntegerField()
    jmeno = models.CharField(max_length=30)
    prijmeni = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    datum_narozeni = models.DateField()

    def __str__(self):
        return self.jmeno + " " + self.prijmeni + " " + self.email


class Prostor(models.Model):
    idSpr = models.IntegerField()
    vzdalenost = models.FloatField()
    popis = models.CharField(max_length=100)

    def __str__(self):
        return self.popis


class Zbran(models.Model):
    idZbr = models.IntegerField()
    nazev = models.CharField(max_length=30)
    typ_zbrane = models.CharField(max_length=30)
    raze = models.FloatField()
    rok_vyroby = models.IntegerField()

    def __str__(self):
        return self.nazev + " " + self.typ_zbrane + " " + str(self.rok_vyroby)


class Strelba(models.Model):
    idStr = models.IntegerField()
    zacatek = models.DateTimeField()
    konec = models.DateTimeField()
    idZbr = models.ForeignKey('Zbran')
    idZam = models.ForeignKey('Zamestnanec')
    idZak = models.ForeignKey('Zakaznik')
    idSpr = models.ForeignKey('Prostor')


class Rezervace(models.Model):
    idRez = models.IntegerField()
    datumVytvoreni = models.DateTimeField(default=datetime.now)
    datumStrelby = models.DateTimeField()
    idZak = models.ForeignKey('Zakaznik')
    idSpr = models.ForeignKey('Prostor')
    idZbr = models.ForeignKey('Zbran')





# Create your models here.
