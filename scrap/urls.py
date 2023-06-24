from django.urls import path
from . import views

urlpatterns = [
    path('api/scrap', views.scraping_view, name='scraping'),
]