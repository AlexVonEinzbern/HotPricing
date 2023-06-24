from .views import newViewSet
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register('api/new', newViewSet, basename='News')

urlpatterns = [
    path('', include(router.urls)),
]