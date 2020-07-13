from django.db import models


class Lehrveranstaltungen(models.Model):
    name=models.CharField(max_length=35)

    def __str__(self):
        return f'{self.name} '

    def rel(self):
        all_st = self.studierende_set.all()
        li = ', '.join([f'[{a.vorname} {a.nachname}, {a.bereich}] ' for a in all_st])
        return f'{li}'

class Studierende(models.Model):
    vorname=models.CharField(max_length=30)
    nachname = models.CharField(max_length=30)
    matrikelNummer=models.CharField(max_length=12)
    bereich = models.CharField(max_length=30)
    lehrveranstaltung = models.ManyToManyField(Lehrveranstaltungen)

    def __str__(self):
         SS= f'{self.vorname} {self.nachname} '
         return  SS
