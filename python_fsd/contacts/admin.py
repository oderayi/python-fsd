# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register contacts models with the admin dashboard
from .models import Contacts

admin.site.register(Contacts)
