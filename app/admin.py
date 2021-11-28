from django.contrib import admin
from .models import Car

# Register your models here.
admin.site.site_header = '"FunMotors" dashboard'
admin.site.site_url = None
admin.site.index_title = 'App administration'


@admin.register(Car)
class AdminCar(admin.ModelAdmin):
    list_display = ('model_name', 'available_from',
                    'manufacturer')
    list_display_links = ('model_name',)
