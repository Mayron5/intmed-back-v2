from django.contrib import admin
from .models import Especialidade

# Register your models here.
@admin.register(Especialidade)
class EspecialidadesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')