from .models import Client, Keydatum, Chats, Friends
from .serializers import ClientSerializer, KeydatumSerializer, ChatSerializer, FriendSerializer
from rest_framework import serializers, views, viewsets

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class KeydatumViewSet(viewsets.ModelViewSet):
    queryset = Keydatum.objects.all()
    serializer_class = KeydatumSerializer

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chats.objects.all()
    serializer_class = ChatSerializer

class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friends.objects.all()
    serializer_class = FriendSerializer