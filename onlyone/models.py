from django.db import models
from django.contrib.auth.models import AbstractUser

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
            Client.objects.create(username = self, user_subscription = 'F')
    
    def __str__(self):
        return self.username

class Client(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='main_client_user')
    user_subscription = models.CharField(max_length=40, choices = CHOICES)
    def save(self, *args, **kwargs):
        created = not self.pk
        super().save(*args, **kwargs)
        if created:
            Searchfriend.objects.create(user_model = self)
    
    def __str__(self):
        return self.username.username
    
class Friends(models.Model):
    friend_user = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='friend_users')
    related = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='friends', null=True)
    class Meta:
        verbose_name = 'friend'
        verbose_name_plural = "friends"

class Keydatum(models.Model):
    user1 = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='key_datas_user1')
    user2 = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='key_datas_user2', null=True)
    key1 = models.CharField(max_length = 100, blank=True, null=True)
    key2 = models.CharField(max_length = 100, blank=True, null=True)
    key3 = models.CharField(max_length = 100, blank=True, null=True)
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
            Chats.objects.create(client_from=self.user1, chat_with = self.user2, keydata = self)
    class Meta:
        verbose_name = 'keydatum'
        verbose_name_plural = "keydata"

class Chats(models.Model):
    keydata = models.ForeignKey(Keydatum, on_delete=models.CASCADE, null=True, related_name='encrypted_keys')
    client_from = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, related_name = 'chats')
    chat_with = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='chat_with_user', null=True)
    message = models.TextField(max_length=1000, null=True, blank=True)
    to_or_from = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'chat'
        verbose_name_plural = 'chats'


class Searchfriend(models.Model):
    user_model = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='search_user')
    is_your_friend = models.BooleanField(default=False)
    is_friend_offer = models.BooleanField(default=False)

class OffersToBeFriends(models.Model):
    to_user = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='offer_to_user')
    from_user = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='offer_from_user')
    accept = models.BooleanField(default=False)