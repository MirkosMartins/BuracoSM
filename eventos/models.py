# -*- coding: cp1252 -*-
from django.contrib.gis.db import models
from django.contrib.auth.models import User
import django_facebook

# Create your models here.

class Tipo(models.Model):
  nome = models.CharField(max_length=200)
  desc = models.TextField()
  icon = models.CharField(max_length=100)

  def __unicode__(self):
    return "%s" % self.nome


class Evento(models.Model):
#  tipo = models.ForeignKey(Tipo)
  titulo = models.CharField(max_length=200, verbose_name=u"Nome do Buraco")
  posicao = models.PointField()
  foto = models.ImageField(upload_to="buracosdosusuarios", blank=True, null=True)
  objects = models.GeoManager()
  usuario = models.ForeignKey('django_facebook.FacebookCustomUser')

  def __unicode__(self):
    return self.titulo

  class Meta:
    ordering = ["-id", "titulo"]
