from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Haven(models.Model):
    """Model representing a book genre."""
    plaatsnaam = models.CharField(max_length=200, help_text='vul plaats van de haven in')
    def __str__(self):
        """String for representing the Model object."""
        return self.plaatsnaam

class Soort_trip(models.Model):
    """Model representing a book genre."""
    soort_trip = models.CharField(max_length=200, help_text='vul soort trip in')
   
    
    class Meta: 
        verbose_name = "Soort trip"

    def __str__(self):
        """String for representing the Model object."""
        return self.soort_trip

class Boot(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    naam_boot = models.CharField(max_length=200)
    haven  = models.ForeignKey('Haven', on_delete=models.SET_NULL, null=True)
    plaatsen = models.IntegerField(default=0)
    schipper = models.CharField(max_length=200) 

    class Meta: 
        verbose_name = "Boot"
        verbose_name_plural = "Boten"
    
    def __str__(self):
        """String for representing the Model object."""
        return self.naam_boot
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('boot-details', args=[str(self.id)])

import uuid # Required for unique book instances

from django.contrib.auth.models import User

class Vistrip(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    soort_trip = models.ForeignKey('soort_trip', on_delete=models.SET_NULL, null=True) 
    boot = models.ForeignKey('Boot', on_delete=models.SET_NULL, null=True) 
    datum = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['datum']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.boot.naam_boot} ({self.datum})'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('vistrip-detail', args=[str(self.id)])

    def plek_over_count(self,):
        return self.boot.plaatsen - self.visplek_set.count()

    def reverveplek_over_count(self,):
        return self.boot.plaatsen+5 - self.visplek_set.count()

    def reverveplek_gebruiken(self,):
        return self.boot.plaatsen+1

class Visplek(models.Model):
    vistrip =  models.ForeignKey('Vistrip', on_delete=models.SET_NULL, null=True)
    visser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID')  

    class Meta: 
       verbose_name = "Visplek"
       verbose_name_plural = "Visplekken"
       permissions = (("can_addvisplek", "|Inschrijven voor visplek"),)   
       #unique_together = ['vistrip', 'visser']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.vistrip}'

    #https://books.agiliq.com/projects/django-admin-cookbook/en/latest/calculated_fields.html