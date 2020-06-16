from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Pet
from .forms import AdoptRequestForm


def index(request):
    pets = Pet.objects.all()
    context = {
        'pets': pets,
    }
    return render(request, 'adopt/all.html', context)


def pet_details(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)

    context = {
        'pet': pet,
    }
    return render(request, 'adopt/detail.html', context)


def request_a_pet(request):
    if request.method == 'POST':
        form = AdoptRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({})
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse({})
