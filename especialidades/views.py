from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from medicos.serializers import MedicoSerializer

from .models import Especialidade
from medicos.models import Medico
from .serializers import EspecialidadeSerializer

class EspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    
    @action(detail=True, methods=['GET'])
    def medicos(self, request, pk=None):
        medicos = Medico.objects.filter(especialidades=pk)
        serializer = MedicoSerializer(medicos, many=True)
        return Response(serializer.data)
        