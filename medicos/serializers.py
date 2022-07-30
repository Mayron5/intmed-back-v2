from rest_framework import serializers
from .models import Medico


class MedicoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {'especialidades': {'write_only': True}}
        model = Medico
        fields = '__all__'
