from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator

class LikedSong(models.Model):

    name = models.CharField(max_length=500)
    weight = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

class WikiItem(models.Model):

    name = models.CharField(max_length=500)
    weight = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    image = models.ImageField(upload_to='images')
    liked_songs = models.ManyToManyField('LikedSong', blank=True, related_name='wiki_items')

    def __str__(self):
        return self.name

class FacebookFriend(models.Model):

    name = models.CharField(max_length=500)
    weight = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    image = models.ImageField(upload_to='images')
    liked_songs = models.ManyToManyField('LikedSong', blank=True, related_name='facebook_friends')

    def __str__(self):
        return self.name

class TwitterExpert(models.Model):

    name = models.CharField(max_length=500)
    weight = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    image = models.ImageField(upload_to='images')
    liked_songs = models.ManyToManyField('LikedSong', blank=True, related_name='twitter_experts')

    def __str__(self):
        return self.name

class Recommendation(models.Model):

    name = models.CharField(max_length=500)
    weight = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    image = models.ImageField(upload_to='images')
    wiki_items = models.ManyToManyField('WikiItem', blank=True, related_name='recommendations')
    facebook_friends = models.ManyToManyField('FacebookFriend', blank=True, related_name='recommendations')
    twitter_experts = models.ManyToManyField('TwitterExpert', blank=True, related_name='recommendations')

    def __str__(self):
        return self.name