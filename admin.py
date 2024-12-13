from django.contrib import admin
from .models import Habitat, Animal

class AnimalInline(admin.TabularInline):
    model = Animal
    extra = 1  # Número de formularios iniciales

class HabitatAdmin(admin.ModelAdmin):
    inlines = [AnimalInline]

admin.site.register(Habitat, HabitatAdmin)
admin.site.register(Animal)
