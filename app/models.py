from django.db import models
from django.contrib.auth.models import User

# Model for each Cryptocurrency's data

class Coins(models.Model):
    coin_id = models.CharField(max_length=200, primary_key=True, unique=True)
    coin_name = models.CharField(max_length=200)
    coin_price = models.DecimalField(max_digits=10, decimal_places=2)
    market_cap = models.DecimalField(max_digits=12, decimal_places=0)
    rank = models.IntegerField()
    price_change = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=200)

    def __str__(self):
        return self.coin_name

# Model for each post's data

class Post(models.Model):
    coin_name = models.CharField(max_length=200, unique=False)
    user = models.CharField(max_length=80)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    up_votes = models.ManyToManyField(User, related_name='post_up_votes', blank=True)
    down_votes = models.ManyToManyField(User, related_name='post_down_votes', blank=True)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title

# Model for each comment's data

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="replies")
    user = models.CharField(max_length=80)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    up_votes = models.ManyToManyField(User, related_name='comment_up_votes', blank=True)
    down_votes = models.ManyToManyField(User, related_name='comment_down_votes', blank=True)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.content

