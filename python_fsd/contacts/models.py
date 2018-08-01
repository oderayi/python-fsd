# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Models

# Contact model
class Contacts(models.Model):
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  created_at = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.name
  class Meta:
    verbose_name_plural = 'Contacts'