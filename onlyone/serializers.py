from re import L
from typing import final
from rest_framework import serializers
from .models import Client, Keydatum, Chats, Friends
from string import ascii_letters, digits, punctuation
class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = "__all__"

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
        #    final_output = txt.maketrans(str(str(ascii_letters) + str(digits) + str(punctuation) + " "), 'NcljPrCfVYQnFxdTHLpW6072JamMeSsAgEi+,-./:;<=>?@[\]^_`RybqDUukKoGzXZOvwI!"#$%&' + "'" + '()*{|}~' + '134589')
        #    final_output = txt.translate(final_output)
        #    for j in range(len(keys)):
        #        if keys[j] == "":

        #instance_keydata = instance.keydata
        #keys = []
        #txt = str(instance.message)
        #for i in range(1, 16):
        #    exec('keys.append(instance_keydata.key' + str(i) + ')')
        #    exec('key_' + str(i) + ' = instance_keydata.key' + str(i))
        #if instance.to_or_from:
        #    final_output = txt.maketrans(str(str(ascii_letters) + str(digits) + str(punctuation) + " "), 'NcljPrCfVYQnFxdTHLpW6072JamMeSsAgEi+,-./:;<=>?@[\]^_`RybqDUukKoGzXZOvwI!"#$%&' + "'" + '()*{|}~' + '134589')
        #    final_output = txt.translate(final_output)
        #    for j in range(len(keys)):
        #        if keys[j] == "":
        #            overall_range = j + 1
        #            break
        #    
        #    for j in range(overall_range, 1, -1):
        #        exec('final_output = txt.maketrans(final_output, key_' + str(j)  + ')')
        #        final_output = txt.translate(final_output)
        #    return str('Translated to: ' + str(final_output))
        #for j in range(len(keys)):
        #    if keys[j] == "":
        #        overall_range = j + 1
        #        break
        #final_output = txt.maketrans(instance.keydata.key1, str(ascii_letters + digits + punctuation + " "))
        #final_output = txt.translate(final_output)
        #for j in range(2, overall_range + 1):
        #    exec('final_output = txt.maketrans(instance.keydata.key' + str(j) + ', final_output)')
        #    final_output = txt.translate(final_output)
        #final_output = txt.maketrans('NcljPrCfVYQnFxdTHLpW6072JamMeSsAgEi+,-./:;<=>?@[\]^_`RybqDUukKoGzXZOvwI!"#$%&' + "'" + '()*{|}~' + '134589', final_output)
        #final_output = txt.translate(final_output)
        return str("GG")

class KeydatumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keydatum
        exclude = ['user1', 'user2'] #DON'T SHOW IT


class ClientSerializer(serializers.ModelSerializer):
    friends = FriendSerializer(many=True, required=False)
    chats = ChatSerializer(many=True, required=False)
    class Meta:
        model = Client
        fields = "__all__"

