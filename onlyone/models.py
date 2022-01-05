from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import string

class User(AbstractUser):
    secret_key = models.CharField(max_length = 100)
    def save(self, *args, **kwargs):
        created = not self.pk
        super().save(*args, **kwargs)
        if created:
            Client.objects.create(username = self)

class Client(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='main_client_user')
    
class Friends(models.Model):
    friend_user = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='friend_user')
    related = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='related_user_of_friend')
    def save(self, *args, **kwargs):
        created = not self.pk
        super().save(*args, **kwargs)
        if created:
            strer = []
            for i in string.ascii_letters:
                strer.append(i)
            sr = ''.join(random.sample(strer, len(strer)))
            Keydatum.objects.create(user1=self.friend_user, user2=self.related, key=sr)
    class Meta:
        verbose_name = 'friend'
        verbose_name_plural = "friends"

class Keydatum(models.Model):
    user1 = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='key_datas_user1')
    user2 = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='key_datas_user2')
    key = models.CharField(max_length = 100)
    def save(self, *args, **kwargs):
        created = not self.pk
        super().save(*args, **kwargs)
        if created:
            Chats.objects.create(keydata = self.key, chat_with = self.user1)
    class Meta:
        verbose_name = 'keydatum'
        verbose_name_plural = "keydata"

class Chats(models.Model):
    keydata = models.CharField(max_length = 100)
    chat_with = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='chat_with_user', null=True)
    message = models.TextField(max_length=1000, null=True, blank=True)
    to_or_from = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'chat'
        verbose_name_plural = 'chats'
