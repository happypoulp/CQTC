# -*- coding: utf-8 -*-

# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from datetime import datetime
from document import Contact
from forms import ContactForm

def index(request):
    form = ContactForm()
    print 0
    if request.method == 'POST': # If the form has been submitted...
        print 1
        form = ContactForm(request.POST) # A form bound to the POST data
        print 2
        if form.is_valid():
            print 3
            lastname = form.cleaned_data['lastname']
            firstname = form.cleaned_data['firstname']
            pseudo = form.cleaned_data['pseudo']
            code = form.cleaned_data['code']
            new_contact = Contact(firstname=firstname, lastname=lastname, pseudo=pseudo, code=code, created_on=datetime.now(), modified_on=datetime.now())
            new_contact.save()
            return HttpResponseRedirect('/') # Redirect after POST
        else:
            print 4
            form = ContactForm() # An unbound form

    print 5
    contacts = Contact.objects()
    return render_to_response('index.html', {
        'form': form,
        'contacts': contacts
    })
