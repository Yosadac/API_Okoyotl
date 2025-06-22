from django.urls import path, include
from rest_framework import routers
from .views import (
    IncendioViewSet, TipoPuestoViewSet, TipoJornadaViewSet,
    CuadrillaViewSet, EstadoRecursoViewSet, PersonalViewSet,
    RecursosViewSet, MapaViewSet, RelPersonalViewSet, RelRecursoViewSet
)

router = routers.DefaultRouter()
router.register(r'incendios', IncendioViewSet)
router.register(r'tipopuestos', TipoPuestoViewSet)
router.register(r'tipojornadas', TipoJornadaViewSet)
router.register(r'cuadrillas', CuadrillaViewSet)
router.register(r'estadoresursos', EstadoRecursoViewSet)
router.register(r'personal', PersonalViewSet)
router.register(r'recursos', RecursosViewSet)
router.register(r'mapas', MapaViewSet)
router.register(r'relpersonal', RelPersonalViewSet)
router.register(r'relrecurso', RelRecursoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
