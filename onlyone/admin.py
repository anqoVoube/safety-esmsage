from django.contrib import admin
from django.apps import apps
#class FriendsAdmin(admin.ModelAdmin):
#    def save_model(self, request, obj, form, change):
#        obj.user = request.user
#        logged_in_user = Client.objects.get(username = obj.user)
#        super().save_model(request, obj, form, change)
#        ek = []
#        loop_time = 0
#        if form.cleaned_data['friend_user'].user_subscription == 'F' and form.cleaned_data['related'].user_subscription == 'F':
#            loop_time = 3
#        elif (form.cleaned_data['friend_user'].user_subscription == 'F' and form.cleaned_data['related'].user_subscription == 'M') or (form.cleaned_data['friend_user'].user_subscription == 'M' and form.cleaned_data['related'].user_subscription == 'F'):
#            loop_time = 5
#        elif (form.cleaned_data['friend_user'].user_subscription == 'F' and form.cleaned_data['related'].user_subscription == 'H') or (form.cleaned_data['friend_user'].user_subscription == 'H' and form.cleaned_data['related'].user_subscription == 'F'):
#            loop_time = 8
#        elif (form.cleaned_data['friend_user'].user_subscription == 'M' and form.cleaned_data['related'].user_subscription == 'H') or (form.cleaned_data['friend_user'].user_subscription == 'H' and form.cleaned_data['related'].user_subscription == 'M'):
#            loop_time = 11
#        else:
#            loop_time = 15
#        for j in range(loop_time):
#            strer = []
#            for i in str(string.ascii_letters + string.digits + string.punctuation + " "):
#                strer.append(i)
#            sr = ''.join(random.sample(strer, len(strer)))
#            ek.append(sr)
#        if len(ek) < 15:
#            for i in range(15 - len(ek)):
#                ek.append("")
#        
#        Keydatum.objects.create(user1=form.cleaned_data['friend_user'], user2=logged_in_user,
#                                key1=ek[0], key2=ek[1], key3=ek[2], key4=ek[3], key5=ek[4],
#                                key6=ek[5], key7=ek[6], key8=ek[7], key9=ek[8], key10=ek[9],
#                                key11=ek[10], key12=ek[11], key13=ek[12], key14=ek[13], key15=ek[14])


models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

# Register your models here.
