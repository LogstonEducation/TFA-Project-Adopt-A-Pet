from django.forms import ModelForm

from .models import AdoptRequest, Pet


class AdoptRequestForm(ModelForm):
    class Meta:
        model = AdoptRequest
        # All other fields are handled in the background
        fields = [
            'pet',
            'adopter',
        ]


class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'

