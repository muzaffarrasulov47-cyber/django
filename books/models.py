from django.db import models

# Create your models here.

class Cars(models.Model):
    model = models.CharField(max_length=100)
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.model

class Person(models.Model):
    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)
    def __str__(self):
        return self.ism

class Book(models.Model):
    nomi = models.CharField(max_length=150)
    muallif = models.CharField(max_length=150)
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    sahidfalar_soni = models.IntegerField()

    def __str__(self):
        return self.nomi



