from django.db import models


from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Haven(models.Model):
    """Model representing a book genre."""
    naam = models.CharField(max_length=200, help_text='vul plaats van de haven in')
    
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('Haven-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.naam

class Boot(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    naam = models.CharField(max_length=200)
    haven  = models.ForeignKey('Haven', on_delete=models.SET_NULL, null=True)
    plaatsen = models.IntegerField(default=0)
    
    class Meta: 
        verbose_name = "Boot"
        verbose_name_plural = "Boten"

    
    def __str__(self):
        """String for representing the Model object."""
        return self.naam
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('boot-details', args=[str(self.id)])
