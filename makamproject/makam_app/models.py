from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


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
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f"{self.pk} - {self.eser_adi} - {self.creator} tarafından {self.created_date} tarihinde eklendi."

