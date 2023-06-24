from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Hoteles
from .serializers import HotelesSerializer
from scrap.views import hotel_precio, hotel_nombre, hotel_direccion, hotel_imagenes, ciudad

@api_view(['POST'])
def vista_registro(request):
    # ... Código anterior ...
    print("ciudad: " , ciudad)
    # Obtener los bytes de la imagen
    print("len hotel:nombre: ", len(hotel_nombre))
    for c in range(len(hotel_nombre)):
        hotel = None
        if len(hotel_precio[c]) == 3:
            hotel = Hoteles(ciudad=ciudad[0],hotelname=hotel_nombre[c], direccion=hotel_direccion[c], precio_antes=float(hotel_precio[c][0].split()[1].replace("COP", "").replace(".","").replace(",", ".")),precio_ahora=float(hotel_precio[c][2].replace("COP", "").replace(".","").replace(",", ".")), imagen_uno=hotel_imagenes[c][0], imagen_dos=hotel_imagenes[c][1])    
        elif len(hotel_precio[c])==1:
            hotel = Hoteles(ciudad=ciudad[0], hotelname=hotel_nombre[c], direccion=hotel_direccion[c], precio_antes=0,precio_ahora=0, imagen_uno=hotel_imagenes[c][0], imagen_dos=hotel_imagenes[c][1])
        else:
            hotel = Hoteles(ciudad=ciudad[0], hotelname=hotel_nombre[c], direccion=hotel_direccion[c], precio_antes=0,precio_ahora=float(hotel_precio[c][1].replace("COP", "").replace(".","").replace(",", ".")), imagen_uno=hotel_imagenes[c][0], imagen_dos=hotel_imagenes[c][1])
        
        hotel.save()

    # Crear una instancia del serializador y pasar el objeto del modelo como argumento
    hoteles = Hoteles.objects.all()
    serializer = HotelesSerializer(hoteles, many=True)

    # Devolver una respuesta en formato JSON con los datos serializados
    return Response(serializer.data)

    # Devolver una respuesta en formato JSON con los datos serializados
    


@api_view(['GET'])
def listar_hoteles(request):
    # Obtener todos los registros de la base de datos
    hoteles = Hoteles.objects.all()

    # Crear una instancia del serializador y pasar los objetos obtenidos
    serializer = HotelesSerializer(hoteles, many=True)

    # Devolver una respuesta en formato JSON con los datos serializados
    return Response(serializer.data)

@api_view(['DELETE'])
def eliminar_registro(request, pk):
    try:
        # Obtener el objeto Hoteles con el ID (pk) proporcionado
        hotel = Hoteles.objects.get(pk=pk)
    except Hoteles.DoesNotExist:
        # Si el objeto no existe, devolver una respuesta de error
        return Response({"message": "El registro no existe."}, status=404)

    # Eliminar el objeto
    hotel.delete()

    # Devolver una respuesta exitosa
    return Response({"message": "El registro ha sido eliminado exitosamente."}, status=200)

@api_view(['DELETE'])
def eliminar_registro_completo(request):
    # Obtener todos los objetos Hoteles
    hoteles = Hoteles.objects.all()

    # Eliminar todos los objetos
    hoteles.delete()

    # Devolver una respuesta exitosa
    return Response({"message": "Todos los registros han sido eliminados exitosamente."}, status=200)