from django.db import models

# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(null=True, blank=True, upload_to="images/")
    snipet = models.TextField(default="")
    description =models.TextField(default="")
    languages = models.ManyToManyField('Languages', through='LangCat',null=True, blank=True)
    softwars = models.ManyToManyField('Softwars', through='SofCat', null=True, blank=True)
    principles = models.ManyToManyField('Principles', through='PrinCat',null=True, blank=True)
    certificats = models.ManyToManyField('Certificats', through='CertCat',null=True, blank=True)
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Certificats(models.Model):
    titre = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    description = models.TextField(default="")
    picture = models.ImageField(null=True, blank=True, upload_to="images/")
    def __str__(self):
        """String for representing the Model object."""
        return self.titre

class Languages(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(null=True, blank=True, upload_to="images/")
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Softwars(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(null=True, blank=True, upload_to="images/")
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Principles(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="")
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class PrinCat(models.Model):
    principles = models.ForeignKey('Principles', on_delete=models.CASCADE)
    services = models.ForeignKey('Services', on_delete=models.CASCADE)

class CertCat(models.Model):
    certificats = models.ForeignKey('Certificats', on_delete=models.CASCADE)
    services = models.ForeignKey('Services', on_delete=models.CASCADE)

class SofCat(models.Model):
    certificats = models.ForeignKey('Softwars', on_delete=models.CASCADE)
    services = models.ForeignKey('Services', on_delete=models.CASCADE)

class LangCat(models.Model):
    title = models.CharField(max_length=255)
    certificats = models.ForeignKey('Languages', on_delete=models.CASCADE)
    services = models.ForeignKey('Services', on_delete=models.CASCADE)
