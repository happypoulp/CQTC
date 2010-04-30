from django.db import models

class Digi(models.Model):
    # user = models.ForeignKey(User)
    code = models.CharField(max_length=30)

    def __unicode__(self):
        return self.code

class User(models.Model):
    digi = models.ForeignKey(Digi)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    address = models.CharField(max_length=300)

    def __unicode__(self):
        return self.firstname + ' ' + self.lastname