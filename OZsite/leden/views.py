from django.shortcuts import render

# Create your views here.
from leden.models import Boot

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_boten = Boot.objects.all().count()
    
    context = {
        'num_boten': num_boten,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)