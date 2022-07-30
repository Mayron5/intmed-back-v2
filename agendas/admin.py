from django.contrib import admin

from agendas.models import Agenda, Horario

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    fields = ('horario', )
    
    
@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    fields = ('medico', 'dia', 'horario')