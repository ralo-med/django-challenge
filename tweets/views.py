from django.shortcuts import render
from .models import Tweet
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import TweetSerializer


@api_view(['GET'])
def api_tweet_list(request):
    tweets = Tweet.objects.all()
    serializer = TweetSerializer(tweets, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_user_tweet_list(request, user_id):
    User = get_user_model()
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
    tweets = Tweet.objects.filter(user=user)
    serializer = TweetSerializer(tweets, many=True)
    return Response(serializer.data)


def tweet_list(request):
    tweets = Tweet.objects.all()
    return render(request, 'tweets/tweet_list.html', {'tweets': tweets})
