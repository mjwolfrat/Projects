from django.shortcuts import render, redirect, get_object_or_404
from zeetrips.models import Vistrip,Visplek,Boot
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.views.generic.edit import FormMixin
from django.views.generic.detail import DetailView
from .forms import VisplekinschrijfForm
from django.urls import reverse


def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    test1 = Vistrip.objects.filter(boot__naam_boot__iexact='Wiesje')
    if Visplek.objects.filter(vistrip__pk=3, visser__username__icontains=request.user).exists:
        test = 'ja'
    num_vistrips =Vistrip.objects.all().count()
    
    context = {
        'num_vistrips': num_vistrips,'test': test,
     
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

class VistripDetailView(FormMixin, DetailView):
    template_name='zeetrips/vistrip_detail.html'
    model = Vistrip
    form_class = VisplekinschrijfForm

        
    def get_success_url(self):
        return reverse('vistrip-detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        if Visplek.objects.filter(vistrip=self.object,visser__username=self.request.user).exists():
            ingeschreven = 'ja'
        else:
            ingeschreven ='nee'
          

        context = super(VistripDetailView, self).get_context_data(**kwargs)
        context['ingeschreven'] = ingeschreven
        context['form'] = VisplekinschrijfForm(initial={'vistrip': self.object, 'visser':self.request.user})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(VistripDetailView, self).form_valid(form)

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
    form= VisplekForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('mijn-trips')

  
    context= {'form': form }
        
    return render(request, 'zeetrips/Inschrijven.html', context)

def BeheerTrip(request, vistrip_id):
    vistrip = Vistrip.objects.get(pk=vistrip_id)
    plekover = vistrip.boot.plaatsen - vistrip.visplek_set.count()
    plaatsen = vistrip.boot.plaatsen

    VisserFromSet = inlineformset_factory(Vistrip, Visplek, fields=('visser',),extra=plekover,max_num=plaatsen)

    if request.method == 'POST':
        formset = VisserFromSet(request.POST, instance=vistrip)
        if formset.is_valid():
            formset.save()
            return redirect('vistrip-detail', pk=vistrip_id)

    formset = VisserFromSet(instance=vistrip)

    return render(request, 'zeetrips/Beheer_Trip.html', {'formset' : formset, 'plaatsen': plaatsen, 'plekover' : plekover} )
