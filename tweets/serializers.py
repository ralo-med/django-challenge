from rest_framework import serializers
from .models import Tweet
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined']

class TweetSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Tweet
        fields = ['id', 'payload', 'user', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at'] 
