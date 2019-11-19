from django.contrib import admin

# Register your models here.
from .models import Boot, Haven

admin.site.register(Boot)
admin.site.register(Haven)