from django.db import models

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
    pass