from rest_framework import serializers
from .models import Tweet

class TweetSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    payload = serializers.CharField()
    user = serializers.IntegerField(source='user.id')
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField() 
