from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state', 'mobile_no', 'gst_no')
    search_fields = ('name',)
    list_filter = ('city',)
    fieldsets = (
        (None, {
            'fields': (('name', 'address'), ('mobile_no', 'city'), ('state', 'gst_no'))
        }),
    )


admin.site.register(Customer, CustomerAdmin)
