from django.db import models

from medicos.models import Medico

class Horario(models.Model):
    horario = models.TimeField(unique=True)
    
    def __str__(self) -> str:
        return str(self.horario)

class Agenda(models.Model):
    
    medico = models.ForeignKey(Medico, models.CASCADE)
    dia = models.DateField()
    horario = models.ManyToManyField(Horario)
    
    def __str__(self) -> str:
        return  'Médico: ' + str(self.medico) + ' dia: ' + str(self.dia)
    