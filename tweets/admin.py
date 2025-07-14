from django.contrib import admin
from .models import Tweet, Like

class ElonMuskFilter(admin.SimpleListFilter):
    title = "Elon Musk filter"
    parameter_name = "elon"

    def lookups(self, request, model_admin):
        return [
            ("contain", "Elon Musk contain"),
            ("not_contain", "Elon Musk not contain"),
        ]

    def queryset(self, request, queryset):
        val = self.value()
        if val == "contain":
            return queryset.filter(payload__icontains="Elon Musk")
        if val == "not_contain":
            return queryset.exclude(payload__icontains="Elon Musk")
        return queryset

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "payload", "like_count", "created_at", "updated_at")
    search_fields = ("payload", "user__username")
    list_filter = ("created_at", ElonMuskFilter)

    def like_count(self, obj):
        return obj.likes.count()

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "tweet", "created_at", "updated_at")
    search_fields = ("user__username",)
    list_filter = ("created_at",)
