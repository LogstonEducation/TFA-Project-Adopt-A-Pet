from django.urls import path

from . import views


# Allow for namespaces in reverse URLs
app_name = 'adopt'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pet_id>/', views.pet_details, name='details'),
    path('request/', views.request_a_pet, name='request'),
]
