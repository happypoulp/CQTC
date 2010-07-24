# -*- coding: utf-8 -*-

# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from datetime import datetime
from document import Contact
from forms import ContactForm

def index(request):
    form = ContactForm()
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            lastname = form.cleaned_data['lastname']
            firstname = form.cleaned_data['firstname']
            pseudo = form.cleaned_data['pseudo']
            code = form.cleaned_data['code']
            new_contact = Contact(firstname=firstname, lastname=lastname, pseudo=pseudo, code=code, created_on=datetime.now(), modified_on=datetime.now())
            new_contact.save()
            return HttpResponseRedirect('/') # Redirect after POST
        else:
            form = ContactForm() # An unbound form
    
    contacts = Contact.objects()
    return render_to_response('index.html', {
        'form': form,
        'contacts': contacts
    })

def edit(request, contact):
    contact = Contact.objects(id=contact)[0]
    form = ContactForm({'firstname': contact.firstname, 'lastname': contact.lastname, 'code': contact.code or ' ', 'pseudo': contact.pseudo})
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            lastname = form.cleaned_data['lastname']
            firstname = form.cleaned_data['firstname']
            pseudo = form.cleaned_data['pseudo']
            code = form.cleaned_data['code']
            contact.firstname = firstname
            contact.lastname = lastname
            contact.code = code
            contact.pseudo = pseudo
            contact.save()
        else:
            form = ContactForm({'firstname': firstname, 'lastname': lastname, 'code': code or ' ', 'pseudo': pseudo})
    
    return render_to_response('edit.html', {
        'form': form,
        'contact': contact
    })

def delete(request, contact):
    contact = Contact.objects(id=contact)[0]
    contact.delete()
    return HttpResponseRedirect('/')
