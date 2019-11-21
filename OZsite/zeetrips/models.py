from django.db import models

class Haven(models.Model):
    """Model representing a book genre."""
    plaatsnaam = models.CharField(max_length=200, help_text='vul plaats van de haven in')
    def __str__(self):
        """String for representing the Model object."""
        return self.plaatsnaam


class Boot(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    naam = models.CharField(max_length=200)
    haven  = models.ForeignKey('Haven', on_delete=models.SET_NULL, null=True)
    plaatsen = models.IntegerField(default=0)
    schipper = models.CharField(max_length=200) 

    class Meta: 
        verbose_name = "Boot"
        verbose_name_plural = "Boten"
    
    def __str__(self):
        """String for representing the Model object."""
        return self.naam
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('boot-details', args=[str(self.id)])

import uuid # Required for unique book instances

from django.contrib.auth.models import User

class Vistrip(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unieke ID voor deze trip')
    datum = models.DateField(null=True, blank=True)
    boot = models.ForeignKey('Boot', on_delete=models.SET_NULL, null=True) 
    vissers = models.ManyToManyField(User)
   
    class Meta:
        ordering = ['datum']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.boot.naam} ({self.datum})'