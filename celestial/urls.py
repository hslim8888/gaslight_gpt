from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CelestialObjectViewSet, VisitViewSet

router = DefaultRouter()
router.register(r'celestial_objects', CelestialObjectViewSet)
router.register(r'visits', VisitViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
