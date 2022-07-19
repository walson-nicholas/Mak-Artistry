from django.contrib import admin
from .models import Card, Illustration, Journal, Package

class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on')
    search_fields = ['name']

class IllustrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on')
    search_fields = ['name']

class JournalAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on')
    search_fields = ['name']

class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on')
    search_fields = ['name']

admin.site.register(Card, CardAdmin)
admin.site.register(Illustration, IllustrationAdmin)
admin.site.register(Journal, JournalAdmin)
admin.site.register(Package, PackageAdmin)