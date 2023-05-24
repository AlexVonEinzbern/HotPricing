from .views import RegisterAPI, LoginAPI
from knox import views as knox_views
from django.urls import path, include

from login import views as login_views

from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', login_views.HomeView.as_view(), name='home'),

    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

    # Login and Logout Social Media accounts
    path('api/login/social', auth_views.LoginView.as_view(), name='login'),
    path('api/logout/social', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    path('api/oauth/', include('social_django.urls', namespace='social')),
]