from django.contrib import admin

# Register your models here.
from task.models import Site, Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('site', 'a_value', 'b_value', 'date_created')


admin.site.register(Site)
