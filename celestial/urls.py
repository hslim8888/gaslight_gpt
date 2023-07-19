from django.urls import path
from .views import CelestialObjectListCreateAPIView, ObservationLogCreateAPIView, PhotoCreateAPIView

urlpatterns = [
    path('celestial-objects/', CelestialObjectListCreateAPIView.as_view(), name='celestial-object-list-create'),
    path('observation-logs/', ObservationLogCreateAPIView.as_view(), name='observation-log-create'),
    path('photos/', PhotoCreateAPIView.as_view(), name='photo-create'),
]
