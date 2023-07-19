from django.test import TestCase
from .models import CelestialObject


class CelestialObjectTestCase(TestCase):
    def setUp(self):
        CelestialObject.objects.create(name='Earth', type='planet', location_x=0, location_y=0, location_z=0)

    def test_celestial_object_created(self):
        """Celestial objects are correctly created"""
        earth = CelestialObject.objects.get(name='Earth')
        self.assertEqual(earth.type, 'planet')
