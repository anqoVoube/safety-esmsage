from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import string
CHOICES = [
('F', 'Free'),
('M', 'Medium Protection'),
('H', 'Hard Protection'),
]

class User(AbstractUser):
    secret_key = models.CharField(max_length = 100)
    def save(self, *args, **kwargs):
        created = not self.pk
        super().save(*args, **kwargs)
        if created:
            Client.objects.create(username = self, user_subscription = 'Free')

class Client(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='main_client_user')
    user_subscription = models.CharField(max_length = 40, choices = CHOICES)
    
class Friends(models.Model):
    friend_user = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='friend_user')
    related = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='related_user_of_friend')
    def save(self, *args, **kwargs):
        created = not self.pk
        super().save(*args, **kwargs)
        if created:
            ek = []
            loop_time = 0
            if self.friend_user.user_subscription == 'Free' and self.related.user_subscription == 'Free':
                loop_time = 3
            elif (self.friend_user.user_subscription == 'Free' and self.related.user_subscription == 'Medium Protection') or (self.friend_user.user_subscription == 'Medium Protection' and self.related.user_subscription == 'Free'):
                loop_time = 5
            elif (self.friend_user.user_subscription == 'Free' and self.related.user_subscription == 'Hard Protection') or (self.friend_user.user_subscription == 'Hard Protection' and self.related.user_subscription == 'Free'):
                loop_time = 8
            elif (self.friend_user.user_subscription == 'Medium Protection' and self.related.user_subscription == 'Hard Protection') or (self.friend_user.user_subscription == 'Hard Protection' and self.related.user_subscription == 'Medium Protection'):
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
            
            Keydatum.objects.create(user1=self.friend_user, user2=self.related,
                                    key1=ek[0], key2=ek[1], key3=ek[2], key4=ek[3], key5=ek[4],
                                    key6=ek[5], key7=ek[6], key8=ek[7], key9=ek[8], key10=ek[9],
                                    key11=ek[10], key12=ek[11], key13=ek[12], key14=ek[13], key15=ek[14])

    class Meta:
        verbose_name = 'friend'
        verbose_name_plural = "friends"

class Keydatum(models.Model):
    user1 = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='key_datas_user1')
    user2 = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='key_datas_user2')
    key1 = models.CharField(max_length = 100)
    key2 = models.CharField(max_length = 100)
    key3 = models.CharField(max_length = 100)
    key4 = models.CharField(max_length = 100, blank=True, null=True)
    key5 = models.CharField(max_length = 100, blank=True, null=True)
    key6 = models.CharField(max_length = 100, blank=True, null=True)
    key7 = models.CharField(max_length = 100, blank=True, null=True)
    key8 = models.CharField(max_length = 100, blank=True, null=True)
    key9 = models.CharField(max_length = 100, blank=True, null=True)
    key10 = models.CharField(max_length = 100, blank=True, null=True)
    key11 = models.CharField(max_length = 100, blank=True, null=True)
    key12 = models.CharField(max_length = 100, blank=True, null=True)
    key13 = models.CharField(max_length = 100, blank=True, null=True)
    key14 = models.CharField(max_length = 100, blank=True, null=True)
    key15 = models.CharField(max_length = 100, blank=True, null=True)

    def save(self, *args, **kwargs):
        created = not self.pk
        super().save(*args, **kwargs)
        if created:
            Chats.objects.create(client_from=self.user1, chat_with = self.user2, keydata = self) #-------autoset client_from logged in user
    class Meta:
        verbose_name = 'keydatum'
        verbose_name_plural = "keydata"

class Chats(models.Model):
    keydata = models.ForeignKey(Keydatum, on_delete=models.CASCADE, null = True, related_name='encrypted_keys')
    client_from = models.ForeignKey(Client, on_delete=models.CASCADE, null = True)
    chat_with = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='chat_with_user', null=True)
    message = models.TextField(max_length=1000, null=True, blank=True)
    to_or_from = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'chat'
        verbose_name_plural = 'chats'