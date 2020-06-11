from django.test import RequestFactory, TestCase
from django.utils import timezone

from adopt import models
from adopt import views


class AllPetsViewTestCase(TestCase):
    def test_gets_all_pets(self):
        pet = models.Pet.objects.create(
            name='Rover',
            birth_date=timezone.now(),
            vaccinated=True,
        )

        request = RequestFactory().get('/')

        response = views.index(request)

        self.assertIn(pet.name, response.content.decode())


class PetDetailsTestCase(TestCase):
    def test_gets_details(self):
        pet = models.Pet.objects.create(
            name='Rover',
            birth_date=timezone.now(),
            vaccinated=True,
            breed='Border Collie',
        )

        request = RequestFactory().get('/')

        response = views.pet_details(request, pet.id)

        self.assertIn(pet.name, response.content.decode())
        self.assertIn(pet.breed, response.content.decode())


class RequestAPetTestCase(TestCase):
    def test_post(self):
        pet = models.Pet.objects.create(
            name='Rover',
            birth_date=timezone.now(),
            vaccinated=True,
            breed='Border Collie',
        )

        data = {
            'adopter': 'Janet',
            'pet': pet.id,
        }

        request = RequestFactory().post('/', data=data)

        self.assertFalse(models.AdoptRequest.objects.all())

        views.request_a_pet(request, pet.id)

        self.assertTrue(models.AdoptRequest.objects.filter(adopter='Janet').first())
