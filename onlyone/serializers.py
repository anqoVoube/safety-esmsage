from typing import final
from rest_framework import serializers
from .models import Client, Keydatum, Chats, Friends
from string import ascii_letters
class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = "__all__"

class ChatSerializer(serializers.ModelSerializer):
    output = serializers.SerializerMethodField()
    class Meta:
        model = Chats
        exclude = ['keydata']
        read_only_fields = ['keydata', 'chat_with']
    
    def get_output(self, instance):
        if instance.to_or_from:
            txt = str(instance.message)
            final_output = txt.maketrans(str(ascii_letters), instance.keydata)
            return str('Translated to: ' + str(txt.translate(final_output)))
        txt = str(instance.message)
        final_output = txt.maketrans(instance.keydata, str(ascii_letters))
        return str('Translated from: ' + str(txt.translate(final_output)))

class KeydatumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keydatum
        fields = "__all__" #DON'T SHOW IT


class ClientSerializer(serializers.ModelSerializer):
    friends = FriendSerializer(many=True, required=False)
    chats = ChatSerializer(many=True, required=False)
    class Meta:
        model = Client
        fields = "__all__"

