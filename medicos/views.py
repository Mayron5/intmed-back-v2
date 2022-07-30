from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from medicos.models import Medico
from medicos.serializers import MedicoSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer