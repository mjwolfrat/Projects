from django.shortcuts import render
from zeetrips.models import Vistrip,Visplek
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_vistrips =Vistrip.objects.all().count()
    
    context = {
        'num_vistrips': num_vistrips,
     
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class VistripListView(generic.ListView):
    model = Vistrip
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(VistripListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

class VistripDetailView(generic.DetailView):
    model = Vistrip


class MijnTripsByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = Visplek
    template_name ='zeetrips/Vistrips_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return Visplek.objects.filter(visser=self.request.user)