from typing import ValuesView

from django.db.models.fields import related
from rest_framework.decorators import permission_classes
from .models import Client, Keydatum, Chats, Friends, Searchfriend, OffersToBeFriends
from .serializers import ClientSerializer, KeydatumSerializer, ChatSerializer, FriendSerializer, SearchfriendSerializer, OfferSerializer
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import permissions
from .permissions import IsAdminUserOrReadOnly
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username__username']

class KeydatumViewSet(viewsets.ModelViewSet):
    queryset = Keydatum.objects.all()
    serializer_class = KeydatumSerializer #Remove it
    
class ChatViewSet(viewsets.ModelViewSet):
    serializer_class = ChatSerializer
    def get_queryset(self):
        current_logged_in_user = Client.objects.get(username = self.request.user)
        first_filter = Chats.objects.filter(client_from=current_logged_in_user)
        second_filter_of_chats = Chats.objects.filter(chat_with=current_logged_in_user)
        overall_chats = first_filter | second_filter_of_chats
        return overall_chats

class FriendViewSet(viewsets.ModelViewSet):
    serializer_class = FriendSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    def get_queryset(self):
        current_logged_in_user = Client.objects.get(username = self.request.user)
        first_filter = Friends.objects.filter(friend_user=current_logged_in_user)
        second_filter_of_friends = Friends.objects.filter(related=current_logged_in_user)
        overall = first_filter | second_filter_of_friends
        return overall

class SearchFriendViewSet(viewsets.ModelViewSet):
    serializer_class = SearchfriendSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user_model__username__username']
    def get_queryset(self):
        return Searchfriend.objects.exclude(user_model__username__username=self.request.user.username)

class OfferViewSet(viewsets.ModelViewSet):
    serializer_class = OfferSerializer
    def get_queryset(self):
        current_client_logged_in = Client.objects.get(username = self.request.user)
        getting_offers = OffersToBeFriends.objects.filter(to_user = current_client_logged_in)
        if getting_offers:
            return getting_offers
        return []