
from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('vistrips/', views.VistripListView.as_view(), name='vistrip'),
    path('vistrip/<int:pk>', views.VistripDetailView.as_view(), name='vistrip-detail'),
    path('mijntrips/', views.MijnTripsByUserListView.as_view(), name='mijn-trips'),
]