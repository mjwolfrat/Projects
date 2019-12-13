from django.shortcuts import render, redirect
from zeetrips.models import Vistrip,Visplek
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory


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

from django.shortcuts import render
from .forms import VisplekForm

def showform(request):
    form= VisplekForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('mijn-trips')

  
    context= {'form': form }
        
    return render(request, 'zeetrips/Inschrijven.html', context)


def Inschrijven2(request, vistrip_id):
    vistrip = Vistrip.objects.get(pk=vistrip_id)
    plekover = vistrip.boot.plaatsen - vistrip.visplek_set.count()
    plaatsen = vistrip.boot.plaatsen

    VisserFromSet = inlineformset_factory(Vistrip, Visplek, fields=('visser',),extra=plekover,max_num=plaatsen)

    if request.method == 'POST':
        formset = VisserFromSet(request.POST, instance=vistrip)
        if formset.is_valid():
            formset.save()
            return redirect('inschrijven2', vistrip_id=vistrip.id)

    formset = VisserFromSet(instance=vistrip)

    return render(request, 'zeetrips/inschrijven2.html', {'formset' : formset, 'plaatsen': plaatsen, 'plekover' : plekover} )
