from django.forms import ModelForm

from .models import AdoptRequest


class AdoptRequestForm(ModelForm):
    class Meta:
        model = AdoptRequest
        # All other fields are handled in the background
        fields = [
            'pet',
            'adopter',
        ]
