from django.db import models

class Habitat(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    habitat = models.ForeignKey(Habitat, on_delete=models.CASCADE, related_name='animales')

    def __str__(self):
        return self.nombre
