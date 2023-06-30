from rest_framework import serializers
from .models import Hoteles

class HotelesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Hoteles
        fields = ['id', 'ciudad', 'hotelname', 'direccion', 'precio_antes', 'precio_ahora', 'imagen_uno', 'imagen_dos', 'visitas', 'reservas','urls']

class HotelesVisitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hoteles
        fields = ['visitas']

class HotelesReservasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hoteles
        fields = ['reservas']

class HotelesUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hoteles
        fields = ['urls']
