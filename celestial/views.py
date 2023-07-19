from rest_framework import generics
from .models import CelestialObject, ObservationLog, Photo
from .serializers import CelestialObjectSerializer, ObservationLogSerializer, PhotoSerializer


class CelestialObjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = CelestialObject.objects.all()
    serializer_class = CelestialObjectSerializer


class ObservationLogCreateAPIView(generics.CreateAPIView):
    queryset = ObservationLog.objects.all()
    serializer_class = ObservationLogSerializer


class PhotoCreateAPIView(generics.CreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
