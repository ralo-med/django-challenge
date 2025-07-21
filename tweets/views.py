from django.shortcuts import render
from .models import Tweet
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TweetSerializer, UserSerializer

User = get_user_model()

class TweetList(APIView):
    def get(self, request):
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TweetDetail(APIView):
    def get_object(self, pk):
        try:
            return Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            return None
    
    def get(self, request, pk):
        tweet = self.get_object(pk)
        if tweet is None:
            return Response({'detail': 'Tweet not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TweetSerializer(tweet)
        return Response(serializer.data)
    
    def put(self, request, pk):
        tweet = self.get_object(pk)
        if tweet is None:
            return Response({'detail': 'Tweet not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TweetSerializer(tweet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        tweet = self.get_object(pk)
        if tweet is None:
            return Response({'detail': 'Tweet not found.'}, status=status.HTTP_404_NOT_FOUND)
        tweet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None
    
    def get(self, request, pk):
        user = self.get_object(pk)
        if user is None:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class UserTweetList(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        tweets = Tweet.objects.filter(user=user)
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)

def tweet_list(request):
    tweets = Tweet.objects.all()
    return render(request, 'tweets/tweet_list.html', {'tweets': tweets})
