
from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
     path('', views.index, name='index'),
]
#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('vistrips/', views.VistripListView.as_view(), name='vistrips'),
    path('vistrips/<int:pk>', views.VistripDetailView.as_view(), name='vistrip-detail'),
]