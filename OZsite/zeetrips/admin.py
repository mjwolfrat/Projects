from django.contrib import admin

from .models import Boot, Haven,Vistrip,Visplek

admin.site.register(Haven)
admin.site.register(Visplek)

class VisplekInline(admin.TabularInline):
    model = Visplek

class VistripAdmin(admin.ModelAdmin):
    list_display = ('datum', 'boot')
    inlines = [VisplekInline]

admin.site.register(Vistrip, VistripAdmin)

class VistripInline(admin.TabularInline):
    model = Vistrip

@admin.register(Boot)
class BootAdmin(admin.ModelAdmin):
    list_display = ('naam_boot', 'plaatsen','haven')
    inlines = [VistripInline]