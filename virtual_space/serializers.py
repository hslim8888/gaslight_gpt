from rest_framework import serializers
from virtual_space.models import CelestialObject, Visit


class CelestialObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CelestialObject
        fields = '__all__'


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'
