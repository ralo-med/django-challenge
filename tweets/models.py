from django.db import models
from django.contrib.auth import get_user_model

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Tweet(BaseModel):
    payload = models.TextField(max_length=180)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='tweets')

    def __str__(self):
        return f"{self.user} - {self.payload[:20]}"

class Like(BaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='likes')
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f"{self.user} likes Tweet {self.tweet.id}"
