"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tweets.views import tweet_list, TweetList, TweetDetail, UserList, UserDetail, UserTweetList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tweet_list, name='tweet_list'),
    # Tweet API routes
    path('api/v1/tweets/', TweetList.as_view(), name='api_tweet_list'),
    path('api/v1/tweets/<int:pk>/', TweetDetail.as_view(), name='api_tweet_detail'),
    # User API routes
    path('api/v1/users/', UserList.as_view(), name='api_user_list'),
    path('api/v1/users/<int:pk>/', UserDetail.as_view(), name='api_user_detail'),
    path('api/v1/users/<int:pk>/tweets/', UserTweetList.as_view(), name='api_user_tweet_list'),
]
