# -*- coding: utf-8 -*-

from mongoengine import *

class Contact(Document):
    firstname = StringField()
    lastname = StringField()
    pseudo = StringField()
    code = StringField()
    created_on = DateTimeField()
    changed_on = DateTimeField()
