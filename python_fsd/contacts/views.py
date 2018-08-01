# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Contacts

# Homepage
def index(request):

  contacts = Contacts.objects.all()[:10]

  context = {
      'title': 'My Contacts',
      'contacts': contacts
  }
  return render(request, 'contacts/index.html', context)

def details(request, id):
  contact = Contacts.objects.get(id=id)

  context = {
    'contact': contact
  }

  return render(request, 'contacts/details.html', context)
