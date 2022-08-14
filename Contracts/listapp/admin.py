from django.contrib import admin

from .models import Contract

# Register your models here.


class NameAdmin(admin.ModelAdmin):
    list_display = ('name', 'number')


admin.site.register(Contract, NameAdmin)
