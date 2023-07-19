from rest_framework import viewsets
from virtual_space.models import CelestialObject, Visit
from .serializers import CelestialObjectSerializer, VisitSerializer


class CelestialObjectViewSet(viewsets.ModelViewSet):
    queryset = CelestialObject.objects.all()
    serializer_class = CelestialObjectSerializer


class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
