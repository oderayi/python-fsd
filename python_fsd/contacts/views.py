# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import Contacts
from .forms import ContactForm

# Homepage

def index(request):
  context = {
      'title': 'Welcome',
  }
  return render(request, 'contacts/index.html', context)

# Contacts list
def contacts(request):

  contacts = Contacts.objects.all()[:10]

  context = {
      'title': 'My Contacts',
      'contacts': contacts
  }
  return render(request, 'contacts/list.html', context)

# Contact creation page
def create(request):
  if request.method == "POST":
    form = ContactForm(request.POST)
    if form.is_valid():
      contact = form.save(commit=False)
      contact.name = request.POST.get('name')
      contact.email = request.POST.get('email')
      contact.save()
      return redirect('details', id=contact.pk)
  else:
    form = ContactForm()

    context = {
        'title': 'Add Contact',
        'form': form
    }
  return render(request, 'contacts/contact_edit.html', context)

# Contact details
def details(request, id):
  contact = Contacts.objects.get(id=id)

  context = {
    'contact': contact
  }

  return render(request, 'contacts/details.html', context)
