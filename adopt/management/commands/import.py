import csv

from django.core.management.base import BaseCommand
from django.utils import timezone
from adopt.models import Pet


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        pets = []
        for dict_ in data:
            pets.append(Pet(
                name=dict_['name'],
                birth_date=None,  # Do date conversion
                vaccinated=dict_['vaccinated'].lower() == 'true'
            ))

        Pet.objects.bulk_create(pets)
