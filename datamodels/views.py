from rest_framework import generics, filters, serializers, status
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from rest_framework.response import Response

from .serializers import LikedSongSerializer, WikiItemSerializer, FacebookFriendSerializer, TwitterExpertSerializer, RecommendationSerializer
from .models import LikedSong, WikiItem, FacebookFriend, TwitterExpert, Recommendation

class DataListView(generics.ListAPIView):

    model = LikedSong
    serializer_class = LikedSongSerializer
    
    pagination_class = None
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend, ]
    filterset_fields = []
    search_fields = ['$name', '^id']
    ordering_fields = ['name', ]
    ordering = ['name', ]

    def get_queryset(self):
        return self.model.objects.all()

    def list(self, request, *args, **kwargs):

        songs = LikedSong.objects.all()
        witems = WikiItem.objects.all()
        fitems = FacebookFriend.objects.all()
        titems = TwitterExpert.objects.all()
        recos = Recommendation.objects.all()
        data = {}
        data['songs'] = self.get_serializer(songs, many=True, context={'request': request}).data
        data['witems'] = WikiItemSerializer(witems, many=True, context={'request': request}).data
        data['fitems'] = FacebookFriendSerializer(fitems, many=True, context={'request': request}).data
        data['titems'] = TwitterExpertSerializer(titems, many=True, context={'request': request}).data
        data['recos'] = RecommendationSerializer(recos, many=True, context={'request': request}).data
        return Response(data,status=status.HTTP_200_OK)