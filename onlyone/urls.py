from django.urls import path, include
from rest_framework import routers
from .views import ChatViewSet, ClientViewSet, FriendViewSet, KeydatumViewSet
router = routers.DefaultRouter()
router.register('clients', ClientViewSet)
router.register('chat', ChatViewSet)
router.register('friends', FriendViewSet)
router.register('keydatum', KeydatumViewSet)
urlpatterns = [
    path('', include(router.urls))
]