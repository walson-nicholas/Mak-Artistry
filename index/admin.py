from django.contrib import admin
from .models import WhatWeDo, WhatsNew, CustomersReview

class WhatWeDoAdmin(admin.ModelAdmin):
    list_display = ('writeUp', 'created_on')
    search_fields = ['writeUp']

class WhatsNewAdmin(admin.ModelAdmin):
    list_display = ('writeUp', 'created_on')
    search_fields = ['writeUp']
    
class CustomersReviewAdmin(admin.ModelAdmin):
    list_display = ('writeUp', 'created_on')
    search_fields = ['writeUp']

admin.site.register(WhatWeDo, WhatWeDoAdmin)
admin.site.register(WhatsNew, WhatsNewAdmin)
admin.site.register(CustomersReview, CustomersReviewAdmin)