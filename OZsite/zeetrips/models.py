from django.db import models

class Haven(models.Model):
    """Model representing a book genre."""
    plaatsnaam = models.CharField(max_length=200, help_text='vul plaats van de haven in')
    def __str__(self):
        """String for representing the Model object."""
        return self.plaatsnaam


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
    id = models.AutoField(primary_key=True, default=0)
    datum = models.DateField(null=True, blank=True)
    boot = models.ForeignKey('Boot', on_delete=models.SET_NULL, null=True) 

    class Meta:
        ordering = ['datum']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.boot.naam_boot} ({self.datum})'


class Visplek(models.Model):
    vistrip =  models.ForeignKey('Vistrip', on_delete=models.SET_NULL, null=True)
    visser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.vistrip} ({self.visser})'