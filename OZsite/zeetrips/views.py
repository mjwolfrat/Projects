from django.shortcuts import render
from zeetrips.models import Vistrip

def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_vistrips =Vistrip.objects.all().count()
    
    context = {
        'num_vistrips': num_vistrips,

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
