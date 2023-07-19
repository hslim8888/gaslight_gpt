from rest_framework import serializers
from .models import CelestialObject, ObservationLog, Photo


class CelestialObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CelestialObject
        fields = '__all__'


class ObservationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObservationLog
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'
