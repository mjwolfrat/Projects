from django.contrib import admin

from .models import Boot, Haven,Vistrip

admin.site.register(Haven)



class VistripAdmin(admin.ModelAdmin):
    list_display = ('datum', 'boot')

admin.site.register(Vistrip, VistripAdmin)

class VistripInline(admin.TabularInline):
    model = Vistrip

@admin.register(Boot)
class BootAdmin(admin.ModelAdmin):
    list_display = ('naam_boot', 'plaatsen','haven')
    inlines = [VistripInline]