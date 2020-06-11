from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect

from .models import Pet
from .forms import AdoptRequestForm
from .forms import PetForm


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


def request_a_pet(request, pet_id):
    initial = {
        'pet': pet_id,
    }
    if request.method == 'POST':
        form = AdoptRequestForm(request.POST, initial=initial)
        if form.is_valid():
            form.save()
            return redirect('adopt:details', pet_id)

    else:
        form = AdoptRequestForm(initial=initial)

    context = {
        'form': form,
    }
    return render(request, 'adopt/request.html', context)


def add_a_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adopt:index')

    else:
        form = PetForm()

    context = {
        'form': form,
    }
    return render(request, 'adopt/add.html', context)
