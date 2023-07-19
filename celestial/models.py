from django.db import models
from django.contrib.auth.models import User


class CelestialObject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='celestial_images')
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ObservationLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    celestial_object = models.ForeignKey(CelestialObject, on_delete=models.CASCADE)
    observation_date = models.DateField()
    location = models.CharField(max_length=100)
    conditions = models.TextField()
    result = models.TextField()

    def __str__(self):
        return f"Observation by {self.user.username} on {self.observation_date}"


class Photo(models.Model):
    observation_log = models.ForeignKey(ObservationLog, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='observation_photos')
    caption = models.CharField(max_length=255)
    capture_date = models.DateField()

    def __str__(self):
        return f"Photo for Observation: {self.observation_log.id}"
