from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(null=True, blank=True, upload_to="images/")
    snipet = models.TextField(default="")
    description =models.TextField(default="")
    languages = models.ManyToManyField('Language', through='LangCat', blank=True)
    softwars = models.ManyToManyField('Softwar', through='SofCat', blank=True)
    principles = models.ManyToManyField('Principle', through='PrinCat', blank=True)
    certificats = models.ManyToManyField('Certificat', through='CertCat', blank=True)
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Certificat(models.Model):
    titre = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    description = models.TextField(default="")
    services = models.ManyToManyField('Service', through='CertCat', blank=True)
    picture = models.ImageField(null=True, blank=True, upload_to="images/")
    def __str__(self):
        """String for representing the Model object."""
        return self.titre

class Language(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(null=True, blank=True, upload_to="images/")
    services = models.ManyToManyField('Service', through='LangCat', blank=True)
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Softwar(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(null=True, blank=True, upload_to="images/")
    services = models.ManyToManyField('Service', through='SofCat', blank=True)
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Principle(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="")
    services = models.ManyToManyField('Service', through='PrinCat', blank=True)
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class PrinCat(models.Model):
    principles = models.ForeignKey('Principle', on_delete=models.CASCADE)
    services = models.ForeignKey('Service', on_delete=models.CASCADE)
    def __str__(self):
        """String for representing the Model object."""
        return str(self.principles) + ' | ' + str(self.services)

class CertCat(models.Model):
    certificats = models.ForeignKey('Certificat', on_delete=models.CASCADE)
    services = models.ForeignKey('Service', on_delete=models.CASCADE)
    def __str__(self):
        """String for representing the Model object."""
        return str(self.certificats) + ' | ' + str(self.services)

class SofCat(models.Model):
    softwars = models.ForeignKey('Softwar', on_delete=models.CASCADE)
    services = models.ForeignKey('Service', on_delete=models.CASCADE)
    def __str__(self):
        """String for representing the Model object."""
        return str(self.softwars) + ' | ' + str(self.services)

class LangCat(models.Model):
    languages = models.ForeignKey('Language', on_delete=models.CASCADE)
    services = models.ForeignKey('Service', on_delete=models.CASCADE)
    def __str__(self):
        """String for representing the Model object."""
        return str(self.languages) + ' | ' + str(self.services)