from rest_framework import serializers
from .models import Hoteles

class HotelesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Hoteles
        fields = '__all__'
