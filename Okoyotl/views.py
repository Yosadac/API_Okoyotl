from rest_framework import viewsets
from rest_framework import permissions
from .models import (
    Incendio, TipoPuesto, TipoJornada, Cuadrilla, EstadoRecurso,
    Personal, Recursos, Mapa, RelPersonal, RelRecurso
)
from .serializers import (
    IncendioSerializer, TipoPuestoSerializer, TipoJornadaSerializer,
    CuadrillaSerializer, EstadoRecursoSerializer, PersonalSerializer,
    RecursosSerializer, MapaSerializer, RelPersonalSerializer, RelRecursoSerializer
)

class IncendioViewSet(viewsets.ModelViewSet):
    queryset = Incendio.objects.all()
    serializer_class = IncendioSerializer
    permission_classes = [permissions.AllowAny]  # Cambia según tu auth

class TipoPuestoViewSet(viewsets.ModelViewSet):
    queryset = TipoPuesto.objects.all()
    serializer_class = TipoPuestoSerializer
    permission_classes = [permissions.AllowAny]

class TipoJornadaViewSet(viewsets.ModelViewSet):
    queryset = TipoJornada.objects.all()
    serializer_class = TipoJornadaSerializer
    permission_classes = [permissions.AllowAny]

class CuadrillaViewSet(viewsets.ModelViewSet):
    queryset = Cuadrilla.objects.all()
    serializer_class = CuadrillaSerializer
    permission_classes = [permissions.AllowAny]

class EstadoRecursoViewSet(viewsets.ModelViewSet):
    queryset = EstadoRecurso.objects.all()
    serializer_class = EstadoRecursoSerializer
    permission_classes = [permissions.AllowAny]

class PersonalViewSet(viewsets.ModelViewSet):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer
    permission_classes = [permissions.AllowAny]

class RecursosViewSet(viewsets.ModelViewSet):
    queryset = Recursos.objects.all()
    serializer_class = RecursosSerializer
    permission_classes = [permissions.AllowAny]

class MapaViewSet(viewsets.ModelViewSet):
    queryset = Mapa.objects.all()
    serializer_class = MapaSerializer
    permission_classes = [permissions.AllowAny]

class RelPersonalViewSet(viewsets.ModelViewSet):
    queryset = RelPersonal.objects.all()
    serializer_class = RelPersonalSerializer
    permission_classes = [permissions.AllowAny]

class RelRecursoViewSet(viewsets.ModelViewSet):
    queryset = RelRecurso.objects.all()
    serializer_class = RelRecursoSerializer
    permission_classes = [permissions.AllowAny]
