from django.db import models

from especialidades.models import Especialidade

class Medico(models.Model):
    nome = models.CharField(max_length=255)
    crm = models.IntegerField(unique=True)
    email = models.EmailField(blank=True)
    especialidades = models.ManyToManyField(Especialidade)
    
    class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'
        ordering = ['nome']
    
    def __str__(self) -> str:
        return self.nome