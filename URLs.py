from django.urls import path
from .views import AnimalListView

urlpatterns = [
    path('animales/', AnimalListView.as_view(), name='animal_list'),
]