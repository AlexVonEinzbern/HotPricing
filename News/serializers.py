from rest_framework import serializers
from .models import news

# News Serializer
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = news
        fields = ('id', 'newname', 'image', 'title','contenido')
    

# RegisterNew Serializer
class RegisterNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = news
        fields = ('id', 'newname', 'image', 'title','contenido')
        read_only_fields = ('id')

    
