from django.contrib import admin
from .models import Tweet, Like

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "payload", "like_count", "created_at", "updated_at")
    search_fields = ("user__username", "payload")
    
    def like_count(self, obj):
        return obj.likes.count()

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "tweet", "created_at", "updated_at")
    search_fields = ("user__username", "tweet__id")
