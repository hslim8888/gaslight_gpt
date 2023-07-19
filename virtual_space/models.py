from django.db import models
from django.utils import timezone


class CelestialObject(models.Model):
    TYPE_CHOICES = [
        ('star', 'Star'),
        ('planet', 'Planet'),
        # 여기에 필요한 다른 타입들을 추가할 수 있습니다.
    ]

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    location_x = models.FloatField()
    location_y = models.FloatField()
    location_z = models.FloatField()


class Visit(models.Model):
    celestial_object = models.ForeignKey(CelestialObject, on_delete=models.CASCADE)
    visit_time = models.DateTimeField(default=timezone.now)
