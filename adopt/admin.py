from django.contrib import admin

# Register your models here.
from .models import Pet
from .models import AdoptRequest

admin.site.register(Pet)
admin.site.register(AdoptRequest)
