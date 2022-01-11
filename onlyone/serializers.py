from django.db.models.fields import related
from rest_framework import serializers
from .models import Client, Keydatum, Chats, Searchfriend, OffersToBeFriends, Friends
from string import ascii_letters, digits, punctuation
import string
import random
class KeydatumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keydatum
        fields = '__all__'
        read_only_fields = ['key1', 'key2', 'key3', 'key4', 'key5', 'key6', 'key7', 'key8', 'key9', 'key10', 'key11', 'key12', 'key13', 'key14', 'key15']

class ChatSerializer(serializers.ModelSerializer):
    output = serializers.SerializerMethodField()
    class Meta:
        model = Chats
        fields = "__all__"
        read_only_fields = ['keydata', 'chat_with', 'client_from']

    def get_output(self, instance):
        txt = str(instance.message)
        keys = []
        bits = [instance.keydata.key1, instance.keydata.key2, instance.keydata.key3,
                instance.keydata.key4, instance.keydata.key5, instance.keydata.key6, 
                instance.keydata.key7, instance.keydata.key8, instance.keydata.key9,
                instance.keydata.key10, instance.keydata.key11, instance.keydata.key12, 
                instance.keydata.key13, instance.keydata.key14, instance.keydata.key15]
        for i in range(len(bits) - 1):
            if bits[i] != "":
                keys.append(bits[i])
        overall_range = len(keys) - 1
        our_dict = {}
        for index, value in enumerate(keys):
            our_dict[index] = value
        if instance.to_or_from:
            final_output = txt.maketrans(str(str(ascii_letters) + str(digits) + str(punctuation) + " "), 'NcljPrChtB fVYQnFxdTHLpW6072JamMeSsAgEi+,-./:;<=>?@[\]^_`RybqDUukKoGzXZOvwI!"#$%&' + "'" + '()*{|}~' + '134589')
            final_output = txt.translate(final_output)
            
            final_outputer = final_output.maketrans('NcljPrChtB fVYQnFxdTHLpW6072JamMeSsAgEi+,-./:;<=>?@[\]^_`RybqDUukKoGzXZOvwI!"#$%&' + "'" + '()*{|}~' + '134589', keys[len(keys) - 1])
            final_output = final_output.translate(final_outputer)
            for i in range(overall_range, 0, -1):
                final_outputer = final_output.maketrans(our_dict[i], our_dict[i - 1])
                final_output = final_output.translate(final_outputer)
            return final_output
        final_output = txt.maketrans(our_dict[0], our_dict[1])
        final_output = txt.translate(final_output)
        for i in range(1, overall_range):
            final_outputer = final_output.maketrans(our_dict[i], our_dict[i + 1])
            final_output = final_output.translate(final_outputer)
        final_outputer = final_output.maketrans(our_dict[overall_range], 'NcljPrChtB fVYQnFxdTHLpW6072JamMeSsAgEi+,-./:;<=>?@[\]^_`RybqDUukKoGzXZOvwI!"#$%&' + "'" + '()*{|}~' + '134589')
        final_output = final_output.translate(final_outputer)
        final_outputer = final_output.maketrans('NcljPrChtB fVYQnFxdTHLpW6072JamMeSsAgEi+,-./:;<=>?@[\]^_`RybqDUukKoGzXZOvwI!"#$%&' + "'" + '()*{|}~' + '134589', str(str(ascii_letters) + str(digits) + str(punctuation) + " "))
        final_output = final_output.translate(final_outputer)
        return final_output


class KeydatumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keydatum
        exclude = ['user1', 'user2'] #DON'T SHOW IT

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class SearchfriendSerializer(serializers.ModelSerializer):
    user_model = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Searchfriend
        fields = "__all__"
        read_only_fields = ['is_your_friend', 'user_model']

    def create(self, validated_data):
        return Searchfriend.objects.create(**validated_data)

    def update(self, instance, validated_data):
        friended_user = instance.user_model
        client_user = Client.objects.filter(username = self.context['request'].user)
        client_user = client_user.first()
        instance.is_friend_offer = validated_data.get('is_friend_offer', instance.is_friend_offer)
        if instance.is_friend_offer == True:
            OffersToBeFriends.objects.create(to_user = friended_user, from_user = client_user)
        if Friends.objects.filter(friend_user = friended_user, related = client_user) or Friends.objects.filter(related = friended_user, friend_user = client_user):
            instance.is_your_friend = True
            #If friend do not show offer
        instance.save()
        return instance

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = OffersToBeFriends
        exclude = ['to_user']
        read_only_fields = ['from_user']

    def update(self, instance, validated_data):
        instance.accept = validated_data.get('accept', instance.accept)
        ifu = instance.from_user
        itu = instance.to_user
        if instance.accept == True:
            Friends.objects.create(friend_user = ifu, related = itu)
            need_to_be_deleted_offer = OffersToBeFriends.objects.get(to_user = itu, from_user = ifu)
            need_to_be_deleted_offer.delete()
            f_s = ifu.user_subscription
            field_name = 'user_subscription'
            obj = Client.objects.get(username = self.context['request'].user)
            m_s = getattr(obj, field_name)
            print(m_s)
            ek = []
            loop_time = 0
            if f_s == 'F' and m_s == 'F':
                loop_time = 3
            elif (f_s == 'F' and m_s == 'M') or (f_s == 'M' and m_s == 'F'):
                loop_time = 5
            elif (f_s == 'F' and m_s == 'H') or (f_s == 'H' and m_s == 'F'):
                loop_time = 8
            elif (f_s == 'M' and m_s == 'H') or (f_s == 'H' and m_s == 'M'):
                loop_time = 11
            else:
                loop_time = 15
            for j in range(loop_time):
                strer = []
                for i in str(string.ascii_letters + string.digits + string.punctuation + " "):
                    strer.append(i)
                sr = ''.join(random.sample(strer, len(strer)))
                ek.append(sr)
            if len(ek) < 15:
                for i in range(15 - len(ek)):
                    ek.append("")
            Keydatum.objects.create(
               user1=ifu,
                   user2=itu,
                   key1=ek[0], key2=ek[1], key3=ek[2], key4=ek[3], key5=ek[4],
                   key6=ek[5], key7=ek[6], key8=ek[7], key9=ek[8], key10=ek[9],
                   key11=ek[10], key12=ek[11], key13=ek[12], key14=ek[13], key15=ek[14]
               )

            
        return instance
#Whether leave it on serializers or it'll be better to put that key creation in model save() method?
    
class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        exclude = ['related']
    