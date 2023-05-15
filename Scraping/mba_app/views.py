from django.shortcuts import render
from rest_framework import generics
from .models import University
from .serializers import UniversitySerializer



class UniversityList(generics.ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
