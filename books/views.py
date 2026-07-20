from django.shortcuts import render
from rest_framework import generics

from .models import Book,Cars,Person
from .serializers import BookSerializer,CarSerializer,PersonSerializer

class BookListApiView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class CarListApiView(generics.ListAPIView):
    serializer_class = CarSerializer
    queryset = Cars.objects.all()

class PersonListApiView(generics.ListAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


