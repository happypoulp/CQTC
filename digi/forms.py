# -*- coding: utf-8 -*-

from django import forms

class ContactForm(forms.Form):
    firstname = forms.CharField(max_length=50, required=True)
    lastname = forms.CharField(max_length=50)
    pseudo = forms.CharField(max_length=30)
    code = forms.CharField(max_length=20)

