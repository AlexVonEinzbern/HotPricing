from django.contrib.auth import login

# from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view


# Create your views here.

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
    
# login_data = openapi.Parameter('data', openapi.IN_QUERY, description="", required=True, type=openapi.TYPE_OBJECT)
# data_response = openapi.Response('', openapi.Schema(
#     type=openapi.TYPE_OBJECT,
#     properties={
#         "Token ": openapi.Schema(title='AuthToken',  
#                                  description='', 
#                                  type=openapi.TYPE_STRING),
#     },
#     required=["Token"],))

# Login API
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    # @swagger_auto_schema(
    #         method='post', 
    #         request_body=AuthTokenSerializer,
    #         responses={201: data_response},
    #         security=[],)
    # @api_view(['POST'])
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user'] # type: ignore
        login(request, user)
        return super(LoginAPI, self).post(request, format=None) # type: ignore