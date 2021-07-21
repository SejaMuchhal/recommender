from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import LikedSong, WikiItem, FacebookFriend, TwitterExpert, Recommendation

class LikedSongAdmin(ModelAdmin):
    list_display = ['id', 'name', 'weight', 'image']
    search_fields = ['name']

admin.site.register(LikedSong, LikedSongAdmin)

class WikiItemAdmin(ModelAdmin):
    list_display = ['id', 'name', 'weight', 'image']
    search_fields = ['name']
    list_filter = ['liked_songs']

admin.site.register(WikiItem, WikiItemAdmin)

class FacebookFriendAdmin(ModelAdmin):
    list_display = ['id', 'name', 'weight', 'image']
    search_fields = ['name']
    list_filter = ['liked_songs']

admin.site.register(FacebookFriend, FacebookFriendAdmin)

class TwitterExpertAdmin(ModelAdmin):
    list_display = ['id', 'name', 'weight', 'image']
    search_fields = ['name']
    list_filter = ['liked_songs']

admin.site.register(TwitterExpert, TwitterExpertAdmin)

class RecommendationAdmin(ModelAdmin):
    list_display = ['id', 'name', 'weight', 'image']
    search_fields = ['name']
    list_filter = ['wiki_items', 'facebook_friends', 'twitter_experts']

admin.site.register(Recommendation, RecommendationAdmin)
