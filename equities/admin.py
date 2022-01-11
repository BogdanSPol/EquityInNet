from django.contrib import admin
from .models import EquityProject


class EquityAdmin(admin.ModelAdmin):
    readonly_fields = ('date_last_modified', 'add_date_time',)


admin.site.register(EquityProject, EquityAdmin)
