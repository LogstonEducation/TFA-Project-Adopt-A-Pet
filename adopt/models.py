from django.db import models
from django.utils.translation import gettext as _


class Pet(models.Model):
    name = models.CharField(
        max_length=100,
        help_text=_('Name of pet'),
    )

    breed = models.CharField(
        max_length=100,
        help_text=_('Breed of pet'),
    )

    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

    SEX_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]

    sex = models.CharField(
        max_length=16,
        help_text=_('Sex of pet'),
        choices=SEX_CHOICES,
        default=OTHER,
    )

    birth_date = models.DateField(
        help_text=_('Birthday of pet'),
    )

    vaccinated = models.BooleanField(
        help_text=_('Pet has been vaccinated'),
    )

    profile_image = models.ImageField(
        help_text=_('Profile picture of pet'),
        blank=True,
        upload_to='profile_images',
    )

    bio = models.TextField(
        help_text=_('Biography of Pet'),
    )

    adopt_me_if = models.TextField(
        blank=True,
    )

    first_thing_people_notice_about_me = models.TextField(
        blank=True,
    )

    friday_night = models.TextField(
        blank=True,
    )

    def __str__(self):
        return self.name


class AdoptRequest(models.Model):
    pet = models.ForeignKey(
        'adopt.Pet',
        on_delete=models.CASCADE,
    )

    create_ts = models.DateTimeField(
        # Automatically set when request is saved
        auto_now_add=True,
    )

    adopter = models.EmailField(
        help_text=_('Email of adopter'),
    )

    def __str__(self):
        return f'{self.adopter} at {self.create_ts}'
