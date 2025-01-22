from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
 
class UserSerializer(serializers.ModelSerializer):
     class Meta:
         model = User
         fields = ['id', 'email', 'password', 'first_name', 'last_name', 'phone', 'address', 'city', 'state', 'country', 'pincode']
         extra_kwargs = {'password': {'write_only': True}}
 
     def validate_password(self, value):
          if len(value) < 8:
                raise ValidationError("Password must be at least 8 characters long.")
          if not any(char.isupper() for char in value):
                raise ValidationError("Password must contain at least one uppercase character.")
          if not any(char.islower() for char in value):
                raise ValidationError("Password must contain at least one lowercase character.")
          return value
     def create(self, validated_data):
         validated_data['password'] = make_password(validated_data['password'])
         return super().create(validated_data)
 
class UserLoginSerializer(serializers.Serializer):
     email = serializers.EmailField()
     password = serializers.CharField(write_only=True)