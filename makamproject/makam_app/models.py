from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

# sadece isimleri kaydettim


class Makam(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class Usul(models.Model):
    name = models.CharField(max_length=127)

    def __str(self):
        return self.name


class Piece(models.Model):
    eser_adi = models.CharField(max_length=127)
    bestekar = models.CharField(max_length=127)
    yuzyil = models.IntegerField()
    gufte_yazari = models.CharField(max_length=127)
    gufte_vezin = models.CharField(max_length=127)
    gufte_nazim_bicim = models.CharField(max_length=127)
    gufte_nazim_tur = models.CharField(max_length=127)
    makam = models.JSONField()
    usul = models.JSONField()
    form = models.CharField(max_length=127)
    subcomponents = models.JSONField()
