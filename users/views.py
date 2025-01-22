from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, UserLoginSerializer
from django.contrib.auth import authenticate
from rest_framework import permissions
from .models import User

class UserRegistrationView(APIView):
  permission_classes = [permissions.AllowAny]
  def post(self, request):
      serializer = UserSerializer(data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
   permission_classes = [permissions.AllowAny]
   def post(self, request):
     serializer = UserLoginSerializer(data=request.data)
     if serializer.is_valid():
         email = serializer.validated_data['email']
         password = serializer.validated_data['password']
         user = authenticate(email=email, password=password)
         if user:
           refresh = RefreshToken.for_user(user)
           return Response({
               'refresh': str(refresh),
               'access': str(refresh.access_token)
             }, status=status.HTTP_200_OK)
         return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminListView(APIView):
    def get(self, request):
        users = User.objects.filter(is_staff=True)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)