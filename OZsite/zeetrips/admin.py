from django.contrib import admin

from .models import Boot, Haven,Vistrip,Visplek,Soort_trip

admin.site.register(Haven)
admin.site.register(Visplek)
admin.site.register(Soort_trip)

class VisplekInline(admin.TabularInline):
    model = Visplek

class VistripAdmin(admin.ModelAdmin):
    list_display = ('datum','boot','soort_trip')
    inlines = [VisplekInline]

admin.site.register(Vistrip, VistripAdmin)

class VistripInline(admin.TabularInline):
    model = Vistrip

@admin.register(Boot)
class BootAdmin(admin.ModelAdmin):
    list_display = ('naam_boot', 'plaatsen','haven')
    inlines = [VistripInline]