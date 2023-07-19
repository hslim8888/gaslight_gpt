from django.core.management.base import BaseCommand
from virtual_space.models import CelestialObject
import random


class Command(BaseCommand):
    help = 'Populates the database with random celestial objects'

    def add_arguments(self, parser):
        parser.add_argument('num_objects', type=int)

    def handle(self, *args, **options):
        num_objects = options['num_objects']

        for _ in range(num_objects):
            CelestialObject.objects.create(
                name='Star ' + str(random.randint(1, 1000000)),
                type='star',
                location_x=random.uniform(-1000, 1000),
                location_y=random.uniform(-1000, 1000),
                location_z=random.uniform(-1000, 1000),
            )
