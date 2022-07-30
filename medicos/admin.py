from django.contrib import admin

from medicos.models import Medico

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'crm', 'email')
