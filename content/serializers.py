from rest_framework import serializers
from .models import Content
from users.serializers import UserSerializer
 
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
         model = Content
         fields = ['id', 'author','title', 'body', 'summary', 'categories', 'created_at', 'updated_at']
         read_only_fields = ('created_at', 'updated_at')
 
class AdminContentSerializer(serializers.ModelSerializer):
     author = UserSerializer(read_only=True)
     class Meta:
         model = Content
         fields = ['id', 'author','title', 'body', 'summary', 'categories', 'created_at', 'updated_at']
         read_only_fields = ('created_at', 'updated_at')