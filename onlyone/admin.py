from django.contrib import admin
from .models import User, Chats, Client
admin.site.register(User)
admin.site.register(Chats)
admin.site.register(Client)
# Register your models here.
