from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from .models import news
from .serializers import NewsSerializer, RegisterNewSerializer

class newViewSet(viewsets.ModelViewSet):
    queryset = news.objects.all()
    serializer_class=NewsSerializer
    

