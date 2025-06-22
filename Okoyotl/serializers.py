from rest_framework import serializers
from .models import (
    Incendio, TipoPuesto, TipoJornada, Cuadrilla, EstadoRecurso,
    Personal, Recursos, Mapa, RelPersonal, RelRecurso
)

class IncendioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incendio
        fields = '__all__'

class TipoPuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPuesto
        fields = '__all__'

class TipoJornadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoJornada
        fields = '__all__'

class CuadrillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuadrilla
        fields = '__all__'

class EstadoRecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoRecurso
        fields = '__all__'

class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = '__all__'

class RecursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recursos
        fields = '__all__'

class MapaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mapa
        fields = '__all__'

class RelPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelPersonal
        fields = '__all__'

class RelRecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelRecurso
        fields = '__all__'


