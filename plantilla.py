from django.shortcuts import render
from django.views.generic import ListView
from django_filters.views import FilterView
from .models import Animal
from .filters import AnimalFilter

class AnimalListView(FilterView, ListView):
    model = Animal
    template_name = 'animal_list.html'
    context_object_name = 'animales'
    filterset_class = AnimalFilter
