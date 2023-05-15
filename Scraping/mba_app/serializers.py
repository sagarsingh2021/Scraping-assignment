from rest_framework import serializers
from .models import University

class UniversitySerializer(serializers.ModelSerializer):
    '''
        Serialized University Model
    '''
    class Meta:
        model = University
        fields = '__all__'
