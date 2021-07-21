from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import LikedSong, WikiItem, FacebookFriend, TwitterExpert, Recommendation

class RecommendationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recommendation
        fields = ['id', 'name', 'weight', 'image']

class WikiItemSerializer(serializers.ModelSerializer):
    recommendations =  RecommendationSerializer(many=True, read_only=True)

    class Meta:
        model = WikiItem
        fields = '__all__'

class FacebookFriendSerializer(serializers.ModelSerializer):
    recommendations =  RecommendationSerializer(many=True, read_only=True)

    class Meta:
        model = FacebookFriend
        fields = '__all__'

class TwitterExpertSerializer(serializers.ModelSerializer):
    recommendations =  RecommendationSerializer(many=True, read_only=True)

    class Meta:
        model = TwitterExpert
        fields = '__all__'

class LikedSongSerializer(serializers.ModelSerializer):
    wiki_items =  WikiItemSerializer(many=True, read_only=True)
    facebook_friends = FacebookFriendSerializer(many=True, read_only=True)
    twitter_experts = TwitterExpertSerializer(many=True, read_only=True)

    class Meta:
        model = LikedSong
        fields = '__all__'